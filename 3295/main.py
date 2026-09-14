"""w"""
def main():
    """k"""
    units = int(input().strip())

    base_cost = 0
    u = units

    if u > 200:
        base_cost += (u - 200) * 15
        u = 200
    if u > 100:
        base_cost += (u - 100) * 12
        u = 100
    if u > 50:
        base_cost += (u - 50) * 10
        u = 50
    if u > 10:
        base_cost += (u - 10) * 7
        u = 10
    if u > 0:
        base_cost += u * 5

    total_x10 = (base_cost * 10) + (units * 5) + int(round(base_cost * 0.7))

    total = total_x10 / 10.0

    print(f"{total:.1f}")
main()
