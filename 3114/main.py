"""x"""
import math

x = [25,50,80,110,145,180,250]

def main():
    """kk"""
    start = float(input())
    end = float(input())

    dt = end - start
    if dt <= 0.15:
        print("FREE")
    else:
        dt = math.ceil(dt)
        if  0 < dt <= 6:
            print(x[dt-1])
        elif 7 <= dt <= 24:
            print(x[-1])
        else:
            print("ERROR")
main()