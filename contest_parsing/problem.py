import requests
from bs4 import BeautifulSoup

from contest_parsing import testcase

class Problem:
    """
        * A Problem consisting of problemTag, problemURL and testcases attributes
    """
    
    def __init__(self, tag: str, problemURL: str):
        self.problemTag = tag
        self.problemURL = problemURL
        self.testcases = self.getTestcases()

    def getTestcases(self) -> list: 
        """
            * Returns the a list of TestCase objects associated with the Problem
        """
        
        # Scraping the Problems Page
        problemPage = requests.get(self.problemURL)
        parsedProblemPage = BeautifulSoup(problemPage.content, "html.parser")
        
        # Getting the sampleTests div
        # TODO Check for multiple "sample-test" divs
        sampleTests = parsedProblemPage.find_all(class_="sample-test")[0]
        
        # Extracting the inputs and outputs
        # TODO Check for no "input" and "output" divs
        inputs = [inp.pre.contents[0] for inp in sampleTests.find_all(class_="input")]
        outputs = [out.pre.contents[0] for out in sampleTests.find_all(class_="output")]
        
        # Creating the testcases list
        testcases = []
        for inp, out in zip(inputs, outputs):
            testcases.append(testcase.Testcase(inp.strip(), out.strip()))

        return testcases

    def __str__(self) -> str:
        build = []
        
        build.append(f"\n# Problem: {self.tag}")
        build.append(f"Link: {self.problemURL}")
        for tc in self.testcases:
            build.append("\n" + str(tc))

        return "\n".join(build)