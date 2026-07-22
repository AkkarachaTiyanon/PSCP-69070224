"""kk"""
def main():
    """s"""
    Price = float(input())

    Servicecharge = Price*0.1
    if Servicecharge < 50:
        Servicecharge = 50
    elif Servicecharge > 1000:
        Servicecharge = 1000
    TotalPrice = (Price + Servicecharge) * 1.07

    print(f'{TotalPrice:.2f}')
main()
