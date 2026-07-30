"""a"""
def main():
    """k"""
    even_count = 0
    odd_count = 0

    for _ in range(3):
        num = int(input())
        if not num % 2:
            even_count += 1
        else:
            odd_count += 1
    print(f"{even_count}")
    print(f"{odd_count}")
main()
