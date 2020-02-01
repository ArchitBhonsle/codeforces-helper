import requests
from bs4 import BeautifulSoup

import problem

class Contest:


    def __init__(self, contestURL: str):
        self.contestURL = contestURL
        self.name, self.problems = self.getProblems()
        
    def getProblems(self) -> tuple:
        """
            * Returns a list of Problem objects associated with the Contest
        """
        contestPage = requests.get(self.contestURL)
        parsedContestPage = BeautifulSoup(contestPage.content, "html.parser")

        name = parsedContestPage.find_all(class_="rtable")[0].tr.th.a.contents[0]
        # ! Check for multiple "problems" divs
        problemsTable = parsedContestPage.find_all(class_="problems")[0]
        problemDivs = problemsTable.find_all(class_="id")
        problemsList = [(p.a.contents[0].strip(), "https://codeforces.com" + p.a["href"]) for p in problemDivs]

        return name, [problem.Problem(tag, problemUrl) for tag, problemUrl in problemsList]

    def __str__(self) -> str:
        build = []

        build.append(f"## Contest: {self.name}")
        build.append(f"Link: {self.contestURL}")
        for problem in self.problems:
            build.append(str(problem))

        return "\n".join(build)

if __name__ == "__main__":
    ContestEDC81 = Contest("https://codeforces.com/contest/1295")
    print(ContestEDC81)