"""Generate the API index page for every ``brainglobe`` package."""

import os
from pathlib import Path

print("Starting to generate API index files...")

script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

def path_to_module_name(py_file: Path, package_dir: Path, package_name: str) -> str:
    rel_path = py_file.relative_to(package_dir)
    module_name = ".".join(rel_path.with_suffix('').parts)
    return f"{module_name}" if module_name else package_name

def generate_api_index():
    template_path = Path("source/_templates/api_template.rst")
    print(f"Using template: {template_path}")
    downloads_dir = Path("downloads")
    doc_dir = Path("source/documentation")

    excluded_folders = ["tests", "examples", "benchmarks", "atlas_scripts"]

    packages = [p for p in downloads_dir.iterdir() if p.is_dir()]
    print(f"Found {len(packages)} packages to process.")

    # Iterate over all packages in the downloads directory
    for package_dir in packages:
        if package_dir.is_dir():
            package_name = package_dir.name
            print(f"Generating API index for {package_name}")

            # Define the output directory for the package's API file
            api_output_dir = doc_dir / package_name

            # Find all modules in the package
            module_names = []
            for py_file in package_dir.rglob("*.py"):
                if py_file.name == "__init__.py":
                    continue
                if any(part in excluded_folders for part in py_file.parts):
                    continue
                # Convert the file path to a module name and add it to the list
                module_names.append(path_to_module_name(py_file, package_dir, package_name))
            # Join the module names into a single string
            modules_rst = "\n    ".join(module_names)

            # Read the template file
            with open(template_path, 'r') as template_file:
                template_content = template_file.read()
            
            # Replace the label with a unique one for each package
            unique_label = f"target_api_{package_name}"
            template_content = template_content.replace("package_label", unique_label)
            
            # Write the API index file
            api_file_path = api_output_dir / "api.rst"
            with open(api_file_path, 'w') as api_file:
                api_file.write(template_content + "\n\n    ")
                api_file.write(modules_rst)
            print(f"Generated API index file: {api_file_path}")

if __name__ == "__main__":
    generate_api_index()
    print("Finished generating API index files.")
