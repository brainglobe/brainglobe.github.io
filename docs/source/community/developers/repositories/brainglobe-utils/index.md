# `brainglobe-utils`

`brainglobe-utils` is a collection of functions that can be re-used across multiple repositories: for BrainGlobe tools, plugins, or analyses (in the case of `brainglobe-workflows`).
It underpins a number of our user-facing tools like `brainreg` and `cellfinder`, as well as our common interfaces to napari in `brainglobe-napari-io`, for example.
The main feature it provides to users is the [`cite-brainglobe`](#cite-brainglobe-and-the-citation-submodule) command-line program.

## `cite-brainglobe` and the `citation` submodule

The `cite-brainglobe` command-line program is provided by the `citation` submodule, with the command-line wrapper and main function themselves being available in `citation.cite:cli` and `citation.cite:cite` respectively.

At the top level, the workflow for the citation tool is as follows:

- Parse the tool names that the user provides on the command-line. The repositories known to the package, and the names that they use, are defined in the `citation.repository`.
- Fetch the citation data from each `repository` by reading its CITATION.cff file.
- Read the CITATION.cff metadata into the appropriate citation format. This creates an instance of (a subclass of) `citation.format:Format`.
- Invoke the `generate_ref_string()` method of the `Format` instance to obtain the citation string.
- Append the citation string to those already created, and repeat for each tool requested.
- Write the output text to a file, or dump to `stdout` if not provided with an output location.

The `citation` submodule itself breaks down further to accommodate the steps of the workflow above.

- As mentioned, the `citation.cite` module contains the high-level command-line interface and backend function.
- The `citation.fetch` module contains helper functions for quickly retrieving the files we want from their GitHub repositories.
- The `citation.repository` submodule contains the `Repository` class which is a convenient wrapper for storing information about the BrainGlobe tools that we want `cite-brainglobe` to be aware of, and recognise the names of.
- The `citation.format` submodule contains the `Format` base class for reading and generating citation strings.
- The additional modules that match `citation.*_fmt` contain classes that derive from `Format`. This allows us to accommodate different citation formats needing different metadata, amongst other things.

### Adding new repositories or tools

`cite-brainglobe` is only aware of the repositories that we tell it about - and any such repository must have a CITATION.cff (or equivalent metadata file) present in it that we can fetch.

To make `cite-brainglobe` aware of a new BrainGlobe tool, add a static `Repository` instance to the `citation.repositories` submodule [as detailed here](#citationrepositories), specifying the required information.

### Adding a new supported citation format

Create a new submodule called `new-format_fmt` in the `citation` submodule.
Then write a class that inherits from `citation.format.Format` and defines the `required` and `optional` keys that your citation type needs from the `.cff` files we read from GitHub.
Finally, in your class you'll need to overwrite the `generate_ref_string` method to produce the citation string from the metadata information you specified.

Then, head to the `citation.cite` module and add your new format as an option to the command-line interface (`citation.cite.cli`) and backend function (`citation.cite.cite`).

### `citation.repositories`

This module contains the `Repository` class, a function to find the repositories that are referred to in a list of tool names, and the static instances of all the BrainGlobe repositories that we provide a reference for via `cite-brainglobe`.

The `Repository` class is just a convenient container for all the information pertaining to one particular BrainGlobe tool or repository.
The class itself just holds any information we need and some useful actions on that information - like providing the URL for the GitHub repo, storing the alternative names for the tool that is held there, etc.
The static instances of this class are instantiated in this module too - by convention, the variable name should match the repository's name on GitHub.
Each instance is created using the syntax:

```python
bg_tool = Repository("bg-tool", ["list", "of", "alternative", "or", "informal", "names"])
```

This defines a repository that `cite-brainglobe` expects to be called `bg-tool`, under the `brainglobe` organisation on GitHub.
It also expects the CITATION.cff file to be on the `main` branch of this repository - though this location (and the organisation if we really need to point to non-BrainGlobe tools) can be changed when calling the constructor.
The second argument defines the (case-insensitive) names (in addition to the repository name itself) that `cite-brainglobe` will match to this repository.
For example,

```python
bg_atlasapi = Repository(
    "bg-atlasapi",
    [
        "bg_atlasapi",
        "BrainGlobe AtlasAPI",
        "BrainGlobe AtlasAPI",
        "AtlasAPI",
        "Atlas API",
    ],
)
```

means that if the user asks `cite-brainglobe` to cite "atlasapi", the program will recognise this as an alternative alias for `bg-atlasapi`.

The `all_citable_repositories` function is intended for imports in other areas of th `citation` submodule - it automatically detects the static `Repository` instances that we define in the `repositories` and returns them as a set.

The `unique_repositories_from_tools` function takes in a list of tool names or aliases (in particular, the list provided by the user on the command-line) and returns the unique repositories that need to be cited given this list.

### `citation.fetch`

This submodule contains two helper functions.
The simplest is the `yaml_str_to_dict` function which takes a string containing the yaml-formatted content of a file and parses it into a Python `dict` - this is for use when retrieving files from the internet as opposed to loading them from disk.

The `fetch_from_github` function provides a streamlined function for fetching the content of files from GitHub repositories, and validates that the request was successful.

### `citation.format` and the `citation.*_fmt` submodules

The `Format` class resides in this submodule.
This class is the intended base class for any citations that we want to generate, and provides this abstract functionality.
The various `*_fmt` submodules then provide the derived classes for each of the citation formats that we want to support - `bibtex_fmt` provides the `BibTexEntry` class, and `text_fmt` supports writing citations as human-readable strings.

The key properties of the `Format` class are the `required` and `optional` class variables - these are not set in the base class and are intended to be overwritten by classes that inherit from `Format`.
Both of these class variables should be lists of strings, corresponding to the keys in a CITATION.cff format that the citation (described by the inheriting class) needs (respectively can make use of) when being produced.
Existence of these keys in the CITATION.cff information is checked for in the `Format.__init__` class constructor to avoid repetition across submodules and catch errors.
Optional keys are allowed to be missing - these can be set to be reported if so.
The `Format` class also contains a class-wide function for parsing the `authors` key information into a string - `Format._prepare_authors_field` - which is again invoked on instantiation.
Finally, `Format` provides a placeholder `generate_ref_string` function that should be overwritten by any inheriting classes - this is the method that will parse the data read in and produce the citation string.

For example, the `TextCitation` format inherits from `Format` and requires the keys "author", "title" and "year" to produce a reference.
It also provides a list of optional keys that the format can still make use of when producing the citation, but it does not require them.
`TextCitation` itself does not need to define a constructor function since the inherited constructor from `Format` now suffices with the overwritten values for `TextCitation.required` and `TextCitation.optional`.
`TextCitation` does implement `generate_ref_string` in order to overwrite the placeholder function defined by `Format` - this will dictate how the citation string is formatted and assembled.

The `BibTexEntry` class is slightly more subtle since any given entry type in a bibtex file may require different keys present, _and_ the syntax for the author field in a bibtex reference differs from the default format implemented in the `Format._prepare_authors_field`.
As such, `BibTexEntry` overwrites both the `_prepare_authors_field` function, _and_ implements some preliminary steps in `BibTexEntry.__init__` before invoking the base constructor in `Format.__init__`.
`BibTexEntry` _does_ however implement the `generate_ref_string` method, since this is the same for all bibtex citation types.
Each bibtex citation type, such as `Software` or `Article`, then inherits from the `BibTexEntry` class and defines the `required` and `optional` fields as usual.
