"""x"""
def main():
    """kkk"""
    al = []
    n = int(input())
    for _ in range(n):
        a = int(input())
        b = int(input())
        al.append(max(a,b))
    if n == 1:
        print(al[0])
    else:
        sumX = sum(al)
        eq = " + ".join(map(str,al))
        output = f"{eq} = {sumX}"
        print(output)
main()
