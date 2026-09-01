"""oo"""
import math

def parse_time(s):
    """k"""
    try:
        h, m = map(int, s.replace(".", ":").replace(" ", ":").split(":"))
        if 0 <= h <= 23 and 0 <= m <= 59:
            return h * 60 + m
    except Exception:
        return None

def main():
    """o"""
    t1 = parse_time(input().strip())
    t2 = parse_time(input().strip())

    if t1 is None or t2 is None:
        print("ERROR")
        return

    diff = t2 - t1
    if diff < 0:
        diff += 1440

    if diff <= 15:
        print(0)
        return

    hrs = math.ceil(diff / 60)
    rates = {1: 25, 2: 50, 3: 80, 4: 110, 5: 145, 6: 180}

    if 1 <= hrs <= 6:
        print(rates[hrs])
    elif 7 <= hrs <= 24:
        print(250)
    else:
        print("ERROR")
main()
