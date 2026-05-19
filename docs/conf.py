"""Sphinx configuration for builds that use ``docs/`` as the source root.

The primary configuration lives in ``docs/source/conf.py`` because the site
content is organized under ``source/``. Some build tooling invokes Sphinx with
``docs/`` as the configuration directory, so this shim loads the existing
configuration and rewrites the path-sensitive settings to match that layout.
"""

from __future__ import annotations

import importlib.util
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SOURCE_DIR = os.path.join(BASE_DIR, "source")
SOURCE_CONF_PATH = os.path.join(SOURCE_DIR, "conf.py")


def _load_source_config() -> object:
    spec = importlib.util.spec_from_file_location(
        "brainglobe_source_conf",
        SOURCE_CONF_PATH,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load Sphinx config from {SOURCE_CONF_PATH}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_source_conf = _load_source_config()

for _name in dir(_source_conf):
    if not _name.startswith("_"):
        globals()[_name] = getattr(_source_conf, _name)


master_doc = "source/index"
templates_path = [os.path.join("source", "_templates")]
html_static_path = [os.path.join("source", "_static")]
html_extra_path = [os.path.join("source", "_redirects")]
html_favicon = os.path.join("source", "_static", "brainglobe.png")

html_theme_options = dict(getattr(_source_conf, "html_theme_options", {}))
if "logo" in html_theme_options:
    html_theme_options["logo"] = dict(html_theme_options["logo"])
    html_theme_options["logo"]["image_light"] = os.path.join(
        "source",
        "_static",
        "brainglobe.png",
    )
    html_theme_options["logo"]["image_dark"] = os.path.join(
        "source",
        "_static",
        "brainglobe.png",
    )

exclude_patterns = list(getattr(_source_conf, "exclude_patterns", []))
exclude_patterns.extend(
    [
        "source/**.ipynb_checkpoints",
        "source/**/includes/**",
        "source/documentation/brainglobe-atlasapi/_atlas_table.md",
        "source/**_examples_source",
    ]
)

sphinx_gallery_conf = dict(getattr(_source_conf, "sphinx_gallery_conf", {}))
sphinx_gallery_conf["examples_dirs"] = [
    os.path.join("source", "api_examples_source"),
    os.path.join("source", "aws_examples_source"),
]
sphinx_gallery_conf["gallery_dirs"] = [
    os.path.join("source", "api_examples"),
    os.path.join("source", "aws_examples"),
]
