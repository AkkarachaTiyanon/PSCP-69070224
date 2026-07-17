"""s"""
def main():
    """d"""
    money = int(input())
    tencoin = 0
    fivecoin = 0
    twocoin = 0
    onecoin = 0
    while money > 0:
        if money >= 10:
            tencoin += 1
            money -=  10
        elif money >= 5:
            fivecoin += 1
            money -= 5
        elif money >= 2:
            twocoin += 1
            money -= 2
        elif money >= 1:
            onecoin += 1
            money -=1
    print(f'10 = {tencoin}')
    print(f'5 = {fivecoin}')
    print(f'2 = {twocoin}')
    print(f'1 = {onecoin}')
main()
