"""a"""
def main():
    """k"""
    small = int(input())
    big = int(input())
    goal = int(input())

    max_large_used = min(big, goal // 5)
    remaining_length = goal - (max_large_used * 5)

    if small >= remaining_length:
        print(remaining_length)
    else:
        print("-1")
main()
