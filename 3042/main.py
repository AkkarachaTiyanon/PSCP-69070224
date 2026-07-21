"""10 d"""
def main():
    """c"""
    k = int(input())
    # floor(k/10) * 10
    # หาตัวเลขใกล้เคียงของ k ทืี่สามารถหาร 10 ได้
    r = (k//10) * 10
    z = []
    while r > 0:
        r -= 10
        z.append(str(r))
    # "50 40 30... 0"
    print(" ".join(z))
main()
