"""a"""
def main():
    """k"""
    a, b = map(int, input().split())

    primes = []
    for i in range(a, b + 1):
        if i < 2:
            continue
        passed = True
        for x in range(2, int(i**0.5) + 1):
            if not i % x:
                passed = False
                break
        if passed:
            primes.append(i)

    if primes:
        print(*primes)
    print(f"Total primes: {len(primes)}")

main()
