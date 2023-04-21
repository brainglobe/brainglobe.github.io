# How to contribute to this website

## Website structure

The website is structured in three high-level sections, represented by folders in the `docs/source` directory:
- Data Analysis
- Programming
- Guides

Each section is further divided into sub-sections, each corresponding to a different markdown file in `docs/source/{section}` directory. There are also `docs/source/{section}/index.md` files, which are used to create the tables of contents for each section.

## Adding new content

To add a new sub-section, create a new markdown file in the appropriate section directory, and make sure to start it with a level-1 heading. Remember to also add the new file to the table of contents in the corresponding`docs/source/{section}/index.md` file.

To add entries to an existing sub-section, simply add new level-2/3 headings to the right markdown file, as appropriate.
  
## GitHub workflow
* Clone the GitHub repository, and create your `new_branch`.
* Edit the website and commit your changes to the `new_branch`.
* Push the `new_branch` to GitHub and create a pull request. This will automatically trigger a [GitHub Action](https://github.com/ammaraskar/sphinx-action) that checks if the website still builds correctly.
* If the checks pass, assign someone to review your changes. 
* When the reviewer merges your changes into the `main` branch, a different [GitHub Action](https://github.com/peaceiris/actions-gh-pages) will be triggered, which will build the website and publish it to the `gh-pages` branch.
* The updated website should be available at [howto.neuroinformatics.dev](https://howto.neuroinformatics.dev)

> **note**
> If you wish to view the website locally, before you push it, you can do so by running the following commands from the root of the repository.
> ```bash
> # First time only
> pip install -r docs/requirements.txt
> sphinx-build docs/source docs/build
>
> # Every time you want to build the website
> rm -rf docs/build && sphinx-build docs/source docs/build
>```
>You can view the local build at `docs/build/index.html`
