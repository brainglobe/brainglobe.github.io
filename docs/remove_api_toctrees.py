"""Remove API toctrees, api.rst files, and generated api/ directories."""

import os
import shutil
from pathlib import Path
import re

script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

# Path to the documentation directory
doc_dir = Path("source/documentation")

# Flag to track if any files were removed
removed_any = False

if doc_dir.exists():
    # Iterate over all tool directories in the documentation directory
    for tool_dir in doc_dir.iterdir():
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

            # Delete the api.rst file
            api_rst_file = tool_dir / "api.rst"
            if api_rst_file.exists():
                api_rst_file.unlink()
                print(f"Removed file: {api_rst_file}")
                removed_any = True

            # Delete the generated api/ directory
            generated_api_dir = tool_dir / "api"
            if generated_api_dir.is_dir():
                shutil.rmtree(generated_api_dir)
                print(f"Removed directory: {generated_api_dir}")
                removed_any = True
            else:
                print(f"No API Reference toctree section found in {index_md}")
        else:
            print(f"{tool_dir} is not a directory, skipping.")

if removed_any:
    print("API Reference toctree sections removed successfully.")
else:
    print("No API Reference toctree sections were found or removed.")