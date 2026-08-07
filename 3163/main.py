"""z"""
def main():
    """s"""
    sumk = 0
    even = 0
    odd = 0
    for _ in range(int(input())):
        x = int(input())
        sumk += x
        if x % 2:
            even += 1
        else:
            odd += 1
    print("SUM",sumk)
    print("EVEN",odd)
    print("ODD",even)
main()
