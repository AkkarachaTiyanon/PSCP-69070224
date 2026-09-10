"""ota."""


def main():
    """a"""
    parts = input().split()
    x = int(parts[0])
    k = parts[1]

    mid = x // 2

    for row in range(x):
        if k == "#":
            char = "#"
        else:
            distance = abs(mid - row)
            char = chr(ord(k) + distance)

        line = ""
        for col in range(x):
            if col in (row,x - 1 - row):
                line += char
            else:
                line += "-"

        print(line)
main()
