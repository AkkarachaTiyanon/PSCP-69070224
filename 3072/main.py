"""x"""
vowels = ['a', 'e', 'i', 'o', 'u']

def main():
    """l"""
    text = input().lower()
    vowels_count = [0, 0, 0, 0, 0]

    for char in text:
        if char == 'a':
            vowels_count[0] += 1
        elif char == 'e':
            vowels_count[1] += 1
        elif char == 'i':
            vowels_count[2] += 1
        elif char == 'o':
            vowels_count[3] += 1
        elif char == 'u':
            vowels_count[4] += 1

    for i, vowel in enumerate(vowels):
        if vowels_count[i] > 0:
            print(f"{vowel} : {vowels_count[i]}")
main()
