"""s"""
roman_dict = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
}

def main():
    """o"""
    number = int(input().strip())
    if number < 0:
        print("Error : Please input positive number")
        return

    if not number or number > 9:
        print("Error : Out of range")
        return

    print(roman_dict[number])
main()
