from contest_parsing import contest, problem, testcase
import os
import sys

templatesPath = os.path.join(os.environ["CFHDIR"], "templates")
runScriptSourceContent = ""
diffScriptSourceContent = ""
cleanScriptSourceContent = ""
solutionTemplateSourceContent = ""

runScriptSourcePath = os.path.join(templatesPath, "run.sh")
with open(runScriptSourcePath, "r") as runScriptSource:
    runScriptSourceContent = runScriptSource.read()

diffScriptSourcePath = os.path.join(templatesPath, "diff.sh")
with open(diffScriptSourcePath, "r") as diffScriptSource:
    diffScriptSourceContent = diffScriptSource.read()

cleanScriptSourcePath = os.path.join(templatesPath, "clean.sh")
with open(cleanScriptSourcePath, "r") as cleanScriptSource:
    cleanScriptSourceContent = cleanScriptSource.read()

solutionTemplateSourcePath = os.path.join(templatesPath, "sol.cpp")
with open(solutionTemplateSourcePath, "r") as solutionTemplateSource:
    solutionTemplateSourceContent = solutionTemplateSource.read()


def createContestFolder(mainPath, currentContest: contest):
    """
        * Creates the Contest folder and invokes createProblemFolder for each Problem.
    """

    # Creating the Contest Folder
    currentContestPath = os.path.join(mainPath, currentContest.getId())
    os.mkdir(currentContestPath)

    # Invoking createProblemFolder for all the Contest's Problems
    for problem in currentContest.problems:
        createProblemFolder(currentContestPath, problem)

    # Copies contents of the clean.sh file in templates to clean.sh in the Contest directory
    cleanScriptPath = os.path.join(currentContestPath, "clean.sh")
    with open(cleanScriptPath, "w") as cleanScript:
        cleanScript.write(cleanScriptSourceContent)
    os.chmod(cleanScriptPath, 0o775)

    print(str(currentContest))


def createProblemFolder(currentContestPath: str, currentProblem: problem):
    """
        * Creates the problem folder and invokes createTestcaseFiles for each Testcase.
        * Also adds a run.sh and diff.sh to each problem directory
    """

    # Creating the Problem folder
    currentProblemPath = os.path.join(
        currentContestPath, currentProblem.problemTag)
    os.mkdir(currentProblemPath)

    # Invoking createTestcaseFiles for all the Problem's Testcases
    for testcaseIndex, currentTestcase in enumerate(currentProblem.testcases):
        createTestcaseFiles(currentProblemPath, testcaseIndex, currentTestcase)

    # Copies contents of the run.sh file in templates to run.sh in the problem directory
    runScriptPath = os.path.join(currentProblemPath, "run.sh")
    with open(runScriptPath, "w") as runScript:
        runScript.write(runScriptSourceContent)
    os.chmod(runScriptPath, 0o775)

    # Copies contents of the diff.sh file in templates to diff.sh in the problem directory
    diffScriptPath = os.path.join(currentProblemPath, "diff.sh")
    with open(diffScriptPath, "w") as diffScript:
        diffScript.write(diffScriptSourceContent)
    os.chmod(diffScriptPath, 0o775)

    # Copies contents of the sol.cpp file in templates to sol.cpp in the problem directory
    solutionTemplatePath = os.path.join(currentProblemPath, "sol.cpp")
    with open(solutionTemplatePath, "w") as solutionTemplate:
        solutionTemplate.write(solutionTemplateSourceContent)


def createTestcaseFiles(currentProblemPath: str, testcaseIndex: int, currentTestCase: testcase):
    """
        * Creating .inp, .exp and .out for each Testcase
    """

    # Creating Input file
    currentTestcaseInpPath = os.path.join(
        currentProblemPath, f"{testcaseIndex}.inp")
    with open(currentTestcaseInpPath, "w") as testcaseFileIn:
        testcaseFileIn.write(currentTestCase.inp)

    # Creating Expected_Output file
    currentTestcaseExpPath = os.path.join(
        currentProblemPath, f"{testcaseIndex}.exp")
    with open(currentTestcaseExpPath, "w") as testcaseFileExp:
        testcaseFileExp.write(currentTestCase.out)

    # Creating (empty) Output file
    currentTestcaseOutPath = os.path.join(
        currentProblemPath, f"{testcaseIndex}.out")
    with open(currentTestcaseOutPath, "w") as testcaseFileOut:
        pass


mainPath = os.environ['DIRFORCES']
currentContest = contest.Contest(sys.argv[1])
createContestFolder(mainPath, currentContest)
