---
title: "Project: Route Planner"
module: "05-data-structures-and-algorithms"
hours: 40
artifact: "routes: a route planner on real OpenStreetMap data for your own town — graph construction, connectivity analysis, BFS, Dijkstra with your own heap, A*, travel-time routing, and map rendering"
deliverable: "Design doc + benchmark report (Dijkstra vs A*, node expansions, times) + 5-minute demo with routes drawn on a map"
---

# Project: Route Planner

| | |
| :-- | :-- |
| **Module** | 05 Data Structures and Algorithms |
| **Time** | About 40 hours |
| **Prerequisites** | Labs 01–03 (your `MinHeap` and BFS); Math M10 (trigonometry for distances); Module 03 Unit 7 (graphs) |
| **You build** | `routes`, a planner that loads the real street map of your town from OpenStreetMap, turns it into a graph, analyses it, and finds shortest and fastest routes with Dijkstra and A* — using your own priority queue — then draws them on a map you can open in a browser |
| **Deliverable** | Design doc, benchmark report, and demo |

---

## Why this matters

Graphs model anything connected: roads, networks, friendships, dependencies, web links, the states of a game. Shortest-path algorithms run inside every map app, every internet router (Module 09: routing protocols use Dijkstra), and every game AI. Doing it on **your own town's real streets** makes the results checkable by your own experience — you know whether a route is sensible.

You'll also feel the difference between an algorithm that explores blindly (Dijkstra) and one guided by a good estimate (A*), and you'll prove why the guided one still finds the best route.

**Real-world analogs:** OSRM and GraphHopper (open-source routing engines), Google Maps, link-state routing (OSPF), game pathfinding.

> **Data licence:** OpenStreetMap data is © OpenStreetMap contributors and available under the Open Database Licence (ODbL). Credit it in your README and on any map you share.

---

## Milestones

### Milestone 1 — Design doc and the map data

1. **Get data:** export a small area (a few square kilometres around where you live) from openstreetmap.org (**Export** button → `.osm` XML file), or use the Overpass API (search "Overpass turbo") to download roads only. Start small: 5,000–50,000 nodes.
2. **Design doc v1** (3–5 pages): the graph representation (adjacency lists keyed by node id; why not an adjacency matrix? [W] — compute how much memory a matrix would need for your map), what counts as an edge, how you'll handle one-way streets, the algorithms, goals with numbers (e.g. "any route in your town in under 200 ms with A*").
3. **Parse** the XML (Python's `xml.etree.ElementTree` is allowed — XML parsing isn't the point here): `<node id lat lon>` elements, and `<way>` elements with `<nd ref>` lists and `<tag k="highway" v="…">`. Keep ways that are roads/paths you care about (decide which `highway` values for walking vs driving). Respect `oneway=yes` for driving.

### Milestone 2 — Build and analyse the graph

1. **Edges:** consecutive nodes along each way; weight = distance in metres by the **haversine formula** (great-circle distance on a sphere, from latitude and longitude — derive or look up the formula; it's M10 trigonometry on a sphere). Test it: the distance between two known points (measure on the OSM website) should match within 1%.
2. **Stats:** number of nodes and edges; degree distribution (how many nodes have degree 1, 2, 3, 4+? — Module 03's handshake lemma says the degrees sum to 2 × edges for undirected roads: check it!).
3. **Connected components:** with BFS (Lab 03), and again with **union-find** (look it up: a simple structure with `find` and `union`, near-constant time with path compression). Compare. Keep the largest component for routing. [W] Why do real map extracts have many tiny disconnected pieces?
4. **Simplify:** many nodes have degree 2 (just shape points along a curve). Contract chains of degree-2 nodes into single edges with summed lengths, keeping the geometry for drawing. How much smaller does the graph get?

**Done when:** stats, components (both methods agree), and simplification numbers are recorded.

### Milestone 3 — BFS and Dijkstra with your own heap

1. **BFS** finds the route with the fewest **edges** (intersections). Why isn't that the shortest **distance**? Find an example on your map where they differ.
2. **Priority queue:** use your Lab 02 `MinHeap`. Dijkstra needs to lower a node's distance after it's been pushed. Two approaches: (a) **lazy deletion** — push a new (distance, node) entry and skip stale entries when popped; (b) a heap with an **index map** supporting `decrease_key`. Implement (a) first, then (b), and compare speed and memory.
3. **Dijkstra:**
   ```
   # 1. dist[start] = 0; push (0, start)
   # 2. Pop the closest unsettled node u; if stale, skip; mark u settled
   # 3. If u is the goal, stop
   # 4. For each edge u→v with weight w: if dist[u] + w < dist[v], update dist[v], came_from[v] = u, push v
   # 5. Rebuild the path from came_from
   ```
4. **Correctness:** write the proof (Proof Journal): when a node is popped from the heap, its distance is final — because all edge weights are non-negative, any other path to it would have to go through a node at least as far away. [W] Construct a tiny graph with a negative edge where Dijkstra gives the wrong answer.

**Tests:**
- tiny hand-made graphs with known answers;
- on 200 random pairs in your map: Dijkstra's distance equals **Bellman–Ford's** (a slower algorithm that tries every edge n − 1 times — implement it as a second witness, run on a small sub-map);
- every returned path is a real path (consecutive nodes are connected) and its edge weights sum to the reported distance.

**Done when:** all tests pass.

### Milestone 4 — A*

**A*** adds a **heuristic**: an estimate h(v) of the remaining distance from v to the goal. It pops nodes by dist[v] + h(v) instead of dist[v], exploring toward the goal first.

1. Use h(v) = straight-line (haversine) distance from v to the goal.
2. **Admissible** means h never overestimates the true remaining distance. Is straight-line distance admissible for road distance? (Roads can't be shorter than a straight line.) Prove: with an admissible (and consistent) heuristic, A* returns a shortest path.
3. **Measure:** for 200 random pairs, compare Dijkstra and A* by (a) nodes expanded (popped and settled), (b) time, (c) path length (must be equal!). Also try h = 0 (A* becomes Dijkstra) and h = 2 × straight-line distance (no longer admissible — how much faster, and how much worse are the routes?).
4. **Draw the explored nodes** for one pair, for both algorithms (Milestone 6's renderer): Dijkstra explores a circle; A* explores a narrow ellipse toward the goal.

**Done when:** the comparison table and the exploration pictures exist.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *why A* with an honest estimate still finds the best route*. Why-ladder target: *why does overestimating make A* faster but wrong?*

### Milestone 5 — Fastest route, not just shortest

1. Give each edge a **travel time**: length ÷ speed, with speeds by road type (`maxspeed` tag if present; otherwise a table you choose, e.g. residential 30 km/h, primary 50 km/h — M06 unit conversion to m/s).
2. A* heuristic for time: straight-line distance ÷ the **maximum** speed in the map. [W] Why the maximum? (Admissibility again.)
3. Compare the shortest route and the fastest route for 5 trips you actually make. Do the results match what you do in real life? Where not, why?

### Milestone 6 — Draw it

1. **GeoJSON output:** write routes (and explored nodes) as GeoJSON — a simple JSON format for map shapes. Open it at geojson.io or in any GIS viewer to see it on a real map.
2. **SVG output:** project latitude/longitude to x/y (for a small area, the equirectangular approximation is fine: x = lon × cos(mid-latitude), y = lat, then scale — M10), draw all roads in grey, the route in a colour, explored nodes as dots. (Your [Floor Plan and Turtle](../../../00-foundations/math/projects/floor-plan-and-turtle/spec.md) SVG skills.)

**Done when:** a route on your town renders in both formats, with the OSM credit.

---

## Testing guidance

- **Second witnesses:** Bellman–Ford for distances; BFS for reachability; brute-force all-paths on tiny graphs (a few nodes).
- **Property checks** on every returned path.
- **Real-world sense checks:** routes you know.

## Common pitfalls

- **Latitude/longitude order:** many formats use (lon, lat); OSM XML uses separate attributes. Mixing them up puts your town in the ocean.
- **Degrees vs radians** in haversine (M10).
- **One-way streets** in the wrong direction (OSM `oneway=-1` means the reverse of the way's node order).
- **Stale heap entries** processed as if fresh (lazy deletion requires the "skip if stale" check).
- **Comparing floats for equality** when checking Dijkstra vs A* distances — use a tolerance (M06).

## Communication deliverable

1. **Design doc** v1 → v2.
2. **Benchmark report** (2 pages): graph stats; BFS vs Dijkstra example; lazy vs decrease-key; Dijkstra vs A* (expanded nodes, times) including the inadmissible heuristic; shortest vs fastest for your 5 real trips.
3. **Demo (5 minutes):** load the map, plan a real trip, show both algorithms' exploration pictures, and the GeoJSON route on a real map.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 3, write Dijkstra's steps from memory; before Milestone 4, A*'s difference |
| **F** | Dijkstra's settled set; A*'s guidance |
| **W** | Matrix vs lists; disconnected pieces; negative edges; admissibility; max speed in the heuristic |
| **S** | Algorithm subgoal comments; proof structure for correctness |
| **I** | Graphs, heaps, geometry, units, and proofs together |
| **T** | Design doc, report, demo |

## Stretch goals

- **Bidirectional Dijkstra/A*:** search from both ends and meet in the middle. Measure the speed-up.
- **Contraction hierarchies or landmarks (ALT):** preprocessing techniques that make real routing engines fast. Read about one and implement a simple version.
- **Public transport:** load a GTFS timetable (many cities publish one) and route with departure times (time-dependent Dijkstra).
- **Minimum spanning tree** (Kruskal with your union-find): the cheapest set of roads connecting every intersection.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Graph building | Haversine tested; one-ways; stats; components two ways; simplification | Works | Wrong distances |
| Dijkstra | Own heap (both variants); Bellman–Ford witness; proof | Lazy only | Bugs |
| A* | Admissibility proved; expansions measured; inadmissible tried | Works | Missing |
| Travel time | Speeds, time heuristic, 5 real trips | Partial | Missing |
| Rendering | GeoJSON and SVG with exploration views and credit | One format | Missing |
| Communication | Doc lifecycle, report, demo | Most | Few |

**Done when:** every area at least 2; Dijkstra and A* at 3.

## Connections

- **Back:** Lab 02 (`MinHeap`), Lab 03 (BFS), M06 (units), M10 (trigonometry, projection), Module 03 Unit 7 (graphs, handshake lemma), Worldfile's linter (your first BFS).
- **Forward:** Module 09 (routing in networks; shortest-path routing protocols), Module 08 (schedulers with priority queues), Module 12 (graphs as matrices).

> **Originality note:** the project framing (your own town, real data), milestones, and experiments were written for this curriculum. Dijkstra, A*, Bellman–Ford, and union-find are classic algorithms used here as components.
