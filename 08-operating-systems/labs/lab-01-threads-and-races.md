---
title: "Lab 01 — Threads and Races"
module: "08-operating-systems"
hours: 10
---

# Lab 01 — Threads and Races

**Goal:** write multithreaded C correctly — see a race condition happen, fix it with a mutex, coordinate threads with condition variables, cause and fix a deadlock, and let ThreadSanitizer find bugs for you.

**Time:** about 10 hours, in four sessions.

---

## Session 1 — Threads and the first race (2 hours)

A **thread** is a separate flow of execution inside a process. Threads share the process's memory (globals, heap) but each has its own stack and registers. (Compare: `fork` creates a separate process with its own copy of memory.)

```c
#include <pthread.h>
#include <stdio.h>

long counter = 0;

void *worker(void *arg) {
    (void)arg;
    for (int i = 0; i < 1000000; i++)
        counter++;                // read, add one, write back
    return NULL;
}

int main(void) {
    pthread_t a, b;
    pthread_create(&a, NULL, worker, NULL);
    pthread_create(&b, NULL, worker, NULL);
    pthread_join(a, NULL);
    pthread_join(b, NULL);
    printf("%ld\n", counter);    // expected 2000000
    return 0;
}
```

Compile with `-pthread`. Run it 10 times. Record the results. They're less than 2,000,000, and different each time.

**[W] Why?** `counter++` is three machine steps (load, add, store — Module 06 Lab 01: look at it in Compiler Explorer). If both threads load the same value before either stores, one increment is lost. This is a **race condition**: the result depends on timing. Draw the interleaving that loses an update [R].

**ThreadSanitizer:** compile with `-fsanitize=thread -g` and run once. Read the report: it names both accesses and both threads.

---

## Session 2 — Mutexes and atomics (3 hours)

A **mutex** (mutual exclusion lock) makes a block of code run by one thread at a time:

```c
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
/* in worker: */
pthread_mutex_lock(&lock);
counter++;
pthread_mutex_unlock(&lock);
```

Now it's always 2,000,000. Time it: how much slower is it than the racy version? Try locking once around the whole loop instead. [W] What's the trade-off between fine-grained and coarse-grained locking?

**Atomics:** `<stdatomic.h>` gives hardware-supported atomic operations: `atomic_fetch_add(&counter, 1)`. Time it too.

**Exercise — a thread-safe hash map:** take your Module 07 C hash map; make it safe for 4 threads doing random inserts and lookups (one global lock first; then one lock per bucket). Measure throughput for both. Run under TSan: no reports.

---

## Session 3 — Condition variables: the bounded buffer (3 hours)

Threads often need to **wait** for something: a producer waits for space; a consumer waits for data. Spinning in a loop (`while (empty) {}`) burns the CPU. A **condition variable** lets a thread sleep until another thread signals.

**Build a bounded buffer** (your Module 05 `RingQueue`, in C, shared between threads):

```c
// put(x):  lock; while (count == CAP) wait(&not_full, &lock);
//          add x; count++; signal(&not_empty); unlock
// get():   lock; while (count == 0) wait(&not_empty, &lock);
//          remove x; count--; signal(&not_full); unlock; return x
```

- `pthread_cond_wait` **releases the lock while sleeping** and re-acquires it before returning.
- **Always wait in a `while` loop, not an `if`.** [W] Why? (Spurious wakeups; and another thread may have taken the item between the signal and your wake-up.)

**Test:** 3 producers each put the numbers 1…100,000; 3 consumers take them; check that the sum of everything taken equals 3 × the sum of 1…100,000 (Gauss, M11), and that nothing is taken twice. Under TSan: clean.

---

## Session 4 — Deadlock (2 hours)

**Cause one:** two locks A and B; thread 1 locks A then B; thread 2 locks B then A. Add a short `usleep` between the two lock calls. Run it: it hangs. Attach `gdb -p <pid>` and `thread apply all bt` to see each thread waiting for the other's lock.

**The four conditions** for deadlock (look them up: mutual exclusion, hold and wait, no preemption, circular wait). Break one:
- **Lock ordering:** every thread takes A before B. Fix and verify.
- **trylock and back off:** `pthread_mutex_trylock`; if B is busy, release A and retry.

**[W]:** your kernel will need locks too, and it can't call `pthread_mutex_lock`. What will a lock look like inside a kernel, where the "threads" include interrupt handlers? (Seedling M4 answers this: spinlocks with interrupts disabled.)

---

## Done when

- [ ] Race demonstrated, explained with a drawn interleaving, and fixed three ways (mutex, coarse lock, atomic) with timings.
- [ ] Thread-safe hash map (two locking strategies) measured and TSan-clean.
- [ ] Bounded buffer passes the sum test under TSan.
- [ ] Deadlock caused, observed in gdb, and fixed two ways.

## Retrieval and reflection

1. **[R]:** why `counter++` races; what a mutex and a condition variable each do; why `while` around `wait`; the four deadlock conditions.
2. **[F] (spoken, 2 min):** "What is a race condition?" — with your drawn interleaving.
