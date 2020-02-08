# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'TurboTeleBASIC'
copyright = '2020, The TurboTeleBASIC Team'
author = 'The TurboTeleBASIC Team'
release = '0.1.0'
master_doc = 'index'

# -- General configuration ---------------------------------------------------

xtensions = []
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
