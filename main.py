from contest_parsing import contest, problem, testcase
import os
import sys

templatesPath = os.path.join(os.environ["CFHDIR"], "templates")
cleanScriptSourceContent = ""
runScriptSourceContent = ""
diffScriptSourceContent = ""

cleanScriptSourcePath = os.path.join(templatesPath, "clean.sh")
with open(cleanScriptSourcePath, "r") as cleanScriptSource:
    cleanScriptSourceContent = cleanScriptSource.read()

runScriptSourcePath = os.path.join(templatesPath, "run.sh")
with open(runScriptSourcePath, "r") as runScriptSource:
    runScriptSourceContent = runScriptSource.read()

diffScriptSourcePath = os.path.join(templatesPath, "diff.sh")
with open(diffScriptSourcePath, "r") as diffScriptSource:
    diffScriptSourceContent = diffScriptSource.read()


def createContestFolder(mainPath, currentContest: contest):
    """
        * Creates the Contest folder and invokes createProblemFolder for each Problem.
        * Also adds a clean.sh to every Contest folder to make it ready for Github push.
    """

    # Creating the Contest Folder
    currentContestPath = os.path.join(mainPath, currentContest.getId())
    os.mkdir(currentContestPath)

    # Invoking createProblemFolder for all the Contest's Problems
    for problem in currentContest.problems:
        createProblemFolder(currentContestPath, problem)

    # TODO Add the clean.sh part
    cleanScriptPath = os.path.join(currentContestPath, "clean.sh")
    with open(cleanScriptPath, "w") as cleanScript:
        cleanScript.write(cleanScriptSourceContent)


def createProblemFolder(currentContestPath: str, currentProblem: problem):
    """
        * Creates the problem folder and invokes createTestcaseFiles for each Testcase.
        * Also adds a run.sh to each problem folder to run solution against each input
    """

    # Creating the Problem folder
    currentProblemPath = os.path.join(
        currentContestPath, currentProblem.problemTag)
    os.mkdir(currentProblemPath)

    # Invoking createtestcaseFiles for all the Problem's Testcases
    for testcaseIndex, currentTestcase in enumerate(currentProblem.testcases):
        createTestcaseFiles(currentProblemPath, testcaseIndex, currentTestcase)

    # TODO Add the run.sh and diff.sh part
    runScriptPath = os.path.join(currentProblemPath, "run.sh")
    with open(runScriptPath, "w") as runScript:
        runScript.write(runScriptSourceContent)

    diffScriptPath = os.path.join(currentProblemPath, "diff.sh")
    with open(diffScriptPath, "w") as diffScript:
        diffScript.write(diffScriptSourceContent)


def createTestcaseFiles(currentProblemPath: str, testcaseIndex: int, currentTestCase: testcase):
    """
        * Creating inp.txt, exp.txt and out.txt for each Testcase
    """

    # Creating Input file
    currentTestcaseInpPath = os.path.join(
        currentProblemPath, f"inp_{testcaseIndex}.txt")
    with open(currentTestcaseInpPath, "w") as testcaseFileIn:
        testcaseFileIn.write(currentTestCase.inp)

    # Creating Expected_Output file
    currentTestcaseExpPath = os.path.join(
        currentProblemPath, f"exp_{testcaseIndex}.txt")
    with open(currentTestcaseExpPath, "w") as testcaseFileExp:
        testcaseFileExp.write(currentTestCase.out)

    # Creating (empty) Output file
    currentTestcaseOutPath = os.path.join(
        currentProblemPath, f"out_{testcaseIndex}.txt")
    with open(currentTestcaseOutPath, "w") as testcaseFileOut:
        pass


mainPath = os.environ['DIRFORCES']
currentContest = contest.Contest(sys.argv[1])
createContestFolder(mainPath, currentContest)
