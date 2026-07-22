"""s"""
def main():
    """sfe"""
    width,long,floor = map(int,input().split())
    pricepermeter = int(input())

    fenchLength = (width + long) * 2
    Overall_fence_length = fenchLength * floor
    price = Overall_fence_length*pricepermeter
    print(Overall_fence_length)
    print(price)
main()
