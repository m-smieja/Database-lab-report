# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information -----------------------------------------------------

project = 'Database Report'
copyright = '2024, Miłosz Śmieja'
author = 'Miłosz Śmieja'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.git', '*/.git', 'venv']

language = 'pl'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = 'Database Report - System CRM'
html_short_title = 'DB Report'

# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'pdflatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'''
        \usepackage[utf8]{inputenc}
        \usepackage[T1]{fontenc}
        \usepackage{lmodern}
        \usepackage{graphicx}
        \usepackage{fancyhdr}
        \usepackage{geometry}
        \geometry{margin=2.5cm}
        \setcounter{secnumdepth}{3}
        \setcounter{tocdepth}{3}
        \usepackage{hyperref}
        \hypersetup{
            colorlinks=true,
            linkcolor=blue,
            filecolor=magenta,
            urlcolor=cyan,
        }
    ''',
    'maketitle': r'''
        \begin{titlepage}
        \centering
        \vspace*{2cm}
        {\Huge\bfseries Database Report\[0.4cm]}
        {\LARGE System zarządzania kontaktami CRM\[2cm]}
        {\Large Autor: ''' + author + r'''\[0.5cm]}
        {\large \today\[4cm]}
        \vfill
        {\large Politechnika\Wydział\Kierunek}
        \end{titlepage}
    ''',
}

latex_documents = [
    ('index', 'database_report.tex', 'Database Report',
     'Miłosz Śmieja', 'manual'),
]

latex_show_urls = 'footnote'
latex_domain_indices = True

# Dodatkowe ścieżki dla submodułów
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('chapter_2'))
sys.path.insert(0, os.path.abspath('task_modules'))
