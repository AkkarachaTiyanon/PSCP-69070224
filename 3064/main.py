"""x"""
from datetime import datetime

def main():
    """k"""
    y1 = int(input())
    m1 = int(input())
    d1 = int(input())

    y2 = int(input())
    m2 = int(input())
    d2 = int(input())

    person1_dob = datetime(y1, m1, d1)
    person2_dob = datetime(y2, m2, d2)

    day_difference = abs((person1_dob - person2_dob).days)

    if day_difference <= 7:
        print("0")
    elif person1_dob < person2_dob:
        print("1")
    else:
        print("2")
main()
