"""Remove API Reference toctree sections from each tool's index.md in the documentation directory."""

import os
from pathlib import Path
import re

script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

# Paths to the API and documentation directories
api_dir = Path("source/api")
doc_dir = Path("source/documentation")

# Get the set of tool directory names that have a corresponding API .rst file
tool_dirs = {api_file.stem.replace("_", "-") for api_file in api_dir.glob("*.rst")}

removed_any = False

for tool_dir in doc_dir.iterdir():
    if tool_dir.is_dir() and tool_dir.name in tool_dirs:
        tool_name = tool_dir.name.replace("-", "_")
        index_md = tool_dir / "index.md"
        if index_md.exists():
            index_content = index_md.read_text(encoding="utf-8")
            # Regex pattern to match the API Reference toctree section for this tool
            pattern = re.compile(
                rf"\n\n## API Reference\n\n```{{toctree}}\n:maxdepth: 1\n\.\./\.\./api/{tool_name}\n```\n",
                re.MULTILINE,
            )
            new_content, n = pattern.subn("", index_content)
            if n > 0:
                index_md.write_text(new_content, encoding="utf-8")
                print(f"Removed API Reference toctree section from {index_md}")
                removed_any = True
            else:
                print(f"No API Reference toctree section found in {index_md}")
        else:
            print(f"{index_md} does not exist, skipping.")

if removed_any:
    print("API Reference toctree sections removed successfully.")
else:
    print("No API Reference toctree sections were found or removed.")