"""zz"""
def main():
    """ss"""
    x = int(input())
    y = int(input())
    quadrant = "Q"
    if x < 0 < y:
        quadrant = "Q2"
    elif x > 0 and y > 0:
        quadrant = "Q1"
    elif x < 0 and y < 0:
        quadrant = "Q3"
    elif x > 0 > y:
        quadrant = "Q4"
    elif x and not y:
        quadrant = "X"
    elif not x and y:
        quadrant = "Y"
    elif not x and not y:
        quadrant = "O"
    print(quadrant)
main()
