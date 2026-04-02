import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Open MICKY'
copyright = '2026, FBOT@Research'
author = 'FBOT@Research'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.youtube'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme_options = {
    # --- Configuração das Logos ---
    "light_logo": "Submarca_fundo_claro.png", # O nome do seu arquivo para o tema claro
    "dark_logo": "Submarca_fundo_escuro.png",  # O nome do seu arquivo para o tema escuro

    # --- Cores personalizadas para o modo claro ---
    "light_css_variables": {
        "color-brand-primary": "#2980b9", 
        "color-brand-content": "#2980b9", 
    },
    
    # --- Cores personalizadas para o modo escuro ---
    "dark_css_variables": {
        "color-brand-primary": "#ff5500", 
        "color-brand-content": "#ff5500", 
    },
}

html_theme = 'furo'
html_static_path = ['_static']
# html_logo = "_static/Submarca_fundo_claro.png"