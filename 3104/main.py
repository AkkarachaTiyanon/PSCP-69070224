"""z"""
def main():
    """k"""
    x = input().lower().split()
    age,day = int(x[0]),x[1]
    price = 0
    if age < 5:
        price = 0
    elif 5 <= age <= 18:
        price = 100
    elif age >= 19:
        price = 150
    if day == "wed":
        price //= 2
    print(price)
main()
