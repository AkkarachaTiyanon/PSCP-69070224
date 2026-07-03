"""this main function"""
def main():
    """input"""
    name = input()
    surname = input()

    print(f'Hello {name} {surname}')
    print(f'{name[:2]}{surname[-1]}')

main()
