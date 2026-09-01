"""w"""

def main():
    """o"""
    n = int(input())
    score = 0
    for _ in range(n):
        if input() == "+":
            score += 10
        else:
            score -= 5
    print(score)
main()
