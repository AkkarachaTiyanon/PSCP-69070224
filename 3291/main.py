"""x"""
def print_turn_signal(k, n):
    """w"""
    mid = n // 2
    for i in range(n):
        indent = mid - abs(mid - i)
        print(" " * indent + "*" * k)


def main():
    """z"""
    k = int(input())
    n = int(input())
    print_turn_signal(k, n)

main()
