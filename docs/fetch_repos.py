# This script fetches external repositories for the Brainglobe project.
# It checks if the repositories already exist in the specified paths,
# and if not, it clones them from their respective GitHub URLs.
# If they do exist, it pulls the latest changes from the remote repository.

import os
import subprocess

REPOS = [
    ("https://github.com/brainglobe/brainglobe-atlasapi.git", "downloads/brainglobe-atlasapi", "main"),
    ("https://github.com/brainglobe/brainglobe-space.git", "downloads/brainglobe-space", "main"),
    ("https://github.com/brainglobe/brainglobe-utils.git", "downloads/brainglobe-utils", "main"),
    ("https://github.com/brainglobe/brainreg.git", "downloads/brainreg", "main"),
    ("https://github.com/brainglobe/brainglobe-segmentation.git", "downloads/brainglobe-segmentation", "main"),
    ("https://github.com/brainglobe/brainglobe-workflows.git", "downloads/brainglobe-workflows", "main"),
    ("https://github.com/brainglobe/brainrender.git", "downloads/brainrender", "main"),
    ("https://github.com/brainglobe/brainglobe-heatmap.git", "downloads/brainglobe-heatmap", "main"),
    ("https://github.com/brainglobe/cellfinder.git", "downloads/cellfinder", "main"),
    ("https://github.com/brainglobe/morphapi.git", "downloads/morphapi", "main"),
    # Add more (url, path, branch) pairs as needed
]

for url, path, branch in REPOS:
    if not os.path.exists(path):
        subprocess.run(["git", "clone", "--branch", branch, url, path], check=True)
    else:
        subprocess.run(["git", "-C", path, "fetch"], check=True)
        subprocess.run(["git", "-C", path, "checkout", branch], check=True)
        subprocess.run(["git", "-C", path, "pull", "origin", branch], check=True)
        
    subprocess.run(["pip", "install", "-e", path])