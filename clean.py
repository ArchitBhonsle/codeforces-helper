import os
import shutil
import sys

contestDirectory = sys.argv[1]
problemDirectories = [f.path for f in os.scandir(
    contestDirectory) if f.is_dir()]


for problemDirectory in problemDirectories:
    # Moving all the solution files out into the main Contest Directory
    os.rename(os.path.join(problemDirectory, "sol.cpp"), os.path.join(
        contestDirectory, problemDirectory[-1]+".cpp"))
    # Deleting all the Problem directories
    shutil.rmtree(problemDirectory)


# Deleting the clean.sh script
os.remove(os.path.join(contestDirectory, "clean.sh"))
