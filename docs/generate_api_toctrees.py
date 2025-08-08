"""Generate API reference toctree sections from each tool's index.md in the documentation directory."""

import os
from pathlib import Path

script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

# Path to the documentation directory
doc_dir = Path("source/documentation")

# For each api.rst file, find the corresponding documentation subdir and update its index.md
for api_file in doc_dir.glob("*/api.rst"):
    tool_doc_dir = api_file.parent

    # Update the subdirectory's index.md to include the API Reference toctree with heading
    index_md = tool_doc_dir / "index.md"
    if index_md.exists():
        index_content = index_md.read_text(encoding="utf-8")
        api_section = (
            "\n\n## API Reference\n\n"
            "```{toctree}\n"
            ":maxdepth: 1\n"
            "api\n"
            "```\n"
        )
        if "## API Reference" not in index_content:
            # Add the API Reference toctree section at the end
            index_content += api_section
            index_md.write_text(index_content, encoding="utf-8")
            print(f"Updated {index_md} with API Reference toctree section.")
        else:
            print(f"{index_md} already contains API Reference toctree section.")
    else:
        print(f"{index_md} does not exist, skipping update.")

print("API Reference toctree sections added successfully.")