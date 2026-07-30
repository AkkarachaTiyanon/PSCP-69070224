"sss"

def main():
    """ss"""
    a = input().strip()
    b = int(input().strip())

    c = "H"
    d = 4567

    e = a == c
    f = b == d

    if e and f:
        print("safe unlocked")
    elif e:
        print("safe locked - change digit")
    elif f:
        print("safe locked - change char")
    else:
        print("safe locked")
main()
