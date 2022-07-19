# Configuration file for Sphinx.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = 'dummy'
copyright = '2022, dummy'
author = 'dummy'

# Sphinx Extensions
extensions = [
    'myst_parser',
    'breathe'
]

# Enable processing of markdown files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Add breathe support for reading in Doxygen content
breathe_projects = {
    'template_project':'../doxygen/build/xml'
}
breathe_default_project = 'template_project'
