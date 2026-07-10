"""s"""
def main():
    """sfe"""
    width,long,floor = map(int,input().split())
    pricepermeter = int(input())

    x1 = (width + long) * 2
    ov = x1 * floor
    price = ov*pricepermeter
    print(ov)
    print(price)
main()
