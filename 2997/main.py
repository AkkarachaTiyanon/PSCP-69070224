"""kkk"""
def main():
    """ddddd"""
    RA = int(input())
    RB = int(input())
    SOMETHING = input()
    EA = 1/( 1+(pow(10,((RB-RA)/400))))
    EB = 1/( 1+(pow(10,((RA-RB)/400))))
    if SOMETHING == "A":
        print(f'{EA:.2f}')
    elif SOMETHING == "B":
        print(f'{EB:.2f}')
main()
