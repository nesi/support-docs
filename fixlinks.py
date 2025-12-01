# python


# Note: Partially AI generated. Not to be trusted.
import argparse, os, re, sys
from pathlib import Path

MD_ROOT = Path("docs")
LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def all_md_files(root):
    return [p for p in root.rglob("*.md")]

def resolve_target(base_md, target):
    # separate anchor
    target_path, *anchor = target.split('#',1)
    anchor = ('#' + anchor[0]) if anchor else ''
    if not target_path:
        return target, False  # anchor-only
    # if target is directory index usually index.md?
    cand = (base_md.parent / target_path).resolve()
    # try direct existence
    if cand.exists():
        return os.path.relpath(cand, base_md.parent) + anchor, True
    # try adding .md
    if not target_path.endswith(".md"):
        cand2 = (base_md.parent / (target_path + ".md")).resolve()
        if cand2.exists():
            return os.path.relpath(cand2, base_md.parent) + anchor, True
    return None, False

def find_candidates(basename, root):
    return [p for p in root.rglob("*.md") if p.name == basename]

def main(dry_run):
    md_files = all_md_files(MD_ROOT)
    fixes = []
    for md in md_files:
        text = md.read_text(encoding="utf8")
        changed = text
        for m in LINK_RE.finditer(text):
            link_text = m.group(1)
            target = m.group(2).strip()
            if target.startswith(("http://","https://","mailto:")): 
                continue
            if target.startswith("/"): 
                # absolute path inside site — leave for manual review
                continue
            # try to resolve relative target
            newrel, ok = resolve_target(md, target)
            if ok:
                # target exists as given relative path - nothing to do
                continue
            # not found: try to find file by basename
            base = os.path.basename(target.split('#',1)[0])
            if not base:
                continue
            candidates = find_candidates(base, MD_ROOT)
            if len(candidates) == 1:
                cand = candidates[0]
                rel = os.path.relpath(cand, md.parent)
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
            # backup then write
            bak = md.with_suffix(md.suffix + ".bak")
            if not bak.exists():
                bak.write_bytes(text.encode("utf8"))
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
    parser.add_argument("--apply", action="store_true", help="apply fixes")
    args = parser.parse_args()
    main(dry_run=not args.apply)
