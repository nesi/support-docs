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
        "pattern": r"(?<!Infrastructure \()(?<![‘'\"])\b(?:NeSI|NESI|Nesi)\b(?![’'\"]|-REANNZ| Keycloak)",
        "scope": "text",
        "level": "notice",
        "skip": [HISTORY_PAGES, MAINTAINER_PAGES],
        "message": "Call the organisation REANNZ and the platform Mahuika. Only write NeSI where a name still \
carries it (see 'Names and terms' in FORMAT.md).",
    },
    {
        # 'the HPC Portal' and 'the HPC platform' are names, 'HPC GridRunner' is a Trinity tool.
        "name": "the_hpc",
        "pattern": r"\b(?:[Tt]he|[Oo]ur|[Tt]his) HPCs?\b(?! (?:[Pp]ortal|[Pp]latform|GridRunner))",
        "scope": "text",
        "level": "notice",
        "skip": [HISTORY_PAGES, MAINTAINER_PAGES],
        "message": "Call the platform Mahuika (or 'the cluster' after the first mention), not '{0}'.",
    },
    {
        "name": "hpc3",
        "pattern": r"\bHPC[- ]?3\b",
        "flags": re.IGNORECASE,
        "scope": "text",
        "level": "notice",
        "skip": [HISTORY_PAGES, MAINTAINER_PAGES],
        "message": "'HPC3' was a temporary name for Mahuika, call it Mahuika.",
    },
    {
        "name": "retired_hostname",
        "pattern": r"\b(?:lander|login|mahuika|maui)\d*\.nesi\.org\.nz\b|\b[\w-]+\.(?:mahuika|maui)\.nesi\.org\.nz\b"
                   r"|\bmaui-[\w-]+\.nesi\.org\.nz\b",
        "scope": "all",
        "level": "warning",
        "skip": [HISTORY_PAGES],
        "message": "'{0}' is a retired hostname. Use the hosts in Standard_Terminal_Setup.md \
(login.hpc.nesi.org.nz, through lander.hpc.nesi.org.nz).",
    },
    {
        "name": "retired_jupyterhub",
        "pattern": r"\bjupyter\.nesi\.org\.nz\b",
        "flags": re.IGNORECASE,
        "scope": "all",
        "level": "warning",
        "skip": [HISTORY_PAGES],
        "message": "'{0}' (JupyterHub) is retired. Use JupyterLab in Mahuika OnDemand (ondemand.nesi.org.nz) instead.",
    },
    {
        "name": "nesi_ssh_alias",
        "pattern": r"^\s*Host\s+(?:\S+\s+)*nesi(?:\s|$)|\b(?:ssh|sftp|sshfs|mosh|autossh)\b[^#\n]*?\snesi\b(?![.\w-])"
                   r"|\bProxyJump\s+(?:\S+,)*nesi\b(?![.\w-])|(?<![\w./-])nesi:(?!//)",
        "scope": "all",
        "level": "warning",
        "skip": [HISTORY_PAGES],
        "message": "The SSH host alias set up in Standard_Terminal_Setup.md is 'mahuika', not 'nesi', \
so this fails for readers who followed it.",
    },
    {
        "name": "generic_heading",
        "pattern": r"^#{2,6}\s+(Introduction|Intro|Overview|Description|Summary|Details|Background|General(?: information)?"
                   r"|About|Info|Information|(?:More|Further|Additional|Other) (?:information|details|info)|Notes?|Other"
                   r"|Misc(?:ellaneous)?|Conclusions?)\s*:?\s*$",
        "flags": re.IGNORECASE,
        "scope": "text",
        "level": "notice",
        "message": "Heading '{0}' doesn't say what its section is about. Name the topic instead, \
or if it's the first heading remove it: the text after the title is the introduction.",
    },
    {
        "name": "placeholder_alt_text",
        "pattern": r"!\[\s*(alt[ -]?text|alt|this is an image|untitled|placeholder|todo"
                   r"|(?:an? )?(?:image|img|picture|pic|photo"
                   r"|screen ?shot|figure|fig|diagram|graphic|icon)(?:\s*\d+)?)\s*\]\("
                   r"|!\[([^\]]*\.(?:png|jpe?g|gif|svg|webp|bmp|tiff?|avif|heic))\s*\]\(|!\[\s*(mceclip\d*[^\]]*)\]\("
                   r"|!\[\s*(screen ?shot \d{4}-\d\d-\d\d[^\]]*)\]\(",
        "flags": re.IGNORECASE,
        "scope": "text",
        "level": "warning",
        "skip": [MAINTAINER_PAGES],
        "message": "Image alt text '{0}' is a placeholder. Describe what the image shows, as if no image were \
visible: screen readers and the docs chat assistant only get this text.",
    },
    {
        # Click [here](for more details), [this page](...), [link](...), [read more](...), <a href="...">here</a>
        "name": "click_here",
        "pattern": r"\[([^\]]*\bhere\b[^\]]*)\]\([^)]*\)"
                   r"|\[\s*((?:(?:this|that|the)\s+)?(?:link|page|website|site|url))\s*\]\(|\[\s*(this|that)\s*\]\("
                   r"|\[\s*((?:read |learn |find out |see )?more(?: info(?:rmation)?| details)?)\s*\]\("
                   r"|<a\s[^>]*>\s*((?:click\s+)?here)\s*</a>",
        "flags": re.IGNORECASE,
        "scope": "markup",
        "message": "Link text '{0}' doesn't say where the link goes, which doesn't help screen reader users. "
                   "Name the destination instead.",
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


def _term(name, pattern, message, flags=re.IGNORECASE, skip=(), level="notice"):
    """A preferred-term rule: a notice (or warning) on prose, outside history and maintainer pages."""
    return {"name": name, "pattern": pattern, "flags": flags, "scope": "text", "level": level,
            "skip": [HISTORY_PAGES, MAINTAINER_PAGES, *skip], "message": message}


# Preferred terms, one rule per term. Notices by default: make one a "warning" once its existing hits are fixed.
# Not checked yet: terms that are fine once the preferred one has been used on the page ('MFA' after
# 'multi-factor authentication', 'WSL', 'SMT', 'interactive job'). That needs a page-level 'first_mention' check.
BANNED_PATTERNS += [
    _term("log_in", r"\blog(?:s|ged|ging)? into\b|\blog-in\b|\bsign(?:s|ed|ing)?[- ]?in(?:to)?\b|\blogged[- ]on\b"
                    r"|\b(?:log(?:s|ged|ging)?[- ]on|logon) (?:to|with|using|via)\b"
                    r"|(?<!the )(?<!your )(?<!every )(?<!a )\b(?:(?:to|can|could|will|would|may|might|then|now|also|just|"
                    r"please|must|should|cannot|not|you|we|they|first|successfully|securely|and|have|ll) login\b(?! nodes?)"
                    r"|login (?:to|into|with|using|via|again|as|from)\b)",
          "Write 'log in' (or 'log in to') for the verb, not '{0}'. 'Login' is the noun.",
          level="warning"),
    _term("mfa", r"\bmultiple[- ]?factor(?: authentication)?\b|\bmulti ?factor(?: authentication)?\b"
                 r"|\b(?:two|2|dual)[- ]?factor(?: authentication)?\b|\b2FA\b|\bsecond[- ]factor authentication\b"
                 r"|\b(?:two|2)[- ]?step (?:verification|authentication|login)\b|\b2SV\b",
          "Write 'multi-factor authentication' (then 'MFA'), not '{0}'."),
    _term("second_factor", r"\b(?:second|2nd)[- ]factors?\b(?! (?:authentication|codes?)\b)|\bauthentication tokens?\b"
                           r"|\bMFA tokens?\b",
          "Write 'additional authentication credentials', not '{0}'."),
    _term("six_digit_code", r"\b6 ?digit (?:codes?|numbers?|pins?|tokens?|passcodes?)\b"
                            r"|\b6-digit (?:numbers?|pins?|tokens?|passcodes?)\b"
                            r"|\bsix[- ]digit (?:codes?|numbers?|pins?|passcodes?)\b"
                            r"|\b(?:second|2nd)[- ]factor codes?\b|\bOTPs?\b"
                            r"|(?<!based )\bone[- ]?time (?:codes?|passwords?|passcodes?|pins?)\b",
          "Write '6-digit code', not '{0}'."),
    _term("authenticator_app", r"\bauthentication app(?:lication)?s?\b|\bauthenticator applications?\b"
                               r"|\b(?:MFA|auth) apps?\b",
          "Write 'authenticator app', not '{0}'."),
    _term("singularity", r"\bSingularity(?:-?CE)?\b|\bsingularity (?:exec|run|build|shell|pull|instance)\b",
          flags=0, skip=[r"/Apptainer\.md$"],
          message="Singularity is now called Apptainer. Write 'Apptainer', not '{0}', unless you mean the old name."),
    # Lowercase 'time' only, so the Slurm Composer's 'Wall Time' label is left alone.
    _term("walltime", r"\b[Ww]all[- ]times?\b|\b[Ww]all[- ]?clock(?: times?)?\b", flags=0,
          message="Write 'walltime', not '{0}'."),
    # Lowercase 'job' only, so the Slurm Composer's 'Array Job' label is left alone.
    _term("job_array", r"\b[Aa]rray[- ]?jobs?\b|\b(?:[Ss]lurm|[Tt]ask) arrays?\b(?! jobs?\b)", flags=0,
          level="warning", message="Write 'job array', not '{0}'."),
    # Case-sensitive: SchedMD writes both 'FairShare' and 'Fairshare', every other spelling is flagged.
    # Not after '- ', so the 'fairshare' tag in front matter is left alone.
    _term("fairshare", r"\b(?i:fair[- ]shar(?:e|es|ing))\b|(?<!- )\b(?!Fair[Ss]hares?\b)(?i:fairshar(?:e|es|ing))\b",
          flags=0, message="Write 'FairShare' (or 'Fairshare'), not '{0}'."),
    _term("hyperthreading", r"\bhyper[- ]?thread(?:ing|s|ed)?\b",
          message="Write 'simultaneous multithreading' (then 'SMT'), not '{0}'. Hyper-Threading is Intel's name for it."),
    _term("multithreading", r"\bmulti[- ]thread(?:ing|ed|s)?\b",
          "Write it as one word ('multithreading', 'multithreaded'), not '{0}'."),
    _term("filesystem", r"\bfile[- ]systems?\b", "Write 'filesystem', not '{0}'."),
    _term("long_term_storage", r"\blong ?term (?:data )?(?:storage|archiv(?:e|es|al|ing))\b",
          "Hyphenate 'long-term' before a noun ('long-term storage'), not '{0}'."),
    _term("directory", r"\b(?:project|home|nobackup|scratch) folders?\b|\bsub[- ]director(?:y|ies)\b|\bsub[- ]?folders?\b",
          "Write 'directory' ('project directory', 'home directory', 'subdirectory'), not '{0}'."),
    _term("project_code", r"\bproject[- ]?(?:IDs?|numbers?|identifiers?)\b|\baccount codes?\b|\bproject accounts?\b",
          "Write 'project code', not '{0}'."),
    # Not 'REANNZ team members', who are staff.
    _term("project_member", r"\b(?:project|your|fellow|new|read-only|other) team[- ]members?\b",
          "Write 'project member', not '{0}'."),
    # Not field labels such as 'User name:'.
    _term("username", r"\b(?:user[- ]names?|user[- ]?IDs?|login (?:names?|IDs?))\b(?!\s*:)", "Write 'username', not '{0}'.",
          level="warning"),
    # Lowercase 'license' only, so quoted licence texts ('the License') are left alone.
    _term("licence", r"\b(?:[Aa]|[Tt]he|[Tt]his|[Tt]hat|[Yy]our|[Mm]y|[Oo]ur|[Tt]heir|[Nn]o|[Aa]ny|[Vv]alid|own|software|"
                     r"commercial|academic|free|site|research|institutional) licenses?\b"
                     r"|\b[Ll]icense (?:servers?|files?|keys?|holders?|agreements?|tokens?|terms|fees?|costs?"
                     r"|managers?|types?"
                     r"|pools?|checks?|details|requirements?|restrictions?|conditions?)\b", flags=0,
          message="Write 'licence' for the noun ('license' is the verb), not '{0}'."),
    _term("licensed", r"\blicenc(?:ed|ing)\b", "Write 'licensed' or 'licensing' (from the verb 'license'), not '{0}'."),
    _term("set_up", r"\b(?:to|can|could|will|would|may|might|you|we|they|then|now|first|also|just|and|must|should|please|"
                    r"not|ll|is|are|was|were|be|been|being|get|gets|got|have|has|had) setup\b"
                    r"|\bsetup (?:your|the|a|an|my|our|their|this|that|these|those|it|them)\b|\bset-ups?\b|\bsetting-up\b",
          "Write 'set up' for the verb and 'setup' for the noun, not '{0}'."),
    _term("runtime", r"\brun[- ]times?\b", "Write 'runtime', not '{0}'."),
    _term("website", r"\bweb[- ](?:sites?|pages?)\b", "Write 'website' or 'webpage', not '{0}'.",
          level="warning"),
    # Not field labels such as 'Host name:'.
    _term("filename", r"\b(?:file|host)[- ]names?\b(?!\s*:)", "Write it as one word ('filename', 'hostname'), not '{0}'.",
          level="warning"),
    _term("x11_forwarding", r"\bX[- ]forwarding\b|\bX11-forwarding\b|\bx11[- ]forwarding\b|\bX[- ]11[- ]forwarding\b",
          flags=0, message="Write 'X11 forwarding', not '{0}'."),
    # Not GPU names such as 'A100 80GB'.
    _term("size_units", r"(?<!A100 )(?<!H100 )(?<!PCIe )\b\d+(?:\.\d+)?(?:[KMGTP]i?B|kB|[KMGT]b)\b", flags=0,
          message="Put a space between the number and the unit ('20 GB'), not '{0}'."),
]


def _blank(m):
    return " " * len(m.group(0))


def mask_non_prose(line):
    """Blanks out inline code, link targets and HTML tags, keeping columns, so 'text' rules don't see them."""
    line = re.sub(r"`[^`]*`", _blank, line)
    line = re.sub(r"(?<=\]\()[^)]*(?=\))", _blank, line)
    return re.sub(r"<[^>]+>", _blank, line)
