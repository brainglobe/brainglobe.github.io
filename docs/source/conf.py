# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "BrainGlobe"
copyright = "2023, BrainGlobe"
author = "BrainGlobe contributors"

# The full version, including alpha/beta/rc tags
release = "0.0.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "ablog",
    "sphinx.ext.githubpages",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinx_sitemap",
    "myst_parser",
    "numpydoc",
    "nbsphinx",
    "notfound.extension",
    "sphinx_copybutton"
]

# Configure the myst parser to enable cool markdown features
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
# Automatically add anchors to markdown headings
myst_heading_anchors = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "**.ipynb_checkpoints",
    # to ensure that include files (partial pages) aren't built, exclude them
    # https://github.com/sphinx-doc/sphinx/issues/1965#issuecomment-124732907
    "**/includes/**",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_title = "BrainGlobe"

# Redirect the webpage to another URL
# Sphinx will create the appropriate CNAME file in the build directory
# https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
html_baseurl = "https://brainglobe.info/"
sitemap_url_scheme = "{link}"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    ("css/custom.css", {"priority": 100}),
]

html_favicon = "_static/brainglobe.png"

## Cutomize the theme
html_theme_options = {
    "announcement": "BrainGlobe is undergoing restructuring. Keep track of the latest developments on <a href='https://brainglobe.info/blog/version1/version_1_announcement.html'>the blog</a>",
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/brainglobe",  # required
            # Icon class (if "type": "fontawesome"),
            # or path to local image (if "type": "local")
            "icon": "fa-brands fa-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/brain_globe",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "Mastodon",
            "url": "https://mastodon.online/@brainglobe",
            "icon": "fa-brands fa-mastodon",
        },
        {
            "name": "Bluesky",
            "url": "https://bsky.app/profile/brainglobe.bsky.social",
            "icon": "fa-solid fa-square",
        },
        {
            # Label for this link
            "name": "Zulip (Developer chat)",
            # URL where the link will redirect
            "url": "https://brainglobe.zulipchat.com",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-solid fa-comments",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            # Label for this link
            "name": "image.sc (Help forum)",
            # URL where the link will redirect
            "url": "https://forum.image.sc/tag/brainglobe",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-solid fa-question",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
    ],
    "logo": {
        "text": "BrainGlobe",
        "image_light": "brainglobe.png",
        "image_dark": "brainglobe.png",
    },
    "footer_start": ["footer_start"],
    "footer_end": ["footer_end"],
    "external_links": [],
}


html_show_sourcelink = False

notfound_context = {
    "body": "<h1>This page has likely moved.</h1> <p>We have recently restructured the BrainGlobe website, and some links have broken. Try using the search box or go to the homepage. If you can'</p>",
}

notfound_context = {
    "title": "Page Not Found",
    "body": """
    <h1>Page Not Found</h1>

    <p>Sorry, we couldn't find that page.</p>

    <p>We have recently restructured the BrainGlobe website, and some links have broken. Try using the search box or go to the homepage.</p>
    <p>If you can't find the information you need. Please <a href="https://brainglobe.info/contact.html">get in touch</a>.</p>

""",
}

# needed for GH pages (vs readthedocs)
notfound_urls_prefix = None


linkcheck_ignore = ["https://neuromorpho.org/"]