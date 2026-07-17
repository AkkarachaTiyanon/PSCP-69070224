"""s"""
def main():
    """fe"""
    PI = 3.14
    s = input().split(" ")
    rad,height,glue = float(s[0]),float(s[1]),float(s[2])
    width = height + (2*rad)
    length = (2*PI*rad) + glue
    print(f'{width:.2f} {length:.2f}')
main()
