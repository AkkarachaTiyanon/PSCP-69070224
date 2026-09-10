"""k."""

def main():
    """o"""
    numbers = input().strip().split()
    matched = []

    for num in numbers:
        val = int(num)
        if not val % 3 or not val % 5:
            matched.append(num)

    if not matched:
        print("Nope")
    else:
        for num in matched[::-1]:
            print(num)


main()
