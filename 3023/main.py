"""z"""
def main():
    """tim"""
    n = int(input())
    total = 0
    if n == 1:
        total = 1
    else:
        for i in range(1,n + 1):
            total += len(str(i))
        total += n
    print(total)

main()
