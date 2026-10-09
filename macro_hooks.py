"""
Allows injection of variables into macro stage of rendering.
This allows for arbitrary use of variables in ARTICLES, (e.g. `docs/.md`).
As opposed to `mkdocs_hooks.py` which works only in template step, (e.g. `overrides/*.html`).
If this is confusing, ask Cal to explain.
"""

import os
import json

module_list_path = os.getenv("MODULE_LIST_PATH", "docs/assets/module-list.json")
tag_index_path = os.getenv("TAG_INDEX_PATH", "docs/assets/tag-index.json")
slurm_limits_path = os.getenv("SLURM_LIMITS_PATH", "docs/assets/slurm-limits.json")


class CaseInsensitiveDict(dict):
    """Dict wrapper allowing `applications[app_name]` lookups regardless of case."""

    def __init__(self, data):
        super().__init__(data)
        self._lower_keys = {k.lower(): k for k in data}

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return super().__getitem__(self._lower_keys[key.lower()])

    def __contains__(self, key):
        return super().__contains__(key) or key.lower() in self._lower_keys

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default


def _tb(size):
    """Slurm memory size in TB, e.g. '6T' -> 6, '512G' -> 0.5."""
    return float(size[:-1]) / {"G": 1024, "T": 1}[size[-1]]


def _tidy(x):
    """21.0 -> 21, 31.5 -> 31.5."""
    if isinstance(x, float):
        x = round(x, 1)
        return int(x) if x.is_integer() else x
    return x


def slurm_limits_for_docs(raw):
    """
    slurm-limits.json in the units the docs use, named in each key.
    Slurm counts time in minutes and CPUs as hardware threads.
    """
    day = 1440
    partitions = raw["partitions"].values()
    threads = max(p["threads_per_core"] for p in partitions)
    debug, normal = raw["qos"]["debug"], raw["qos"]["normal"]
    run_mins = normal["max_tres_run_mins_per_user"]
    priority = raw["priority"]
    limits = {
        "debug": {
            "jobs": debug["max_submit_per_user"],
            "minutes": debug["max_wall_minutes"],
            "nodes": debug["max_tres_per_job"]["node"],
            "cores": debug["max_tres_per_job"]["cpu"] // threads,
            "memory_gb": _tb(debug["max_tres_per_job"]["mem"]) * 1024,
            "gpus": debug["max_tres_per_job"]["gres/gpu"],
            # Points added to job priority. Raw, as NO_NORMAL_ALL turns off normalisation.
            "priority": debug["priority"] * priority["weight_qos"],
        },
        "per_job": {
            "days": max(p["max_walltime_minutes"] for p in partitions) / day,
            "nodes": normal["max_tres_per_job"]["node"],
            "node_days": normal["max_tres_mins_per_job"]["node"] / day,
        },
        "per_user": {
            "cores": normal["max_tres_per_user"]["cpu"] // threads,
            "core_days": run_mins["cpu"] / threads / day,
            "memory_tb": _tb(normal["max_tres_per_user"]["mem"]),
            "tb_days": _tb(run_mins["mem"]) / day,
            "gpus": normal["max_tres_per_user"]["gres/gpu"],
            "gpu_days": run_mins["gres/gpu"] / day,
        },
        "priority": {
            "fairshare_points": priority["weight_fairshare"],
            "age_points_per_hour": priority["weight_age"] / (priority["max_age_minutes"] / 60),
            "age_days": priority["max_age_minutes"] / day,
            "calc_minutes": priority["calc_period_minutes"],
            "half_life_days": priority["decay_half_life_minutes"] / day,
            "half_life_periods": priority["decay_half_life_minutes"] // priority["calc_period_minutes"],
        },
    }
    return {group: {k: _tidy(v) for k, v in values.items()} for group, values in limits.items()}


def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    env.variables.applications = CaseInsensitiveDict(json.load(open(module_list_path)))
    tag_index = json.load(open(tag_index_path))

    @env.macro
    def pages_with_tag(tag):
        entries = tag_index.get(tag.lower(), [])
        try:
            current_dir = os.path.dirname(env.page.file.src_path)
        except AttributeError:
            return entries
        return [
            {"title": e["title"], "path": os.path.relpath(e["path"], current_dir)}
            for e in entries
        ]

    # Not `slurm`, mkdocs.yml `extra.slurm` (the Slurm version) already has that name.
    slurm_limits = json.load(open(slurm_limits_path))
    env.variables["slurm_limits"] = slurm_limits_for_docs(slurm_limits)
    # Pages link to the Slurm docs for this version with `config.extra.slurm`.
    env.conf["extra"]["slurm"] = f"slurm-{slurm_limits['slurm_version']}"
