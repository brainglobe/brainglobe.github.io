"""Generate API reference markdown files for each tool in the documentation directory."""

import os
from pathlib import Path

script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

# Paths to the API and documentation directories
api_dir = Path("source/api")
doc_dir = Path("source/documentation")

print(f"Contents of api_dir: {list(api_dir.glob('*'))}")  # Debugging line

# For each API .rst file, find the corresponding documentation subdir and update its index.md
for api_file in api_dir.glob("*.rst"):
    tool_name = api_file.stem  # e.g., 'brainglobe_atlasapi'
    # e.g., 'brainglobe-atlasapi'
    tool_doc_dir = doc_dir / tool_name.replace("_", "-")
    api_md = tool_doc_dir / "api-reference.md"

    # Create the API Reference markdown file
    api_md_content = f"""# API Reference

```{{toctree}}
:maxdepth: 1
../../api/{tool_name}
```
"""
    api_md.write_text(api_md_content, encoding="utf-8")
    print(f"Created {api_md} with API link to {tool_name}")

print("API Reference markdown files generated successfully.")
