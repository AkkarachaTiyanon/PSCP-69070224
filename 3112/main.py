"""s"""
PEARL_CAL = {
    'H': 5,
    'O': 3,
    'J': 2
}

TEA_CAL = {
    'R': {1: 12, 2: 18, 3: 25},
    'T': {1: 15, 2: 20, 3: 30},
    'M': {1: 10, 2: 15, 3: 20}
}

def main():
    """o"""
    pearl_type, pearl_weight = input().split()
    pearl_weight = float(pearl_weight)

    tea_type, sweetness, tea_volume = input().split()
    sweetness = int(sweetness)
    tea_volume = float(tea_volume)

    pearl_calories = pearl_weight * PEARL_CAL[pearl_type]
    tea_calories = tea_volume * TEA_CAL[tea_type][sweetness]

    total_calories = pearl_calories + tea_calories

    if total_calories.is_integer():
        print(int(total_calories))
    else:
        print(total_calories)
main()
