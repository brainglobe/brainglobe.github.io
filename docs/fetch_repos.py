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
# Format: (repository_url, local_download_path, branch, optional_dependencies)
# Use empty string for no optional dependencies.
REPOS = [
    ("https://github.com/brainglobe/brainglobe-atlasapi.git", "downloads/brainglobe-atlasapi", "main", "[atlasgen]"),
    # Add more (url, path, branch, optional) pairs as needed
]

print(f"Found {len(REPOS)} repositories to process.")

for url, path, branch, optional_deps in REPOS:
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
    subprocess.run(["pip", "install", "-e", f"{path}{optional_deps}"], check=True)
    print(f"Successfully installed {path}.")

print("All repositories fetched and installed successfully.")
