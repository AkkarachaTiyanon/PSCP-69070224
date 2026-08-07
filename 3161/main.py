"""ss"""
def main():
    """z"""
    k = int(input())
    for i in range(1,k+1):
        if not i % 5 and i:
            print("X",end="")
        else:
            print("*",end="")
main()
