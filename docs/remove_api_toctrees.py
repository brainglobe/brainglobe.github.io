"""Remove API Reference toctree sections from each tool's index.md in the documentation directory."""

import os
from pathlib import Path
import re

script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

# Paths to the documentation directory
doc_dir = Path("source/documentation")

# Regex pattern to match the API Reference toctree section
pattern = re.compile(
    r"\n\n## API Reference\n\n```{toctree}\n:maxdepth: 1\n\.\./\.\./api/.+\n```\n",
    re.MULTILINE,
)

for tool_dir in doc_dir.iterdir():
    index_md = tool_dir / "index.md"
    if index_md.exists():
        index_content = index_md.read_text(encoding="utf-8")
        new_content, n = pattern.subn("", index_content)
        if n > 0:
            index_md.write_text(new_content, encoding="utf-8")
            print(f"Removed API Reference toctree section from {index_md}")
        else:
            print(f"No API Reference toctree section found in {index_md}")
    else:
        print(f"{index_md} does not exist, skipping.")

print("API Reference toctree sections removed successfully.")