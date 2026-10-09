# Archived Scripts

One-off migration and fix scripts from the vault's 2026-09/10 restructuring, moved here by [[DR-002 - Vault Refactor and Canonical Numbering|DR-002]].

> [!WARNING] Do not re-run these.
> Most of them rewrite curriculum notes in place, using old assumptions. `refactor.py` assigns `block_id` from the Start Here list, which is where the old wrong numbering came from. `refactor_curriculum.py` deletes `milestone` lines and renames headings. Running either one would undo DR-002.

The read-only checkers (`check_links.py`, `check_orphans.py`, `sum_hours.py`) are replaced by `verify_curriculum.py` in the vault root. It checks links, numbering, frontmatter, prerequisites and the Sequential Flow chain, and prints the planned-hours total.
