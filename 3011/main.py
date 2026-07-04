"""docdoc"""
def main():
    """z"""
    c1 = input().lower()
    c2 = input().lower()

    cc = {c1,c2}
    result = ""
    if cc == {"red","yellow"}:
        result = "Orange"
    elif cc == {"red","blue"}:
        result = "Violet"
    elif cc == {"yellow","blue"}:
        result = "Green"
    elif cc == {"red"}:
        result = "Red"
    elif cc == {"yellow"}:
        result = "Yellow"
    elif cc == {"blue"}:
        result = "Blue"
    else:
        result = "Error"
    print(result)
main()
