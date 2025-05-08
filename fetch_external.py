# This script fetches external repositories for the Brainglobe project.
# It checks if the repositories already exist in the specified paths,
# and if not, it clones them from their respective GitHub URLs.
# If they do exist, it pulls the latest changes from the remote repository.

import os
import subprocess

REPOS = [
    ("https://github.com/brainglobe/brainglobe-atlasapi.git", "external/brainglobe-atlasapi"),
    # ("https://github.com/brainglobe/brainglobe-space.git", "external/brainglobe-space"),
    # ("https://github.com/brainglobe/brainglobe-utils.git", "external/brainglobe-utils"),
    # ("https://github.com/brainglobe/brainreg.git", "external/brainreg"),
    # ("https://github.com/brainglobe/cellfinder.git", "external/cellfinder"),
    # Add more (url, path) pairs as needed
]

for url, path in REPOS:
    if not os.path.exists(path):
        subprocess.run(["git", "clone", url, path])
    else:
        subprocess.run(["git", "-C", path, "pull"])
        
    subprocess.run(["pip", "install", "-e", path])