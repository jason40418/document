##
#  @file
#  Configuration file for the Sphinx documentation builder.
#
#  @copyright
#  Copyright (c) 2025, Jason Lin. All rights reserved.<BR>
#
#  SPDX-License-Identifier: BSD-3-Clause
#
#  @par Specification Reference:
#
##
"""
Configuration file for the Sphinx documentation builder.
"""
# -- Project information
project = 'document'
copyright = '2025, Jason Lin'
author = 'Jason Lin'

release = '0.1'
version = '0.1.0'

# -- General configuration
extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
