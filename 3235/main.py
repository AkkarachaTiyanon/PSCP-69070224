"""z"""
def main():
    """w"""
    k = int(input())
    mostfat = ""
    _mf = 0
    fatcount = 0
    for _ in range(k):
        h = input().split()
        name,weight = h[0],int(h[1])
        if weight > 15:
            fatcount += 1
        if weight > _mf:
            mostfat = name
            _mf = weight
    print(fatcount)
    if len(mostfat) > 0:
        print(mostfat)

main()
