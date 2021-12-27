# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import json
import os
import sys
import configparser

from pdf2image import convert_from_path
from pathlib import Path

# sys.path.insert(0, os.path.abspath('.'))


# -- INI configuration file --------------------------------------------------

config = configparser.ConfigParser()

if 'SPHINX_CONF_INI' in os.environ and os.environ['SPHINX_CONF_INI'] != "":
    ini_file = Path(os.environ['SPHINX_CONF_INI'])
    if ini_file.is_file():
        config.read(os.environ['SPHINX_CONF_INI'])
    else:
        print ("Cannot access file: " + os.environ['SPHINX_CONF_INI'])
        sys.exit(1)

def get_file_from_conf_ini(path_to_file):
    """Get path to file indicated in "conf.ini" file

    Convert relative to absolute path if necessary.
    """
    f = Path(path_to_file)

    if not f.is_file():
        # Try relative path to conf.ini file
        conf_ini_dir = os.path.dirname(os.environ['SPHINX_CONF_INI'])
        f = Path(conf_ini_dir + "/" + path_to_file)

    assert f.is_file(), f"Cannot find file: {f}"

    return str(f)


# -- Project information -----------------------------------------------------

project = u'learn.adacore.com'
copyright = u'2018 – 2021, AdaCore'
author = u'AdaCore' if not config.has_option('', 'author') else \
    config['DEFAULT']['author']
title = u'Learn Ada (Complete)' if not config.has_option('', 'title') else \
    config['DEFAULT']['title']
publisher = u'AdaCore'

# Automatic version/release string based on date
version_date = datetime.date.today().strftime('%Y.%m')
release_date = datetime.date.today().strftime('%Y-%m')

# The short X.Y version
version = version_date

# The full version, including alpha/beta/rc tags
release = release_date
release_name = 'Release'

if config.has_option('', 'version'):
    version = config['DEFAULT']['version']
    release = config['DEFAULT']['version']
    release_name = 'Version'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# Find the widgets extension
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import widget_extension

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
#    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'widget_extension',
    'sphinx_rtd_theme',
    'sphinx_reredirects',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [u'_build',
                     'Thumbs.db',
                     '.DS_Store',
                     'old-content',
                     'sass',
                     '**/node_modules',
                     'internal',
                     '**/package.json',
                     '**/webpack.config.js'
                     'built',
                     'dist',
                     'src']

# Exclude internal and unfinished material from final site build
if 'GEN_LEARN_SITE' in os.environ and os.environ['GEN_LEARN_SITE'] == "yes":
    exclude_patterns += ['**internal/**']
else:
    # When not building final site, `todo` and `todoList` produce output
    todo_include_todos = True

if 'HIDDEN_BOOKS' in os.environ and os.environ['HIDDEN_BOOKS'] != "":

    hidden_books_file_name = os.environ['HIDDEN_BOOKS']

    with open(hidden_books_file_name, 'r') as hidden_books_file:
        for hidden_book in hidden_books_file.readlines():
            exclude_patterns += ["**{}/**".format(hidden_book.strip())]

show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

nitpicky = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'learn_theme'
html_theme = 'sphinx_rtd_theme'

html_title = "learn.adacore.com"
smartquotes = False

html_theme_path = ['.'] # make sphinx search for themes in current dir

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': False,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_logo = "img/logo.svg"

html_favicon = "img/favicon.ico"

html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['img',]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# Keep this as True. Setting to False makes the search have no descriptions
html_copy_source = True

html_context = {
    'year': datetime.date.today().strftime('%Y'),
}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'learnadacorecomdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'xelatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
\usepackage{pmboxdraw} \usepackage{unicode-math}
\usepackage{pdfpages}
\fvset{fontsize=\small}
''',

    # Font package inclusion
    #
    'fontpkg': r'''
\setmainfont{Open Sans}
\setsansfont{Open Sans}
\setmonofont{DejaVu Sans Mono}
''',

    # Latex figure (float) alignment
    #
    'figure_align': 'htbp',

    # Avoid blank page for chapters on odd pages
    # 'extraclassoptions': 'openany',

    # Sphinx Setup (LaTeX-type customization)
    #
    'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',

    'sphinxsetup': '''
VerbatimBorderColor={rgb}{0.90,0.90,0.90},
VerbatimColor={rgb}{0.99,0.99,0.99},
TitleColor={named}{MidnightBlue}
''',
    # 'verbatimwithframe=false'

    # Inline code cannot be highlighted, see
    # https://github.com/sphinx-doc/sphinx/issues/5157

    'releasename': release_name,
}

if config.has_option('', 'cover_page'):
    pdf_cover_page = get_file_from_conf_ini(config['DEFAULT']['cover_page'])

    latex_elements['maketitle'] = r'''
\begin{titlepage}
\includepdf{''' + pdf_cover_page + r'''}
\sphinxmaketitle
\end{titlepage}
'''

latex_logo = 'img/logo.png'

latex_show_urls = 'footnote'

latex_show_pagerefs = True

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'learnadacorecom.tex', title,
     author, 'manual'),
]

if config.has_option('', 'latex_toplevel_sectioning'):
    latex_toplevel_sectioning = config['DEFAULT']['latex_toplevel_sectioning']

# -- Options for Epub output ---------------------------------------------------

epub_title = title
epub_author = author.replace(r' \\and', ' and')
epub_publisher = publisher
epub_copyright = copyright
epub_description = release_name + " " + release

epub_version = 3.0

epub_theme = '_epub_theme'

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
epub_cover = ()
if config.has_option('', 'cover_page'):
    epub_cover = ("_static/cover.jpeg", "epub-cover.html")

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['cover-A4.pdf', '.nojekyll', '_static/favicon.ico',
                      'learn_meta_image.jpeg']
#    ['_static/opensearch.xml', '_static/doctools.js',
#    '_static/jquery.js', '_static/searchtools.js', '_static/underscore.js',
#    '_static/basic.css', 'search.html', '_static/websupport.js']

# The depth of the table of contents in toc.ncx.
epub_tocdepth = 3
if config.has_option('', 'epub_tocdepth'):
    epub_tocdepth = int(config['DEFAULT']['epub_tocdepth'])

# Allow duplicate toc entries.
epub_tocdup = False

epub_show_urls = 'footnote'

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'learnadacorecom', title,
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'learnadacorecom', title,
     author, 'learnadacorecom', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {'learn': ('https://learn.adacore.com/', None)}

# -- Options for redirects extension -----------------------------------------

redirects = { }


def setup(app):

    # TODO: find a better way to retrieve the current target (html/latex/epub)
    if 'html' in app.outdir:
        templates_path.append('_templates')

        redirects.update({
            "courses/Ada_For_The_C_Embedded_Developer/index": "../Ada_For_The_Embedded_C_Developer/",
            "courses/GNAT_Toolchain_Getting_Started/index": "../GNAT_Toolchain_Intro/"
        })


        if not os.getenv('FRONTEND_TESTING'):
            try:
                manifest = os.path.join(os.getcwd(), "build-manifest.json")
                with open(manifest, 'r') as infile:
                    data = json.load(infile)

                for chunk, files in data.items():
                    if "css" in files.keys():
                        for css in files["css"]:
                            print("Adding {} to css...".format(css))
                            app.add_css_file(css)
                    if "js" in files.keys():
                        for js in files["js"]:
                            print("Adding {} to js...".format(js))
                            app.add_js_file(js)
            except FileNotFoundError as e:
                print("Warning: build-manifest.json not available")

                if not os.getenv('SPHINX_LOCAL_BUILD'):
                    raise e
    elif 'epub' in app.outdir:
        if config.has_option('', 'cover_page'):
            pdf_cover_page = get_file_from_conf_ini(config['DEFAULT']['cover_page'])
            png_cover_page = app.outdir + "/" + '_static/cover.jpeg'

            pages = convert_from_path(pdf_path=pdf_cover_page,
                                      dpi=72,
                                      size=(2560, None))

            for page in pages:
                page.save(png_cover_page, 'JPEG')
