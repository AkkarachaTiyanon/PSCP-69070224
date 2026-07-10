"""ss"""
def main():
    """ssopwow"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if not d:
        print(0)
        return

    if not b:
        print(d * a)
        return

    currentcoke = 0
    cap = 0
    price = 0
    while currentcoke < d:
        if cap >= b:
            cap -= b
            price += c
            currentcoke += 1
            cap += 1
        else:
            price += a
            cap += 1
            currentcoke += 1
    print(price)
main()
