"""f"""
def main():
    """k"""
    N, K = map(int, input().split())

    queue_counts = [0] * (K + 1)

    for _ in range(N):
        queue_number = int(input())
        queue_counts[queue_number] += 1

    min_passengers_in_queue = min(queue_counts[1:K+1])

    departed_passengers = min_passengers_in_queue * K
    waiting_passengers = N - departed_passengers

    print(waiting_passengers)

main()
