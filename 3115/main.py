"""o"""
def main():
    """l"""
    line1 = input().split()
    num = int(line1[0])

    diff = [0] * 1442

    for _ in range(num):
        start, stop = map(int, input().split())
        diff[start] += 1
        diff[stop] -= 1

    stores_open = [0] * 1442
    current_open = 0
    for i in range(1441):
        current_open += diff[i]
        stores_open[i] = current_open

    queries = map(int, input().split())
    result = [str(stores_open[k]) for k in queries]

    print(" ".join(result))

main()