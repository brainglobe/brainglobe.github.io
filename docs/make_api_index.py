"""Generate the API index page for every ``brainglobe`` package."""

import os
from pathlib import Path

def path_to_module_name(py_file: Path, package_dir: Path, package_name: str) -> str:
    rel_path = py_file.relative_to(package_dir)
    module_name = ".".join(rel_path.with_suffix('').parts)
    return f"{module_name}" if module_name else package_name

def generate_api_index():
    template_path = Path(__file__).resolve().parent / "source" / "_templates" / "api_template.rst"
    downloads_dir = Path(__file__).resolve().parent.parent / "downloads"
    api_dir = Path(__file__).resolve().parent / "source" / "api"
    api_dir.mkdir(parents=True, exist_ok=True)

    for package_dir in downloads_dir.iterdir():
        if package_dir.is_dir():
            package_name = package_dir.name.replace("-", "_")
            # Find all modules in the package
            module_names = []
            for py_file in package_dir.rglob("*.py"):
                if py_file.name == "__init__.py":
                    continue
                module_names.append(path_to_module_name(py_file, package_dir, package_name))
            doctree = "\n    ".join(module_names)

            # Read the template file
            with open(template_path, 'r') as template_file:
                template_content = template_file.read()
            
            # Write the API index file
            api_file_path = api_dir / f"{package_name}.rst"
            with open(api_file_path, 'w') as api_file:
                api_file.write(template_content)
                api_file.write(doctree)

            


if __name__ == "__main__":
    generate_api_index()
    print("API index files generated successfully.")