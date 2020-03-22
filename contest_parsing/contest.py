import requests
from bs4 import BeautifulSoup

from contest_parsing import problem


class Contest:
    """
        * A Contest object with contestURL, name and problems attributes
    """

    def __init__(self, contestURL: str):
        self.contestURL = contestURL
        self.contestName, self.problems = self.getProblems()

    def getProblems(self) -> tuple:
        """
            * Returns the name and a list of Problem objects associated with the Contest
        """

        # Scraping the page
        contestPage = requests.get(self.contestURL)
        parsedContestPage = BeautifulSoup(contestPage.content, "html.parser")

        # Getting the problems(Table -> Div -> List)
        contestName = parsedContestPage.find_all(
            class_="rtable")[0].tbody.tr.th.a.contents[0]

        # TODO Check for multiple "problems" divs
        problemsTable = parsedContestPage.find_all(class_="problems")[0]
        problemDivs = problemsTable.find_all(class_="id")
        problemsList = [(p.a.contents[0].strip(
        ), "https://codeforces.com" + p.a["href"]) for p in problemDivs]

        # Extracting the problemTag and problemURL
        return contestName, [problem.Problem(problemTag, problemURL)
                             for problemTag, problemURL in problemsList]

    def getId(self) -> str:
        """
            * Gets the Codeforces unique ID for the contest.
            * Assumes contestURL is of the format "https://codeforces.com/contest/<codeforces_id>/"
        """
        if self.contestURL[-1] == "/":
            return self.contestURL[31:-1]
        else:
            return self.contestURL[31:]

    def __str__(self) -> str:
        build = []

        build.append(f"## Contest: {self.contestName}")
        build.append(f"Link: {self.contestURL}")
        for problem in self.problems:
            build.append(str(problem))

        return "\n".join(build)
