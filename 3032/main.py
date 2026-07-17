"""dfewf"""
def main():
    """kkk"""
    highest_score = 0
    amount = 0
    amountBunny = int(input())
    for _ in range(amountBunny):
        s = int(input())
        if s > highest_score:
            amount = 1
            highest_score = s
        elif s == highest_score:
            amount += 1
    print(highest_score)
    print(amount)
main()