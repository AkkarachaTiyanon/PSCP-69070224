"""."""


def get_floor(d):
    """a"""
    if d[0] > 5:
        return "9"
    if d[1] > 5:
        return "10"
    if d[2] > 5:
        return "11"
    if d[3] > 5:
        return "12"
    if d[4] > 5:
        return "14"
    return "13"


def get_digit2(d):
    """a"""
    if d[0] == d[4] and d[1] == d[3]:
        if d[0] + d[4] > 5:
            return "1"
        if d[1] * d[3] > 5:
            return "2"
        return "0"

    div_val = d[0] // d[4] if d[4] else 0
    if div_val > 5:
        return "1"
    if d[1] - d[4] > 5:
        return "2"
    return "0"


def get_digit3(d):
    """a"""
    if sum(d) > 25:
        return "1"

    total_prod = 1
    for x in d:
        total_prod *= x

    if total_prod > 55:
        return "2"
    return "0"


def decode_room(n_str):
    """a"""
    d = [int(c) for c in n_str.zfill(5)]
    return get_floor(d) + get_digit2(d) + get_digit3(d)


def main():
    """a"""
    n_input = input().strip()
    print(decode_room(n_input))
main()
