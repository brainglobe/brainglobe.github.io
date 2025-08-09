"""Remove API toctrees, api.rst files, and generated api/ directories."""

import os
import shutil
from pathlib import Path
import re

print("Starting to remove API toctrees and generated files...")

script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

# Path to the documentation directory
doc_dir = Path("source/documentation")

# Flag to track if any files were removed
removed_any = False
files_removed = 0
dirs_removed = 0
to_trees_removed = 0

if doc_dir.exists():
    tool_dirs = [d for d in doc_dir.iterdir() if d.is_dir()]
    print(f"Found {len(tool_dirs)} tool directories to check.")
    # Iterate over all tool directories in the documentation directory
    for tool_dir in tool_dirs:
        if tool_dir.is_dir():
            # Remove the toctree section from index.md
            index_md = tool_dir / "index.md"
            if index_md.exists():
                index_content = index_md.read_text(encoding="utf-8")
                # Regex pattern to find the API reference section
                pattern = re.compile(
                    r"\n\n## API Reference\n\n```{toctree}\n:maxdepth: 1\napi\n```\n",
                    re.MULTILINE
                )
                # Remove the API reference section from the content
                new_content, n = pattern.subn("", index_content)
                if n > 0:
                    index_md.write_text(new_content, encoding="utf-8")
                    print(f"Removed API toctree from: {index_md}")
                    removed_any = True
                    to_trees_removed += 1

            # Delete the api.rst file
            api_rst_file = tool_dir / "api.rst"
            if api_rst_file.exists():
                api_rst_file.unlink()
                print(f"Removed file: {api_rst_file}")
                removed_any = True
                files_removed += 1

            # Delete the generated api/ directory
            generated_api_dir = tool_dir / "api"
            if generated_api_dir.is_dir():
                shutil.rmtree(generated_api_dir)
                print(f"Removed directory: {generated_api_dir}")
                removed_any = True
                dirs_removed += 1
            else:
                print(f"No API Reference toctree section found in {index_md}")
        else:
            print(f"{tool_dir} is not a directory, skipping.")

if removed_any:
    print("\nFinished removing API toctrees and generated files.")
    print("Summary:")
    print(f"  - Toctrees removed: {to_trees_removed}")
    print(f"  - Files removed: {files_removed}")
    print(f"  - Directories removed: {dirs_removed}")
else:
    print("No API Reference toctree sections or generated files were found to remove.")
