"""าา"""


def main():
    """a"""
    raw_input = input().strip().split()
    if len(raw_input) < 4:
        return

    w, l, m, n = map(int, raw_input)
    min_waste = w * l

    for a in range(m, n + 1):
        horizontal_area = w * (l - (l % a))

        vertical_area = (l % a) * (w // a) * a

        waste = (w * l) - (horizontal_area + vertical_area)

        if waste < min_waste:
            min_waste = waste
            if not min_waste:
                break

    print(min_waste)

main()
