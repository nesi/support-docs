"""
House rules for the prose check (run_proselint.py): words and patterns that shouldn't appear in pages.

Each entry in BANNED_PATTERNS runs as a proselint check named 'reannz.<name>', so one can be turned off in
.proselint.json with "reannz.<name>": false. To ban something new, add an entry here rather than writing a new check.

Standard library only: the CI prose job installs nothing but proselint.
"""

import re

# Pages where old names are expected: dated announcements and release notes record what was true at the time,
# and the maintainer pages (FORMAT.md etc.) name the banned words in order to ban them.
HISTORY_PAGES = r"(?i)(^|/)docs/Announcements/|release_notes"
MAINTAINER_PAGES = r"(^|/)docs/[A-Z]+\.md$"
# Downloaded from other repositories (eg. the glossary), so not edited here. No rule runs on these.
FETCHED_FILES = r"(^|/)docs/assets/"

# Words and patterns that shouldn't appear in pages. Matched one line at a time, case-sensitively unless 'flags' says otherwise.
#   name: the check is reported as 'reannz.<name>'.
#   scope "text": prose only, so code blocks, inline code, link targets and HTML tags are ignored.
#   scope "markup": the line as written, link targets and HTML included, but not code blocks.
#   scope "all": code too, for things that are wrong wherever they appear (eg. hostnames).
#   level: "notice" or "warning" (the default). Only warnings fail CHECKS_STRICT.
#   skip: path patterns the entry doesn't apply to.
#   message: '{0}' is replaced with the matched text, or with the pattern's capture group if it has one.
BANNED_PATTERNS = [
    {
        "name": "nesi",
        "pattern": r"(?<!Infrastructure \()(?<![‘'\"])\bNeSI\b(?![’'\"]|-REANNZ| Keycloak)",
        "scope": "text",
        "level": "notice",
        "skip": [HISTORY_PAGES, MAINTAINER_PAGES],
        "message": "Call the organisation REANNZ and the platform Mahuika. Only write NeSI where a name still \
carries it (see 'Names and terms' in FORMAT.md).",
    },
    {
        # 'the HPC Portal' and 'the HPC platform' are names, 'HPC GridRunner' is a Trinity tool.
        "name": "the_hpc",
        "pattern": r"\b[Tt]he HPC\b(?! (?:[Pp]ortal|[Pp]latform|GridRunner))",
        "scope": "text",
        "level": "notice",
        "skip": [HISTORY_PAGES, MAINTAINER_PAGES],
        "message": "Call the platform Mahuika (or 'the cluster' after the first mention), not '{0}'.",
    },
    {
        "name": "hpc3",
        "pattern": r"\bHPC3\b",
        "scope": "text",
        "level": "notice",
        "skip": [HISTORY_PAGES, MAINTAINER_PAGES],
        "message": "'HPC3' was a temporary name for Mahuika, call it Mahuika.",
    },
    {
        "name": "retired_hostname",
        "pattern": r"\b(?:lander|login|mahuika|maui)\.nesi\.org\.nz\b",
        "scope": "all",
        "level": "warning",
        "skip": [HISTORY_PAGES],
        "message": "'{0}' is a retired hostname. Use the hosts in Standard_Terminal_Setup.md \
(login.hpc.nesi.org.nz, through lander.hpc.nesi.org.nz).",
    },
    {
        "name": "nesi_ssh_alias",
        "pattern": r"^\s*Host\s+nesi\s*$|\bssh\b[^#\n]*?\snesi\b(?![.\w-])|(?<![\w./-])nesi:(?!//)",
        "scope": "all",
        "level": "warning",
        "skip": [HISTORY_PAGES],
        "message": "The SSH host alias set up in Standard_Terminal_Setup.md is 'mahuika', not 'nesi', \
so this fails for readers who followed it.",
    },
    {
        "name": "generic_heading",
        "pattern": r"^#{2,6}\s+(Introduction|Overview|Description|Summary|Details|Background|General)\s*:?\s*$",
        "flags": re.IGNORECASE,
        "scope": "text",
        "level": "notice",
        "message": "Heading '{0}' doesn't say what its section is about. Name the topic instead, \
or if it's the first heading remove it: the text after the title is the introduction.",
    },
    {
        "name": "placeholder_alt_text",
        "pattern": r"!\[\s*(alt text|alt|image|img|picture|screenshot|this is an image)\s*\]\("
                   r"|!\[([^\]]*\.(?:png|jpe?g|gif|svg|webp))\s*\]\(|!\[\s*(mceclip\d*[^\]]*)\]\(",
        "flags": re.IGNORECASE,
        "scope": "text",
        "level": "warning",
        "skip": [MAINTAINER_PAGES],
        "message": "Image alt text '{0}' is a placeholder. Describe what the image shows, as if no image were \
visible: screen readers and the docs chat assistant only get this text.",
    },
    {
        # Click [here](for more details)
        "name": "click_here",
        "pattern": r"\[[^\]]*\bhere\b[^\]]*\]\([^)]*\)",
        "flags": re.IGNORECASE,
        "scope": "markup",
        "message": "Don't use 'here' for link text, impedes accessibility.",
    },
    {
        # Any mention of support@nesi.org.nz: a markdown or HTML link, an autolink, or raw text.
        # fix_support_mailto_link.py fixes the links.
        "name": "support_mailto_link",
        "pattern": r"(\[[^\]]*\]\((mailto:)?support@nesi\.org\.nz[^)]*\)"
                   r"|<a\s[^>]*href=[\"'](mailto:)?support@nesi\.org\.nz[^>]*>"
                   r"|<(mailto:)?support@nesi\.org\.nz>"
                   r"|(mailto:)?support@nesi\.org\.nz)",
        "flags": re.IGNORECASE,
        "scope": "markup",
        "message": 'Don\'t reference support@nesi.org.nz directly, use the \
{% include "partials/support_request.html" %} macro instead.',
    },
]


def _blank(m):
    return " " * len(m.group(0))


def mask_non_prose(line):
    """Blanks out inline code, link targets and HTML tags, keeping columns, so 'text' rules don't see them."""
    line = re.sub(r"`[^`]*`", _blank, line)
    line = re.sub(r"(?<=\]\()[^)]*(?=\))", _blank, line)
    return re.sub(r"<[^>]+>", _blank, line)
