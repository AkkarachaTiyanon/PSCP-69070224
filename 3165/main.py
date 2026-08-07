"""s"""
def main():
    """k"""
    step = input().lower()
    x = 0
    y = 0
    for L in step:
        if L == "n":
            y += 1
        elif L == "s":
            y -= 1
        elif L == "e":
            x += 1
        elif L == "w":
            x -= 1
    d = abs(x) + abs(y)
    print(x,y,d)
main()
