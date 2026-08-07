"""s"""
def main():
    """z"""
    N = int(input())
    PASSED = "PASS"
    AVG = 0
    for _ in range(N):
        score = int(input())
        if score < 50:
            PASSED = "FAIL"
        AVG += score
    AVG /= N
    if AVG < 60:
        PASSED = "FAIL"
    print(f"{AVG:.1f}")
    print(PASSED)
main()
