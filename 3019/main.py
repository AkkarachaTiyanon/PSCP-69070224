"""s"""
def main():
    """dog"""
    key = input()
    code = int(input())
    result = "safe locked"
    if key == "H":
        if code == 4567:
            result = "safe unlocked"
        else:
            result = "safe locked - change digit"
    else:
        if code == 4567:
            result = "safe locked - change char"
    print(result)
main()
