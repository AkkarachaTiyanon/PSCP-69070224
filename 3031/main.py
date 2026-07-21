"""d"""
import math

def main():
    """kk"""
    pi = 3.1416
    unitpersec,amountpeople = map(int,input().split(" "))
    result = []
    for _ in range(amountpeople):
        x,y = map(int,input().split(" "))
        r = pi * ((x ** 2) + (y ** 2))
        result.append(math.ceil(r/unitpersec))
    for r in result:
        print(r)
main()
