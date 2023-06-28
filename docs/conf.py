# -*- coding: utf-8 -*-
"""Sphinx configuration file."""
import imp
import sys
import os
import shlex

import django
from django.conf import settings


base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Manual setup is required for standalone Django usage
# NOTE: Since documentation is built using the built/installed package when
# using Tox, it can't use the 'test.settings' Django settings module.
settings.configure(
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'resolwe.observers',
        'resolwe.permissions',
        'resolwe.flow',
        'resolwe.storage',
        'resolwe_bio',
    ),
)
django.setup()

# Get package metadata from 'resolwe_bio/__about__.py' file
about = {}
with open(os.path.join(base_dir, 'resolwe_bio', '__about__.py')) as f:
    exec(f.read(), about)

# -- General configuration ------------------------------------------------

# The extension modules to enable.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'resolwe.flow.utils.docs.autoprocess'
]

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = about['__title__']
version = about['__version__']
release = version
author = about['__author__']
copyright = about['__copyright__']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Parent directory of all process definitions:
autoprocess_process_dir = os.path.join(base_dir, 'resolwe_bio', 'processes')

# Base of the url to process source code:
autoprocess_source_base_url = 'https://github.com/genialis/resolwe-bio/blob/master/resolwe_bio/processes/'

# Process definitions url
autoprocess_definitions_uri = 'catalog-definitions.html'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme'

templates_path = ['_templates']
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'Resolwebiodoc'

# Configuration for intersphinx
_django_major_version = "{}.{}".format(*django.VERSION[:2])
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'django': ('https://docs.djangoproject.com/en/{}/'.format(_django_major_version),
               'https://docs.djangoproject.com/en/{}/_objects/'.format(_django_major_version)),
    'resolwe': ('https://resolwe.readthedocs.io/en/latest', None),
}
