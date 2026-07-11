"""ss"""
def main():
    """ssdfr"""
    month = int(input())
    day = int(input())

    seasonlist = ["winter","spring","summer","fall"]
    idx = (month - 1) // 3

    if not month % 3 and day >= 21:
        idx = (idx + 1) % 4
    print(seasonlist[idx])
main()
