"""x"""
def main():
    """s"""
    a, b, c = map(int, input().split())

    total_price = (a * 25) + (b * 40) + (c * 55)
    total_items = a + b + c
    if total_items >= 3:
        net_price = total_price * 0.9
    else:
        net_price = total_price

    print(int(net_price))
main()
