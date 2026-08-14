"""Ss"""
import math

def main():
    """ss"""
    n = float(input())
    k = int(input())
    for _ in range(k):
        n = math.floor((n * (1.0381))*100) / 100
    print(n)
main()
