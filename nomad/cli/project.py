# -*- coding: utf-8 -*-

import os

from ..client import get_client
from ..conf import Config
from ..project import Project


def get_project():
    """ Returns a fully functional `Project` instance that will be used by the CLI tools. """
    base_dir = '.'

    # Fetches the config options from the current directory.
    # Note/TODO: this could be improved by adding a parameter allowing to manually set the base dir.
    config = Config.from_base_dir(base_dir)

    # Determines the name of the project from the config file or using the base directory.
    project_name = config['name'] or os.path.basename(os.path.abspath(base_dir))

    # Initializes the client instance that will be used to orchestrate containers.
    client = get_client()

    return Project.from_config(project_name, os.path.abspath(base_dir), client, config)