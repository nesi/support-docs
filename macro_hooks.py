"""
Serves a similar function to 'mkdocs_hooks' except for at render rather than template stage.
"""

import os
import json

module_list_path = os.getenv("MODULE_LIST_PATH", "docs/assets/module-list.json")

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    # add to the dictionary of variables available to markdown pages:
    env.variables.applications = json.load(open(module_list_path))
