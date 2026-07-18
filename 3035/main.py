"""s"""
def main():
    """s"""
    z = input().split(" ")
    r,x,y = int(z[0]),int(z[1]),int(z[2])
    cir = r**2
    cir2 = x**2 + y**2
    if cir2 < cir:
        print("IN")
    elif cir2 == cir:
        print("ON")
    else:
        print("OUT")
main()
