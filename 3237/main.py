"""Ss"""
def main():
    """ss"""
    n = int(input())
    for i in range(n):
        o = ""
        if i + 1 == n:
            o = o + "0" * n
        else:
            o = o + "0"
            if i - 1 > 0:
                for x in range(i-1):
                    if x != i-1:
                        o = o + "1"
                    else:
                        o = o + "0"
        if i and i+1 != n:
            o = o + "0"
        print(o)
main()
