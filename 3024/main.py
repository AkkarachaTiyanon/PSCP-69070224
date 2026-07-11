"""c"""
def main():
    """ll"""
    overallscore = float(input())
    maxscore = float(input())

    lowestscore = max(0,overallscore - (2*maxscore))

    if (maxscore - lowestscore) > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
