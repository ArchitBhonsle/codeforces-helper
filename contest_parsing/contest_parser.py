import contest

def contestParser(contestURL: str) -> contest.Contest:
    return contest.Contest(contestURL)

if __name__ == "__main__":
    print(contestParser("https://codeforces.com/contest/1295"))