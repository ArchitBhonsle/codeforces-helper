from contest_parsing import contest, problem, testcase
import os

def createContestFolder(mainPath, currentContest: contest) -> str:
    currentContestPath = os.path.join(mainPath, currentContest.getId())
    os.mkdir(currentContestPath)
    for problem in currentContest.problems:
        createProblemFolder(currentContestPath, problem)

def createProblemFolder(currentContestPath: str, currentProblem: problem) -> str:
    currentProblemPath = os.path.join(currentContestPath, currentProblem.getTag())
    os.mkdir(currentProblemPath)
    for index, testcase in enumerate(currentProblem.testcases):
        currentTestcaseInpPath = os.path.join(currentProblemPath, f"inp_{index}.txt")
        currentTestcaseExpPath = os.path.join(currentProblemPath, f"exp_{index}.txt")
        currentTestcaseOutPath = os.path.join(currentProblemPath, f"out_{index}.txt")
        with open(currentTestcaseInpPath, "w") as testcaseFileIn:
            testcaseFileIn.write(testcase.getInp())
        with open(currentTestcaseExpPath, "w") as testcaseFileExp:
            testcaseFileExp.write(testcase.getOut())
        with open(currentTestcaseOutPath, "w") as testcaseFileOut:
            pass

if __name__ == "__main__":
    mainPath = os.getcwd()
    currentContest = contest.Contest("https://codeforces.com/contest/1301/")
    createContestFolder(mainPath, currentContest)
