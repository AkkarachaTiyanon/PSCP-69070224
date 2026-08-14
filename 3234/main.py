"""x"""
hit = ["r","g","b"]
steps = ["Red","Green","Blue"]
def main():
    """kekw"""
    raw = input().split()
    firststep = int(hit.index(raw[0].lower())) + 1
    loop = int(raw[1])
    while loop > 0:
        print(steps[(firststep - 1) % 3],end=" ")
        firststep += 1
        loop -= 1
main()
