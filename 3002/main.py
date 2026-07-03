"""sss"""
def main():
    """dddd"""
    name = input()
    surname = input()
    age = input()
    passwd = ""
    if len(name) >= 5:
        passwd = f'{name[::2]}{surname[-1]}{age[-1]}'
    else:
        passwd = f'{name[0]}{age}{surname[-1]}'
    print(passwd)
main()
