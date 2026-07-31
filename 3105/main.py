"""x"""
def main():
    """w"""
    distance = int(input())
    if distance <= 0:
        finalprice = 0
    elif distance <= 1:
        finalprice = 35
    elif distance <= 10:
        finalprice = 35 + ((distance - 1) * 5)
    else:
        finalprice = 80 + ((distance - 10) * 8)
    print(finalprice)
main()
