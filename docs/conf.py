#!/usr/bin/env python3
import inspect
import os

# get version from trimesh without installing
import trimesh


def abspath(rel):
    """
    Take paths relative to the current file and
    convert them to absolute paths.

    Parameters
    ------------
    rel : str
      Relative path, IE '../stuff'

    Returns
    -------------
    abspath : str
      Absolute path, IE '/home/user/stuff'
    """

    # current working directory
    cwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return os.path.abspath(os.path.join(cwd, rel))


extensions = [
    "sphinx.ext.napoleon",  # numpy-style docstring
    "myst_parser",
]  # allows markdown
myst_all_links_external = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "trimesh"
copyright = "2022, Michael Dawson-Haggerty"
author = "Michael Dawson-Haggerty"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
# The full version, including alpha/beta/rc tags.
release = trimesh.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output --------------------------------------

# The theme to use for HTML and HTML Help pages
html_theme = "furo"

# options for furo
html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_logo = "images/trimesh-logo.png"

# custom css
html_css_files = ["custom.css"]

html_context = {
    "display_github": True,
    "github_user": "mikedh",
    "github_repo": "trimesh",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

# Output file base name for HTML help builder.
htmlhelp_basename = "trimeshdoc"

autodoc_default_options = {
    "autosummary": True,
    "special-members": "__init__",
}
