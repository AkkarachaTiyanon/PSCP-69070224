"""s"""
def main():
    """o"""
    line1 = input().split()
    size, ramen_type = line1[0], line1[1]

    prices = {
        ('S', 'R'): 60,
        ('S', 'T'): 80,
        ('M', 'R'): 80,
        ('M', 'T'): 100,
        ('L', 'R'): 100,
        ('L', 'T'): 120,
    }

    total_price = prices.get((size, ramen_type), 0)

    line2 = input().split()
    topping = line2[0]

    if topping == 'P':
        total_price += int(line2[1]) * 15
    elif topping == 'E':
        total_price += int(line2[1]) * 10

    print(total_price)

main()
