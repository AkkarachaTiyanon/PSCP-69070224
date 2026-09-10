"""jjkljklh"""
def get_prize(winning_card, user_card):
    """akl"""
    win_letter, win_num = winning_card.split()
    user_letter, user_num = user_card.split()

    is_letter_match = win_letter == user_letter
    is_num_match = win_num == user_num
    is_last_2 = win_num[-2:] == user_num[-2:]
    is_last_3 = win_num[-3:] == user_num[-3:]

    if is_letter_match and is_num_match:
        return 1000000
    if is_num_match:
        return 100000
    if is_last_3 and is_letter_match:
        return 2000
    if is_last_2 and is_letter_match:
        return 1000
    if is_last_3:
        return 200
    if is_last_2:
        return 100
    if is_letter_match:
        return 20

    return 0


def main():
    """a"""
    winning_input = input().strip()
    user_input = input().strip()
    print(get_prize(winning_input, user_input))

main()
