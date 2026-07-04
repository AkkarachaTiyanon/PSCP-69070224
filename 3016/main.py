"""deefw"""
def main():
    """fff"""
    n = int(input())
    firstdigit = [7,9,3,1]
    last2n = n%100
    x = last2n%len(firstdigit)
    r = firstdigit[x-1]
    print(r)
main()
