# codeforeces-helper
This was written to work on UNIX based platforms. If you want to add windows support please feel free to fork it.
## How it works
```
codeforces-helper https://codeforces.com/contest/1323
```
This will create a directory named 1323 under a directory defined during setup with the following structure.
```
1323
├── A
│   ├── 0.exp
│   ├── 0.inp
│   ├── 0.out
│   ├── diff.sh
│   ├── run.sh
│   └── sol.cpp
... < similar for prolems from B to E >
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
`run.sh` in each of the problem directories runs your `sol.cpp` against each of the inputs and redirects to corresponding output files.
`diff.sh` compares your output files against the expected output files.
## How to get it working
First, clone the repo wherever you like.
```
git clone https://github.com/ArchitBhonsle/codeforces-helper
```
Then you need to set up a virtual environment. I recommend using pipenv.
```
pip install --user pipenv
cd <wherever you have cloned the repo>
pipenv shell
pipenv install --ignore-pipfile
```
This will get all the dependencies set up.

However to make this script work you need to setup three environment variables.
To do that add the following to your `.bashrc`
```
export CFHDIR="path to where you've clone the repo"
export CFHVENV="path to the virtual environment"
export DIRFORCES="path to a directory under which you want all the codeforces contest directories to go"
```
The entire script is called from a bash script `codeforces-helper`. You need to make it executable.
```
chmod +x codeforces-helper 
```
To make this `codeforces-helper` script executable from anywhere you need to copy the script to `/usr/local/bin`.  Be sure that this copy is also executable.  Although I do not plan to change this script anytime soon. It might be annoying to copy it again after when a change does occur. Alternatively just add the script to `PATH`.

Voila! The setup is now complete! Just run the below command to confirm.
```
codeforces-helper <URL to the contest>
```