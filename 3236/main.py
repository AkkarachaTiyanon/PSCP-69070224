"""Ss"""
def main():
    """ss"""
    n = int(input())
    line1 = input()
    line2 = input()
    miss = 0
    for i in range(n):
        if int(line1[i]) + int(line2[i]) != 9:
            miss += 1
    if not miss:
        print("YES")
    else:
        print("NO",miss)
main()
