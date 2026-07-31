"""s"""
def main():
    """d"""
    t = int(input())
    tai = input().lower()

    c = t
    if tai == "f":
        c = (t-32)*(5/9)

    if c <= 0:
        print("solid")
    elif 0 < c < 100:
        print("liquid")
    elif c >= 100:
        print("gas")
main()
