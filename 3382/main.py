"""x"""

def main():
    """w"""
    txts = []
    while True:
        i = input()
        if i != "NULL":
            txts.append(i)
        else:
            break
    for i in range(len(txts),0,-1):
        print(txts[i-1])
main()
