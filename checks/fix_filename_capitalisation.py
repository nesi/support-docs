#!/usr/bin/env python3

"""
Auto-fixes the 'title_capitalisation' warning from run_meta_check.py for
pages with NO front-matter 'title:' (mkdocs derives the title from the
filename instead): renames the file itself, updates every internal
link/.pages.yml nav entry that pointed at the old name, and records the move
in redirect_map.yml so external/bookmarked links still resolve.

Skipped, on purpose:
- Anything under Software/Available_Applications/ - software names often
  have legitimate non-standard casing (fastStructure, ollama, VASP) that
  titlecase() would mangle.
- Filenames that are entirely uppercase once separators are stripped (eg.
  GLOSSARY, MACROS, MATLAB) - a strong signal it's an intentional acronym or
  product name, not an undercased phrase.
- Filenames containing 'nesi-org-nz' - that's the my.nesi.org.nz brand
  rendered lowercase-hyphenated by convention (see the sibling directory of
  the same name), not a phrase to titlecase.
"""

import re
import subprocess
from pathlib import Path

import yaml
from titlecase import titlecase

DOC_ROOT = Path("docs")
EXCLUDED_FROM_RENAME = [
    r"docs/assets/.*",
    r".*/index\.md",
    r"docs/Software/Available_Applications/.*",
]
REDIRECT_MAP_PATH = DOC_ROOT / "redirect_map.yml"


def mkdocs_title(stem):
    """Matches mkdocs' own Page.title fallback - see run_meta_check.py's _title_from_filename."""
    name = stem.replace("-", " ").replace("_", " ")
    if name.lower() == name:
        name = name.capitalize()
    return name


def is_acronym_or_brand(stem):
    bare = stem.replace("_", "").replace("-", "")
    return bare.isupper() or "nesi-org-nz" in stem.lower().replace("_", "-")


def word_level_rename(stem):
    """Re-cases each underscore/hyphen-separated word via titlecase(), keeping
    the original separators and word boundaries untouched. Returns None if
    titlecase() changed the word count (unsafe to remap 1:1)."""
    tokens = re.split(r"([_-])", stem)
    words, seps = tokens[0::2], tokens[1::2]

    new_words = titlecase(" ".join(words)).split(" ")
    if len(new_words) != len(words):
        return None

    out = [new_words[0]]
    for sep, word in zip(seps, new_words[1:]):
        out += [sep, word]
    return "".join(out)


def update_references(old_name, new_name):
    """Rewrites internal links/nav entries across docs/ from old filename to new,
    matching both the full filename and the bare stem (for extensionless links)."""
    old_stem, new_stem = old_name.removesuffix(".md"), new_name.removesuffix(".md")
    pattern = re.compile(
        r"(?<=[/(\s-])(" + re.escape(old_name) + "|" + re.escape(old_stem) + r")(?=[)#\s\"']|$)",
        re.MULTILINE,
    )
    changed = []
    for path in list(DOC_ROOT.rglob("*.md")) + list(DOC_ROOT.rglob(".pages.yml")):
        content = path.read_text()
        new_content, n = pattern.subn(
            lambda m: new_name if m.group(1) == old_name else new_stem, content
        )
        if n:
            path.write_text(new_content)
            changed.append(path)
    return changed


def update_redirect_map(old_rel, new_rel):
    if not REDIRECT_MAP_PATH.exists():
        return
    lines = [line for line in REDIRECT_MAP_PATH.read_text().splitlines() if line.strip()]
    updated = []
    for line in lines:
        key, sep, value = line.partition(":")
        if sep and value.strip() == old_rel:
            updated.append(f"{key}: {new_rel}")
        else:
            updated.append(line)
    updated.append(f"{old_rel}: {new_rel}")
    REDIRECT_MAP_PATH.write_text("\n".join(updated) + "\n")


def rename_file(path):
    content = path.read_text()
    match = re.match(r"---\n([\s\S]*?)---", content, re.MULTILINE)
    meta = yaml.safe_load(match.group(1)) if match else {}
    if meta and "title" in meta:
        return None  # handled by fix_title_capitalisation.py instead

    title = mkdocs_title(path.stem)
    if titlecase(title) == title:
        return None  # not actually miscapitalised

    if is_acronym_or_brand(path.stem):
        return "acronym"

    new_stem = word_level_rename(path.stem)
    if new_stem is None or new_stem == path.stem:
        return None

    new_path = path.with_name(new_stem + ".md")
    if new_path.exists():
        print(f"CONFLICT: {new_path} already exists, skipping rename of {path}")
        return None

    subprocess.run(["git", "mv", str(path), str(new_path)], check=True)
    refs = update_references(path.name, new_path.name)
    update_redirect_map(str(path.relative_to(DOC_ROOT)), str(new_path.relative_to(DOC_ROOT)))
    return path, new_path, refs


def main():
    renamed, skipped_acronym = [], []
    for path in sorted(DOC_ROOT.rglob("*.md")):
        if any(re.match(p, str(path)) for p in EXCLUDED_FROM_RENAME):
            continue
        result = rename_file(path)
        if result == "acronym":
            skipped_acronym.append(path)
        elif result:
            renamed.append(result)

    for old, new, refs in renamed:
        print(f"renamed: {old} -> {new} ({len(refs)} referencing file(s) updated)")
    print(f"\nRenamed {len(renamed)} file(s).")

    if skipped_acronym:
        print(f"\nSkipped (looks like an acronym/brand name), {len(skipped_acronym)}:")
        for path in skipped_acronym:
            print(f"  {path}")


if __name__ == "__main__":
    main()
