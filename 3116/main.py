def main():
    school_name = input()
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    first_char_ascii = ord(school_name[0].upper())
    last_char_ascii = ord(school_name[-1].upper())

    step1_data = []
    for i in range(10):
        position = i + 1
        base_value = values[i]

        if position % 2 != 0:
            new_val = first_char_ascii + base_value
        else:
            new_val = last_char_ascii - base_value

        step1_data.append(new_val)

    name_length = len(school_name)
    step2_data = []

    for val in step1_data:
        remainder = val % name_length

        if remainder > 9:
            remainder = remainder % 10

        step2_data.append(remainder)
    final_password_digits = step2_data[2:8]
    password = "".join(map(str, final_password_digits))
    print(password)

main()
