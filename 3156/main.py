"""shis"""
dickhead = [chr(i) for i in range(ord('a'),ord('z') + 1)]
def main():
    """s"""
    a = input()
    move = int(input())
    cipher = ""
    for char in a:
        dog = dickhead.index(char.lower())
        cipherchar = dickhead[(dog + move) % len(dickhead)]
        cipher = cipher + cipherchar
    print(cipher)
main()
