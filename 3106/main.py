"""s"""
def main():
    """x"""
    money = int(input())
    t1 = money//1000
    money -= t1 * 1000
    t2 = money//500
    money -= t2 * 500
    t3 = money//100
    money -= t3 * 100

    if (not t1 and not t2 and not t3) or (money % 100) or (100<money>20000):
        print("ERROR")
        return

    if t1:
        print(f'1000 = {t1}')
    if t2:
        print(f'500 = {t2}')
    if t3:
        print(f'100 = {t3}')
main()
