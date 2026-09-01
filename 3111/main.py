"""saint"""

def main():
    """kk"""
    is_member = input().upper()

    n = int(input())

    total_price = 0.0
    for _ in range(n):
        price = float(input())
        total_price += price

    if is_member == 'Y':
        discount_rate = 0.05
    elif is_member == 'N' and total_price >= 500:
        discount_rate = 0.03
    else:
        discount_rate = 0.00

    net_total = total_price * (1 - discount_rate) + 1e-9
    print(f"{net_total:.2f}")

main()
