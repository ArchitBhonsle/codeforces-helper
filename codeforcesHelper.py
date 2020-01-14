import requests
from bs4 import BeautifulSoup

URL = "https://codeforces.com/contest/1285"

def resolveProblem(problemURL: str) -> tuple:
  problemPage = requests.get(problemURL)
  parsedProblemPage = BeautifulSoup(problemPage.content, "html.parser")

  # ! Check for multiple "sample-test" divs
  sampleTests = parsedProblemPage.find_all(class_="sample-test")[0]
  # ! Check for no "input" and "output" divs
  inputs = [inp.pre.contents[0] for inp in sampleTests.find_all(class_="input")]
  outputs = [out.pre.contents[0] for out in sampleTests.find_all(class_="output")]

  return zip(inputs, outputs)

def getProblems(contestURL: str) -> list:
  contestPage = requests.get(contestURL)
  parsedContestPage = BeautifulSoup(contestPage.content, "html.parser")

  # ! Check for multiple "problems" divs
  problemsTable = parsedContestPage.find_all(class_="problems")[0]
  problems = problemsTable.find_all(class_="id")
  problemURLs = ["https://codeforces.com" + problem.a["href"] for problem in problems]

  return problemURLs

def parseContest(contestURL: str):
  problemURLs = getProblems(contestURL)
  for problemURL in problemURLs:
    sampleTest = resolveProblem(problemURL)
    for inp, out in sampleTest:
      print(inp)
      print(out)    

parseContest(URL)