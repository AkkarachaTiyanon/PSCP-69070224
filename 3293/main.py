"""x"""
def main():
    """k"""
    txts = [input().rstrip() for _ in range(5)]
    max_len = max(len(s) for s in txts)

    border = "*" * (max_len + 4)
    print(border)
    for s in txts:
        print(f"* {s:<{max_len}} *")
    print(border)

main()
