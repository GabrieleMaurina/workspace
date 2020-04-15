# Derts
### Dependency Regression Test Selection
##### A tool to perform Regression Test Selection

Derts saves time when testing code!

Given a codebase that has changed, this tool selects which tests are safe to execute. Only tests that involve changed code are selected. Tests that operate over untouched code shouldn't be run, so Derts doesn't select them. Therefore it saves a lot of time when doing regression testing over large projects or with large test suites.

Derts works well with many languages and it is based upon [Pfff](https://github.com/returntocorp/pfff "Pfff github page"), a tool for static analysis.

Run `python -m derts -h` for help.

### Install
[Python](https://www.python.org/ "Python website") >= 3.8 is required.

**Note:** this guide assumes that your python 3 installation is under the keyword `python`, however for most linux distribution it is under `python3`. If this is the case for you, just use `python3`instead of `python`.

The installation is done through python's package manager **pip**. Simply run:

`python -m pip install derts`

### Usage

Derts can be used as a stand alone module, or trough its API. The basic usage is:

`python -m derts [-h] [-v] [-l <lang profile>] [-p <project folder>] [-t <test folder>] [-s <source folder>] [-o <output>]`

Optional arguments:
*  -h, &nbsp;&nbsp; --help &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; show help message and exit
*  -v, &nbsp;&nbsp; --verbose &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; increase output verbosity
*  -l &nbsp;&nbsp;&nbsp; \<lang profile\> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; set language profile (default "all")
*  -p &nbsp;&nbsp; \<project folder\> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; set project folder (default "current working directory")
*  -t &nbsp;&nbsp;&nbsp; \<test folder\> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; set test folder relative to \<project folder\> (default same as \<project folder\>)
*  -s &nbsp;&nbsp; \<source folder\> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; set source folder relative to \<project folder\> (default same as \<project folder\>)
*  -o &nbsp;&nbsp;&nbsp; \<output\> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; set output file (default no output, set to "stdout" for console output)

### Workflow

The suggested workflow for using Derts that will save time during testing

<img src="https://raw.githubusercontent.com/GabrieleMaurina/derts/master/workflow.png" alt="Workflow" width="500">

### Output

When run, this tool generates, inside the project folder, a new folder named `.derts`, which contains 4 files:
* **selected.json** contains a json array with the paths to all the selected test files. This file should be used to instruct the testing utility on performing regression testing
* **hash.json** contains a json object with all the sha1 of all the source files in the codebase
* **dependencies.json** contains a json object with all the file dependencies in the codebase
* **changed.json** contains a json array with all the changed classes since the previous Derts run

### API

Derts API can be used by another script. Simply import `derts` to access its functions. Its main API is:
* `main()`, to run the whole module as if it was called in the stand alone option.
* `run(language, project_folder, test_folder, source_folder, verbose, output)`, to run Derts passing your own arguments
* `rts(language, project_folder, test_folder, source_folder)`, to run just the rts part

Example: runninf Derts from another script.

```python
#import derts module
>>> import derts

#run derts with language='java', project_folder='java-design-patterns/adapter/', test_folder='src/test', source_folder='src/main', verbose=False
>>> selected, dependencies, changed, new_hashes, test_files, source_files = derts.rts('java', 'java-design-patterns/adapter/', 'src/test', 'src/main')
```

### Languages

Derts supports many languages out of the box, including:
* C
* C++
* C#
* Erlang
* Java
* Javascript
* Php
* Python
* Rust
* Scala
* Swing

However many more languages are available. Read [Dext Language Profiles](https://github.com/GabrieleMaurina/dext/blob/master/README.md#language-profiles "Dext Language Profiles github page") for more info.

### How it works

Derts uses hashes to determine which files in a codebase have changed and then selects only tests that involve those files, thus saving a lot of time when running the test suite. The steps performed by Derts are:
* hash all source files in a codebase
* compare new hashes with the older ones
* mark any file with different hash as "changed"
* mark any new file as "changed"
* compute graph of dependencies
* select any test marked "changed"
* select any test with at least one dependency marked "changed"
* output selected tests
* store hashes for next run

### Advantages

The advantages of using Derts are:
* it works with many languages
* it's lightweight (just a few scripts)
* it's lightning fast to run (faster than other RTS tools)
* it saves a lot of time when used on large projects with large test suites
* it doesn't require anything beside the code itself (other tools need things like the history of faults, class diagrams, integration with versioning tool...)
* it's customizable
