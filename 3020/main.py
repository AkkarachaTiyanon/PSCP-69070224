"""ss"""
def main():
    """ssopwow"""
    Price = int(input())
    ReqCap = int(input())
    SpecialPrice = int(input())
    RequireCokeAmount = int(input())

    if not RequireCokeAmount:
        print(0)
        return

    if not ReqCap:
        print(RequireCokeAmount * Price)
        return

    currentcoke = 0
    cap = 0
    TotalPrice = 0
    while currentcoke < RequireCokeAmount:
        if cap >= ReqCap:
            cap -= ReqCap
            TotalPrice += SpecialPrice
            currentcoke += 1
            cap += 1
        else:
            TotalPrice += Price
            cap += 1
            currentcoke += 1
    print(TotalPrice)
main()
