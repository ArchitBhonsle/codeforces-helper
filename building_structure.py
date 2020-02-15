#!~/.local/share/virtualenvs/codeforces-helper-o_PEnNh5/bin/python
# ! Above shebang is the path to the virtualenv that has the required packages.
# ! YOURS WILL BE DIFFERENT

from contest_parsing import contest, problem, testcase
import os

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

def createProblemFolder(currentContestPath: str, currentProblem: problem):
    """
        * Creates the problem folder and invokes createTestcaseFiles for each Testcase.
        * Also adds a run.sh to each problem folder to run solution against each input
    """
    
    # Creating the Problem folder
    currentProblemPath = os.path.join(currentContestPath, currentProblem.problemTag)
    os.mkdir(currentProblemPath)
    
    # Invoking createtestcaseFiles for all the Problem's Testcases
    for testcaseIndex, currentTestcase in enumerate(currentProblem.testcases):
        createTestcaseFiles(currentProblemPath, testcaseIndex, currentTestcase)
    
    # TODO Add the run.sh part

def createTestcaseFiles(currentProblemPath: str, testcaseIndex: int, currentTestCase: testcase):
    """
        * Creating inp.txt, exp.txt and out.txt for each Testcase
    """
    
    # Creating Input file
    currentTestcaseInpPath = os.path.join(currentProblemPath, f"inp_{testcaseIndex}.txt")
    with open(currentTestcaseInpPath, "w") as testcaseFileIn:
        testcaseFileIn.write(currentTestCase.inp)
    
    # Creating Expected_Output file
    currentTestcaseExpPath = os.path.join(currentProblemPath, f"exp_{testcaseIndex}.txt")
    with open(currentTestcaseExpPath, "w") as testcaseFileExp:
        testcaseFileExp.write(currentTestCase.out)
    
    # Creating (empty) Output file
    currentTestcaseOutPath = os.path.join(currentProblemPath, f"out_{testcaseIndex}.txt")
    with open(currentTestcaseOutPath, "w") as testcaseFileOut:
        pass

if __name__ == "__main__":
    # Please excuse the ghetto testing
    mainPath = os.getcwd() 
    currentContest = contest.Contest("https://codeforces.com/contest/1301/")
    createContestFolder(mainPath, currentContest)
