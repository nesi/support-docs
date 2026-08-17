"""
mkdocs_hooks allows injection of variables into templating stage of rendering.
This allows for arbitrary use of variables in TEMPLATE FILES, (e.g. `overrides/*.html`).
As opposed to `macro_hooks.py` which injects variables into macro rendering (e.g. `docs/*.md`).
If this is confusing, ask Cal to explain.
"""

import fnmatch
import glob
from pathlib import Path
import json
import os
import re

import yaml
from jinja2.compiler import CodeGenerator
from jinja2.exceptions import TemplateNotFound

module_list_path = os.getenv("MODULE_LIST_PATH", "docs/assets/module-list.json")


class SafeIncludeCodeGenerator(CodeGenerator):
    """Makes every `{% include %}` in this environment render as nothing
    instead of raising, if the included template errors while rendering.

    Partials driven by module-list.json data (versions, network licences,
    ...) can fail on one app's unexpected/missing data. Without this, that
    error propagates and takes out the *whole* page (mkdocs-macros' error
    block) or the *whole* build (the supported-apps index renders every app
    inline via the theme's own Jinja env, outside mkdocs-macros' handling).

    `{% extends %}` and `{% import %}` are untouched (separate visit_*
    methods) - only `{% include %}` gets this treatment.

    Set as `environment.code_generator_class` (an official Jinja extension
    point - see Environment.code_generator_class), it replaces the include's
    normal streaming codegen with a call to `environment.safe_include()`,
    which renders the target as one buffered string (so a mid-render failure
    can't leak partial output) and swallows/logs any exception.
    """

    def visit_Include(self, node, frame):
        self.writeline("yield environment.safe_include(", node)
        self.visit(node.template, frame)
        if node.with_context:
            self.write(f", {{**context.get_all(), **{self.dump_local_context(frame)}}}")
        else:
            self.write(", {}")
        self.write(f", {node.ignore_missing!r})")


def make_safe_include(jinja_env):
    """Build the `environment.safe_include()` called by the codegen above.

    A closure (not a method) bound to one specific environment via
    `env.safe_include = make_safe_include(env)`, since generated template
    code looks it up as a plain attribute (`environment.safe_include(...)`)
    rather than through the descriptor protocol.
    """
    def safe_include(name, context_dict, ignore_missing=False):
        try:
            template = (jinja_env.select_template(name)
                        if isinstance(name, (list, tuple))
                        else jinja_env.get_template(name))
        except TemplateNotFound:
            if ignore_missing:
                return ""
            raise
        try:
            return template.render(context_dict)
        except Exception as e:
            print(f"::WARNING file={name},title=include_failed,col=0,endColumn=0,line=0::{e}")
            return ""
    return safe_include


def configure_safe_includes(jinja_env):
    """Make every `{% include %}` rendered by `jinja_env` fail soft.

    Idempotent - safe to call more than once on the same environment (e.g.
    macro_hooks.py's on_pre_page_macros(), which fires per page).
    """
    if getattr(jinja_env, "_safe_includes_configured", False):
        return
    jinja_env.code_generator_class = SafeIncludeCodeGenerator
    jinja_env.safe_include = make_safe_include(jinja_env)
    jinja_env._safe_includes_configured = True


_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _page_description(path):
    """Return a page's front matter `description` as one line, or None."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None
    match = _FRONT_MATTER.match(text)
    if not match:
        return None
    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        # checks/run_meta_check.py is what reports a malformed meta block; the build
        # itself should skip the page rather than fall over.
        return None
    if not isinstance(meta, dict):
        return None
    description = meta.get("description")
    if not isinstance(description, str):
        return None
    # Folded YAML descriptions span several lines; llms.txt entries are one line each.
    return " ".join(description.split()) or None


def on_config(config, **kwargs):
    """Rewrite the llmstxt section globs into explicit per-page entries.

    mkdocs-llmstxt takes link descriptions only from its own config - it never reads page
    front matter, and a glob entry hands every page it matches the same description.
    Expanding the globs here instead lets each llms.txt link carry its own description,
    which is what lets a reader pick a page without fetching several.

    Hooks are appended last in the plugin collection, so this runs after the plugin's own
    on_config. The plugin expands `sections` in on_files, so the rewrite still lands.
    """
    plugin = config.plugins.get("llmstxt")
    if plugin is None:
        return config

    docs_dir = Path(config.docs_dir)
    uris = sorted(p.relative_to(docs_dir).as_posix() for p in docs_dir.rglob("*.md"))

    sections = {}
    for section, patterns in plugin.config.sections.items():
        entries = []
        seen = set()
        for pattern in patterns:
            matches = sorted(fnmatch.filter(uris, pattern)) if "*" in pattern else [pattern]
            for uri in matches:
                if uri in seen:
                    continue
                seen.add(uri)
                description = _page_description(docs_dir / uri)
                entries.append({uri: description} if description else uri)
        sections[section] = entries

    plugin.config.sections = sections
    return config


def on_env(env, config, files, **kwargs):
    # add entire module list to keyword 'applications
    applications = json.load(open(module_list_path))
    env.globals["applications"] = applications
    # Domains actually in use, for the supported-apps filter UI - derived from
    # the data so it can't drift out of sync the way a hardcoded list would.
    env.globals["domain_whitelist"] = sorted({
        domain
        for app in applications.values()
        for domain in app.get("domains", [])
    })
    configure_safe_includes(env)


def lint(*args, **kwargs):
    # Imported lazily: proselint pulls in google-re2 and a large rule set,
    # and this function is not part of the mkdocs build path.
    import proselint as pl

    output = {}
    print("running linter")
    for file in glob.iglob("docs/**/*.md", recursive=True):
        with open(file, "r") as f:
            output[Path(file).stem] = pl.tools.lint(f.read())
    with open("lint_report.json", "w+") as f:
        f.write(json.dumps(output))
    print(output)
