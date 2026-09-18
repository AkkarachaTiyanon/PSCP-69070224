"""w"""
import json

def main():
    """w"""
    w = json.loads(input())
    hadeven = False
    for i in w:
        if not i % 2:
            hadeven = True
    if hadeven:
        for i in w:
            if not i % 2:
                print(i)
    else:
        print("Nope")
main()
