"""Mkljs."""

def count_jumps(x, y):
    """a"""
    current_dist = x
    total_dist = 0
    jumps = 0

    while total_dist < y and current_dist > 0:
        total_dist += current_dist
        jumps += 1
        current_dist -= 2

    return jumps if total_dist >= y else -1


def main():
    """a"""
    x, y = map(int, input().split())
    print(count_jumps(x, y))

main()
