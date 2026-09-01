"""o"""
def main():
    """k"""
    n, k, t = map(int, input().split())
    curr = 1
    count = 1
    while True:
        if curr == t:
            print(count)
            return
        curr = (curr + k - 1) % n + 1
        if curr == 1:
            print(count)
            return
        count += 1
main()
