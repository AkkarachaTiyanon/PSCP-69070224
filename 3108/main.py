"""x"""
def main():
    """s"""
    a,b,c = map(int,input().split())
    total_items = a+b+c
    total_price = (a*25) + (b*40) + (c*55)

    net = 0
    if total_items >= 3 : 
        net = total_price * 90 // 100
    else:
        net = total_price
    print(net)
main()
