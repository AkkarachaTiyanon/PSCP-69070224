"""kk"""
def main():
    """s"""
    k = float(input())
    sc = k*0.1
    if sc < 50:
        sc = 50
    elif sc > 1000:
        sc = 1000
    r = (k + sc) * 1.07
    print(f'{r:.2f}')
main()
