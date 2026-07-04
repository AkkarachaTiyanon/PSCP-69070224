"""dogg"""
def main():
    """ss"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())
    pro = z//x
    left = z%x
    price = (pro * y * a) + (left * a)
    print(price)
main()
