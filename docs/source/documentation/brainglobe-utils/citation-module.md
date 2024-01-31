# Generating Citations for BrainGlobe tools

If you have `brainglobe-utils` installed, you can use the `cite-brainglobe` command-line tool it provides to generate citations or acknowledgement sentences.
`brainglobe-utils` comes with the one-line BrainGlobe install, but will also be fetched by most of our tools if you decide to install them as standalone.
You can check whether or not you have the `cite-brainglobe` program available by running

```bash
cite-brainglobe --help
```

in a terminal in your BrainGlobe environment.
If `cite-brainglobe` is installed, you should see the help and information about it printed to your terminal.
If you get a "no such file or directory" or "no program found" message back, it means that you don't have `cite-brainglobe` installed - you might need to update your BrainGlobe installation, or activate your BrainGlobe environment.

## Using the tool

You can tell `cite-brainglobe` which BrainGlobe tools you are using, and it will return to you a citation for each of those tools that you can copy into your work.
You don't need to use the exact tool name either, though `cite-brainglobe` is not perfect so it helps if you can be as close to the name as possible!
Case-sensitivity is ignored, but you will have to use quotation marks if you refer to a tool that has a space in its name.

For example, if you want to cite BrainGlobe's AtlasAPI tool;

```bash
$ cite-brainglobe "brainglobe atlasapi"
@article{bg-atlasapi,
    authors = "Federico Claudi and Luigi Petrucco and Adam Tyson and Tiago Branco and Troy Margrie and Ruben Portugues",
    title = "BrainGlobe Atlas API: a common interface for neuroanatomical atlases",
    journal = "Journal of Open Source Software",
    year = "2020",
    volume = "5",
    month = "10",
    doi = "10.21105/joss.02668",
}
```

You can also ask for citations for multiple tools at once, and leave out the "brainglobe" prefix for most tools.
Asking for a citation for "brainglobe" will give you a citation that points to the BrainGlobe project webpage.
The following command for example, asks for a citation for `atlasapi` (which is interpreted as "BrainGlobe AtlasAPI"), and for `brainglobe` - the BrainGlobe tool suite:

```bash
$ cite-brainglobe atlasapi brainglobe
@article{bg-atlasapi,
    authors = "Federico Claudi and Luigi Petrucco and Adam Tyson and Tiago Branco and Troy Margrie and Ruben Portugues",
    title = "BrainGlobe Atlas API: a common interface for neuroanatomical atlases",
    journal = "Journal of Open Source Software",
    year = "2020",
    volume = "5",
    month = "10",
    doi = "10.21105/joss.02668",
}

@software{brainglobe-meta,
    authors = "BrainGlobe Developers and Wiliam Michael Graham",
    title = "BrainGlobe",
    url = "https://brainglobe.info/",
    year = "2024",
    abstract = "The BrainGlobe Initiative exists to facilitate the development of interoperable Python-based tools for computational neuroanatomy.",
    license = "BSD-3-Clause",
}
```

By default, citations are printed to the terminal screen (`stdout`), which you can then copy where you need.
The default output format for citations is `bibtex`.
These can be changed by providing the appropriate flags as detailed in the [usage pattern](#usage-pattern).

### Usage Pattern

`cite-brainglobe`'s usage pattern is available by passing the `-h` or `--help` flags:

```bash
$ cite-brainglobe --help
usage: cite-brainglobe [-h] [-l] [-s] [-w] [-o OUTPUT_FILE] [-f FORMAT] [tools ...]

Citation generation for BrainGlobe tools.

positional arguments:
  tools                 BrainGlobe tools to be cited.

options:
  -h, --help            show this help message and exit
  -l, --list            List citable BrainGlobe tools, and formats, then exit.
  -s, --software-citations
                        Explicitly cite software source code over academic papers.
  -w, --warn-unused     Print out when citation information is omitted by the chosen citation
                        format.
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Output file to write citations to.
  -f FORMAT, --format FORMAT
                        Citation format to write. Will be overwritten by the inferred format if
                        the output file argument is also provided. Valid formats can be listed
                        with the -l, --list option.
```

The `-l` (`--list`) option will provide you with a list of citation formats that the tool supports, and the list of tools that the program is aware of.
Currently supported citation formats are:

- Bibtex (`*.tex`), use `--format bibtex` to request this citation type.
- Text (`*.txt`), use `--format text` to request this citation type. This option is mainly for when you want to generate a citation you can copy/paste into a bibliography, or an acknowledgements section.

The `-s` (`--software-citations`) option will prioritise citing BrainGlobe tool _software_ - that is, the source code or program - rather than the article or journal entry that provides the theoretical basis for the tool or algorithm.
By default we expect users to prefer citing the article, however if you specifically want to credit the software or tool implementation - in cases where you have made a contribution to the source code for example - you can use this option.
Keep in mind that this option is set for _all_ tools that you ask to be cited.
If you want to cite some tools by software, and others by article, you will need to run `cite-brainglobe` twice - once with the `-s` flag and once without.

Some citation formats do no make use of all the metadata that we make available.
If you want to be aware of cases where metadata has not been used, you can pass the `-w` or `--warn-unused` flag.
This flag primarily exists for developers when debugging the tool.

You can redirect the citation output to a file of your choice by providing the `-o` (`--output-file`) option, followed by a valid file path.
The file will be overwritten if it exists already, or created if it does not exist.
If you do not provide a format via the `-f` flag, `cite-brainglobe` will attempt to infer the citation format you want from your output files extension.
In the event this is impossible, the tool with report a failure.

The `-f` or `--format` option can be used to toggle the format of the citation that is produced, so long as it is one of the supported format types given by the `--list` option.
For example,

```bash
cite-brainglobe -f txt
```

will write text (human-readable) citations as opposed to the default bibtex style.
The `-f` flag will be ignored if you provide an output file _with a supported extension_ via the `-o` option.
