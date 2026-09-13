"""ahhl"""

def pp(side,size):
    """w"""
    if side == "R":
        for i in range(size):
            txt = size - i
            space = i * 2
            print(" "*space+"*"*txt)
        for i in range(size-2,-1,-1):
            txt = abs(size - i)
            space = i * 2
            print(" "*space+"*"*txt)
    elif side == "L":
        for i in range(size,1,-1):
            space = i - 1
            txt = i
            print(" "*space+"*"*txt)
        for i in range(1,size+1):
            space = abs(i - 1)
            txt = i
            print(" "*space+"*"*txt)


def main():
    """x"""
    nun = input().upper()
    length = int(input())
    for idx, v in enumerate(nun):
        pp(v, length)
        if idx < len(nun) - 1:
            print()
main()
