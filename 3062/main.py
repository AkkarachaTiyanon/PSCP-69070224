"""ค่าตั๋ว"""
def main():
    """noo"""
    a = int(input())
    b = input()[0]
    if b.lower() == "s" or a < 18:
        print(20)
    else:
        print(50)
main()
