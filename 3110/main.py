"""od"""
shipping_rates = {
    ("BKK", "CNX"): (10, 30),
    ("CNX", "UBP"): (15, 40),
    ("UBP", "BKK"): (20, 40),
    ("BKK", "PKT"): (25, 50),
    ("PKT", "CNX"): (30, 60),
    ("UBP", "PKT"): (40, 70)
}

def main():
    """o"""
    origin, destination = input().split()

    weight = float(input())
    route_key = (origin, destination)
    if route_key in shipping_rates:
        base_fee, weight_fee = shipping_rates[route_key]

        total_price = base_fee + (weight * weight_fee)

        print(f"{total_price:.2f}")
    else:
        print("Error")
main()
