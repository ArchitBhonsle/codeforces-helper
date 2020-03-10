# codeforces-helper

This was written to work on UNIX based platforms. If you want to add windows support please feel free to fork it.

## How it works

```bash
codeforces-helper https://codeforces.com/contest/<contest-id>

or

cfh https://codeforces.com/contest/<contest-id>
```

This will create a directory named `<contest-id>` under a directory defined during setup with the following structure.

```text
<contest-id>
├── A
│   ├── 0.exp
│   ├── 0.inp
│   ├── 0.out
│   ├── diff.sh
│   ├── run.sh
│   └── sol.cpp
... <similar for problems from B to E>
└── F
    ├── 0.exp
    ├── 0.inp
    ├── 0.out
    ├── 1.exp
    ├── 1.inp
    ├── 1.out
    ├── 2.exp
    ├── 2.inp
    ├── 2.out
    ├── diff.sh
    ├── run.sh
    └── sol.cpp
```

* `run.sh` in each of the problem directories runs your `sol.cpp` against each of the inputs and redirects to corresponding output files.
* `diff.sh` compares your output files against the expected output files.
* `clean.sh` cleans the contest directory removing all the inp, out & exp files keeping only the solution files making the directory structure as shown below.

```text
<contest-id>
├── A.cpp
├── B.cpp
├── C.cpp
├── D.cpp
├── E.cpp
└── F.cpp
```

## How to get it working

First, clone the repo wherever you like.

```bash
git clone https://github.com/ArchitBhonsle/codeforces-helper
```

Then you need to set up a virtual environment. I recommend using pipenv.

```bash
pip install --user pipenv
cd "path/to/where/you/cloned/the/repo"
pipenv shell
pipenv install --ignore-pipfile
pipenv --venv   # Gives you the path to the virtual environment needed later
```

(The last command gives you the path to the virtual environment which you will need later)
This will get all the dependencies set up.

However to make this script work you need to setup three environment variables.
To do that add the following to your `.bashrc`

```bash
export CFHDIR="path/to/where/you/cloned/the/repo"
export CFHVENV="path/to/the/virtual/environment"
export DIRFORCES="path/to/a/directory/in/which/you/want/all/the/codeforces/contest/directories/to/go"
alias cfh="codeforces-helper"   # Optional
```

(The last line sets up an alias so you can type `cfh` instead of `codeforces-helper`)

The entire script is called from a bash script `codeforces-helper`. You need to make it executable.

```bash
chmod +x codeforces-helper
```

To make this `codeforces-helper` script executable from anywhere you need to copy the script to `/usr/local/bin`.  Be sure that this copy is also executable using the above command.

Voila! The setup is now complete! Just run the below command to confirm.

```bash
codeforces-helper https://codeforces.com/contest/<contest-id>

or

cfh https://codeforces.com/contest/<contest-id>
```
