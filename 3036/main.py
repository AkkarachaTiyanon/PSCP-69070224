"""ss"""
import math

def main():
    """kl"""
    N = int(input())

    if N == 1:
        print(0)
        return

    #get floor
    r = math.isqrt(N - 1) + 1
    #count room N
    i = N - (r - 1)**2

    if i % 2:
        min_walls = (2 * r) - 2
    else:
        min_walls = (2 * r) - 3

    print(min_walls)

main()
