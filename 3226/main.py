"""o"""
def main():
    """l"""
    value = round(float(input().strip()) * 100)
    years = int(input().strip())
    for _ in range(years):
        value += value * 381 // 10000
    print(f"{value // 100}.{value % 100:02d}")
main()
