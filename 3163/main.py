"""z"""
def main():
    """s"""
    sum = 0
    even = 0
    odd = 0
    for _ in range(int(input())):
        x = int(input())
        sum += x
        if x % 2:
            even += 1
        else:
            odd += 1
    print("SUM",sum)
    print("EVEN",odd)
    print("ODD",even)
main()
