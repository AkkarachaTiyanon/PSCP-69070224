"""ss"""
def main():
    """sdkjfe"""
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())

    x2 = int(input())
    y2 = int(input())
    r2 = int(input())

    distance = ((x1-x2)**2) + ((y1-y2)**2)
    raq = (r1 + r2) ** 2

    if distance <= raq:
        print("overlapping")
    else:
        print("no overlapping")
main()
