# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx example'
copyright = '2024, Sukhmanjeet Singh'
author = 'Sukhmanjeet Singh'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'breathe',    
]

breathe_projects = {
  "SphinxExample": "./_build/doxygen/xml"
}

breathe_default_project = "SphinxExample"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_context = {
  'current_version' : "1.0",
  'versions' : [["1.0", "link to 1.0"], ["2.0", "link to 2.0"]],
  'current_language': 'en',
  'languages': [["en", "link to en"], ["de", "link to de"]]
}
