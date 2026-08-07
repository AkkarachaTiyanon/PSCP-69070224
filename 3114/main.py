"""kkk"""

def parse_time(time_str):
    """time float > hour"""
    parts = time_str.split('.')
    if len(parts) != 2:
        return
    hours = int(parts[0])
    minutes = int(parts[1])
    if 0 <= hours <= 23 and 0 <= minutes <= 59:
        return hours * 60 + minutes

def calculate_fee(minutes):
    """cal fee from min"""
    if minutes <= 15:
        return 0

    hours = (minutes + 59) // 60

    if hours == 1:
        return 25
    elif hours == 2:
        return 50
    elif hours == 3:
        return 80
    elif hours == 4:
        return 110
    elif hours == 5:
        return 145
    elif hours == 6:
        return 180
    elif 7 <= hours <= 24:
        return 250

def main():
    entry_str = input().strip()
    exit_str = input().strip()

    entry_min = parse_time(entry_str)
    exit_min = parse_time(exit_str)

    if entry_min is None or exit_min is None:
        print("ERROR")
        return

    duration = exit_min - entry_min
    if duration < 0:
        duration += 24 * 60

    fee = calculate_fee(duration)

    if fee is None:
        print("ERROR")
    else:
        print(fee)
main()
