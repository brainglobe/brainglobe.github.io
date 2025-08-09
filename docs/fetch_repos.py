"""
This script fetches external repositories for the Brainglobe project.

It checks if the repositories already exist in the specified paths,
and if not, it clones them from their respective GitHub URLs.
If they do exist, it pulls the latest changes from the remote repository.
"""

import os
import subprocess

print("Starting to fetch repositories...")

# This list explicitly includes repositories whose docstrings have been vetted
# for public consumption in the API documentation.
# Format: (repository_url, local_download_path, branch)
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

print(f"Found {len(REPOS)} repositories to process.")

for url, path, branch in REPOS:
    print(f"Processing repository: {url} -> {path} (branch: {branch})")
    # If the repository does not exist locally, clone it
    if not os.path.exists(path):
        print(f"Cloning into {path}...")
        subprocess.run(["git", "clone", "--branch", branch, url, path], check=True)
        print(f"Cloned {url} into {path}.")
    # If the repository already exists, fetch the latest changes
    else:
        print(f"Fetching updates for {path}...")
        subprocess.run(["git", "-C", path, "fetch"], check=True)
        subprocess.run(["git", "-C", path, "checkout", branch], check=True)
        subprocess.run(["git", "-C", path, "pull", "origin", branch], check=True)
        print(f"Updated {path} to latest {branch} branch.")

    # Install the repository in editable mode
    print(f"Installing {path} in editable mode...")
    subprocess.run(["pip", "install", "-e", path], check=True)
    print(f"Successfully installed {path}.")

print("All repositories fetched and installed successfully.")
