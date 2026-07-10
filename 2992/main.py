"""ddd"""
def main():
    """ssdlk;jdew"""
    a = int(input())
    operation = input()
    b = int(str(a)[::-1])
    result = 0
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a-b
    elif operation == "*":
        result = a*b
    elif operation == "/":
        result = a/b
    print(f'{a} {operation} {b} = {result}')
main()
