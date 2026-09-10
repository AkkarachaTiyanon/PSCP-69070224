"""js."""


def get_rank_name(rank_str):
    """a"""
    ranks = {
        "A": "ace",
        "J": "jack",
        "Q": "queen",
        "K": "king"
    }
    return ranks.get(rank_str, rank_str)


def get_suit_name(suit_char):
    """oooooo"""
    suits = {
        "D": "diamonds",
        "H": "hearts",
        "S": "spades",
        "C": "clubs"
    }
    return suits.get(suit_char, "")


def parse_card(card_str):
    """k"""
    card = card_str.strip().upper()
    rank_part = card[:-1]
    suit_part = card[-1]
    return f"{get_rank_name(rank_part)} of {get_suit_name(suit_part)}"


def main():
    """ooo"""
    card_input = input().strip()
    print(parse_card(card_input))

main()
