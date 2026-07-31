"""z"""
def main():
    """x"""
    bc = int(input())
    cc = int(input())

    c = 0
    if cc <= 1500:
        c = 0
    elif 1500 < cc <= 2000:
        c = 1
    else:
        c = 2

    bc1 = [1250,1400,2000]
    bc2 = [1100,1300,1700]
    bc3 = [1000,1200,1500]
    if bc <= 1990:
        print(bc1[c])
    elif 1991 <= bc <= 1999:
        print(bc2[c])
    else:
        print(bc3[c])
main()
