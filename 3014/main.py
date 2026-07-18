"""s"""

def main():
    """sd"""
    real_price = int(input())
    sale_cap = int(input())
    sale_milk = int(input())
    budget = int(input())

    bottle = budget // real_price
    total_milk = bottle
    mycap = total_milk

    if sale_cap > 0:
        while mycap >= sale_cap:
            new = mycap // sale_cap
            new_milk = new * sale_milk
            total_milk += new_milk
            mycap = (mycap % sale_cap) + new_milk
    print(total_milk)
main()
