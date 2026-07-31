"""s"""

mb = [6,8,10]
bb = [5,6,7]
gb = [4,5,6]
def main():
    """s"""
    x = input().lower().split()
    role,age,salary = x[0],int(x[1]),int(x[2])
    basebonus = 0

    cobe = 0
    if age <= 5:
        cobe = 0
    elif age <= 10:
        cobe = 1
    else:
        cobe = 2

    mult = 0
    if role == "m":
        basebonus = 1500
        mult = mb[cobe]
    elif role == "b":
        basebonus = 1000
        mult = bb[cobe]
    elif role == "g":
        basebonus = 500
        mult = gb[cobe]

    bonus = salary * (mult/100)
    final = int(basebonus + bonus)
    print(final)
main()
