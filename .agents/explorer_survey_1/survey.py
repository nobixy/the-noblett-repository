import os
import re
import json
from collections import defaultdict

VAULT_ROOT = '/home/noblixy/The Noblett Repository'

def get_vault_files():
    all_files = []
    md_files = []
    for root, dirs, files in os.walk(VAULT_ROOT):
        # Exclude hidden dirs (.agents, .git, .obsidian)
        dirs[:] = [d for d in sorted(dirs) if not d.startswith('.')]
        for f in sorted(files):
            rel_path = os.path.relpath(os.path.join(root, f), VAULT_ROOT)
            all_files.append(rel_path)
            if f.endswith('.md'):
                md_files.append(rel_path)
    return all_files, md_files

def main():
    all_files, md_files = get_vault_files()
    print(f"Total vault files: {len(all_files)}, MD files: {len(md_files)}")

    # Build file lookup maps
    # Exact paths
    relpath_set = set(all_files)
    relpath_lower_map = {p.lower(): p for p in all_files}

    # Basenames (with extension)
    basename_map = defaultdict(list)
    basename_lower_map = defaultdict(list)
    for p in all_files:
        bn = os.path.basename(p)
        basename_map[bn].append(p)
        basename_lower_map[bn.lower()].append(p)

    # Basenames without extension (primarily for .md and attachments)
    no_ext_map = defaultdict(list)
    no_ext_lower_map = defaultdict(list)
    for p in all_files:
        ne = os.path.splitext(os.path.basename(p))[0]
        no_ext_map[ne].append(p)
        no_ext_lower_map[ne.lower()].append(p)

    wikilink_regex = re.compile(r'!?\[\[([^\]]+)\]\]')
    md_link_regex = re.compile(r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)')

    wikilinks = []
    unresolved_wikilinks = []
    resolved_wikilinks = []

    # Graph structures
    # outgoing: src -> set(target_md_rel_paths)
    outgoing_links = defaultdict(set)
    # incoming: dst -> set(source_md_rel_paths)
    incoming_links = defaultdict(set)
    # raw link instances
    all_link_instances = []

    for src_rel in md_files:
        full_src = os.path.join(VAULT_ROOT, src_rel)
        with open(full_src, 'r', encoding='utf-8') as f:
            content = f.read()

        for m in wikilink_regex.finditer(content):
            raw = m.group(1)
            # Syntax: target#heading|alias
            t = raw
            alias = None
            anchor = None
            if '|' in t:
                t, alias = t.split('|', 1)
            if '#' in t:
                t, anchor = t.split('#', 1)

            target = t.strip()
            item = {
                'source': src_rel,
                'raw': raw,
                'target': target,
                'anchor': anchor,
                'alias': alias,
                'start': m.start(),
                'end': m.end()
            }
            all_link_instances.append(item)

            if not target:
                # Same-page anchor: [[#Heading]]
                item['resolution'] = 'same-page'
                item['resolved_path'] = src_rel
                resolved_wikilinks.append(item)
                continue

            # Resolution strategy
            resolved_path = None
            status = 'dead'
            note = ''

            # 1. Exact relative path from vault root
            if target in relpath_set:
                resolved_path = target
                status = 'exact-relpath'
            elif (target + '.md') in relpath_set:
                resolved_path = target + '.md'
                status = 'exact-relpath-plus-md'
            # 2. Relative to current file directory
            else:
                rel_to_cur = os.path.normpath(os.path.join(os.path.dirname(src_rel), target))
                if rel_to_cur in relpath_set:
                    resolved_path = rel_to_cur
                    status = 'curdir-relpath'
                elif (rel_to_cur + '.md') in relpath_set:
                    resolved_path = rel_to_cur + '.md'
                    status = 'curdir-relpath-plus-md'

            # 3. Basename match without extension (standard Obsidian wikilink)
            if not resolved_path:
                if target in no_ext_map:
                    matches = no_ext_map[target]
                    resolved_path = matches[0]
                    status = 'basename-no-ext' if len(matches) == 1 else 'basename-no-ext-ambiguous'
                elif target in basename_map:
                    matches = basename_map[target]
                    resolved_path = matches[0]
                    status = 'basename-exact' if len(matches) == 1 else 'basename-exact-ambiguous'

            # 4. Check case-insensitive match (potential casing issue)
            if not resolved_path:
                t_low = target.lower()
                if t_low in relpath_lower_map:
                    resolved_path = relpath_lower_map[t_low]
                    status = 'casing-mismatch-relpath'
                elif (t_low + '.md') in relpath_lower_map:
                    resolved_path = relpath_lower_map[t_low + '.md']
                    status = 'casing-mismatch-relpath-plus-md'
                elif t_low in no_ext_lower_map:
                    matches = no_ext_lower_map[t_low]
                    resolved_path = matches[0]
                    status = 'casing-mismatch-basename-no-ext'
                elif t_low in basename_lower_map:
                    matches = basename_lower_map[t_low]
                    resolved_path = matches[0]
                    status = 'casing-mismatch-basename'

            item['status'] = status
            item['resolved_path'] = resolved_path

            if resolved_path:
                resolved_wikilinks.append(item)
                if resolved_path.endswith('.md'):
                    outgoing_links[src_rel].add(resolved_path)
                    incoming_links[resolved_path].add(src_rel)
            else:
                unresolved_wikilinks.append(item)

    print(f"Total wikilinks: {len(all_link_instances)}")
    print(f"Resolved wikilinks: {len(resolved_wikilinks)}")
    print(f"Unresolved/Dead wikilinks: {len(unresolved_wikilinks)}")

    print("\n--- UNRESOLVED LINKS ---")
    for u in unresolved_wikilinks:
        print(f"Source: {u['source']}")
        print(f"  Raw: [[{u['raw']}]] -> Target: '{u['target']}'")

    print("\n--- CASING MISMATCHES (RESOLVED BUT CASING DIFFERS) ---")
    casing_mismatches = [l for l in resolved_wikilinks if 'casing-mismatch' in l['status']]
    for c in casing_mismatches:
        print(f"Source: {c['source']} -> Raw: [[{c['raw']}]] -> Resolved: {c['resolved_path']} ({c['status']})")

    # Analyze orphan notes
    orphans = []
    for md in md_files:
        if len(incoming_links[md]) == 0:
            orphans.append(md)

    print(f"\n--- ORPHAN NOTES ({len(orphans)}) ---")
    for o in orphans:
        out_cnt = len(outgoing_links[o])
        print(f"Orphan: {o} (Outgoing: {out_cnt})")

if __name__ == '__main__':
    main()
