# Tries to replace all internal broken links with less broken ones.
# Note: Partially AI generated. Not to be trusted.
import argparse, os, re, sys
from pathlib import Path

MD_ROOT = Path("docs")
LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def all_md_files(root):
    return [p for p in root.rglob("**/*.md")]

def resolve_path(base_md, target):
    # separate anchor
    target_path, *anchor = target.split('#',1)
    anchor = ('#' + anchor[0]) if anchor else ''
    if not target_path:
        return False  # anchor-only
    # if target is directory index usually index.md?
    cand = (base_md.parent / target_path).resolve()
    # try direct existence
    if cand.exists():
        return True
    return False

def find_exact_candidates(basename, root):
    return [p for p in root.rglob("*.md") if p.name == basename]

def find_similar_candidates(basename, root):
    return [p for p in root.rglob("*.md") if jaccard_similarity(p.name, basename) > 0.5] 


def jaccard_similarity(s1, s2):
        set1 = set(s1.split(".")[0].lower().split("_")) # Split into words
        set2 = set(s2.split(".")[0].lower().split("_"))
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        if (intersection / union) > 0:
            print(f"{s2}:{s1} {intersection / union}")
        return intersection / union

def main(dry_run):
    md_files = all_md_files(MD_ROOT)
    fixes = []
    for md in md_files:
        text = md.read_text(encoding="utf8")
        changed = text
        for m in LINK_RE.finditer(text):
            target = m.group(2).strip()
            if target.startswith(("http://","https://","mailto:","/")): 
                continue
            if resolve_path(md, target):
                continue
            # not found: try to find file by basename
            base = os.path.basename(target.split('#',1)[0])
            if not base:
                continue
            candidates = find_exact_candidates(base, MD_ROOT)
            if ~len(candidates):
                candidates = find_similar_candidates(base, MD_ROOT)
            if len(candidates) == 1:
                rel = os.path.relpath(candidates[0], md.parent)
                # preserve anchor
                anchor = ''
                if '#' in target:
                    anchor = '#' + target.split('#',1)[1]
                new_target = rel.replace(os.path.sep, "/") + anchor
                fixes.append((md, target, new_target))
                changed = changed.replace("(%s)" % target, "(%s)" % new_target)
            elif len(candidates) > 1:
                print("MULTIPLE CANDIDATES:", md, target, "=>", [str(p) for p in candidates])
            else:
                print("NO CANDIDATE:", md, target)
        if fixes and not dry_run:
            md.write_text(changed, encoding="utf8")
    # report
    if fixes:
        print("\nProposed / Applied fixes:")
        for f in fixes:
            print(f[0], ":", f[1], "=>", f[2])
    else:
        print("No fixes proposed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="will not write out unless present")
    args = parser.parse_args()
    main(dry_run=not args.apply)
