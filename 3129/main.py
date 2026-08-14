"""s"""
def main():
    """w"""
    zap = int(input())
    overall = 0
    highest = 0
    lowest = 1000
    for _ in range(zap):
        sell = int(input())
        overall += sell
        if sell > highest:
            highest = sell
        if sell < lowest:
            lowest = sell
    avg = overall/zap
    print(overall)
    print(highest)
    print(lowest)
    print(f"{avg:.1f}")
main()
