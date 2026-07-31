"""x"""

specialchar = ["a","e","i","o","u"]
def main():
    """s"""
    gogowa = 0
    for _ in range(int(input())):
        c = input().lower()[0]
        if c in specialchar:
            gogowa += 1
    print(gogowa)
main()
