# Debugging common error messages

## Error messages

Some error in `brainmapper` may come from the `cellfinder` cell detection algorithm. Please also check the 
[cellfinder error messages section](/documentation/cellfinder/troubleshooting/error-messages).

### OSError: [Errno 24] Too many open files

```bash
OSError: [Errno 24] Too many open files
```

This is likely because your default limits are set too low.
To fix this, follow the instructions [here](https://easyengine.io/tutorials/linux/increase-open-files-limit/).
If for any reason you don't want to or can't change the system-wide limits, running `ulimit -n 60000` before running `cellfinder` should work.
This setting will persist for the present shell session, but will have to be repeated if you open a new terminal.

### error: unrecognized arguments

```bash
main.py: error: unrecognized arguments: data/dataset1
```

If what comes after `urecognised arguements` looks to be the part of the filepath you entered, after a space, then you should enclose the full path in quotation marks.
For example, use `"/path/to/my data"` not `path/to/my data`.
Otherwise cellfinder will interpret the path as two inputs, separated by a space.

### CommandLineInputError: File path: cannot be found.

```bash
brainglobe_utils.general.exceptions.CommandLineInputError: File path: '/media/adam/Storage/cellfinder/data/dataset1' cannot be found.
```

If you see an error like this, there could be a few possible reasons, e.g.:

* The filepath that you've passed to cellfinder does not exist, maybe it's misspelled, or on a drive that isn't mounted?
* If the filepath that cannot be found looks to be the part of the filepath you entered, after a space, then you 
should enclose the full path in quotation marks. (**i.e. `"/path/to/my data"` not `path/to/my data`**) . Otherwise 
cellfinder will interpret the path as two inputs, separated by a space.)
