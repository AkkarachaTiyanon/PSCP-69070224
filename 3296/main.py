"""oop."""


def mix_color(c1, c2):
    """lkjklj."""
    return (c1 + c2) // 2


def mix_rgb(c1, c2):
    """M0pp."""
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    r_mix = mix_color(r1, r2)
    g_mix = mix_color(g1, g2)
    b_mix = mix_color(b1, b2)
    return r_mix, g_mix, b_mix


def main():
    """j."""
    r1, g1, b1 = map(int, input().split())
    r2, g2, b2 = map(int, input().split())

    r_mix, g_mix, b_mix = mix_rgb((r1, g1, b1), (r2, g2, b2))

    print(f"{r_mix} {g_mix} {b_mix}")


main()
