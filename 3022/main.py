"""Module"""

def temp_to_c(t: float, n: str):
    """kk."""
    ln = n.lower()
    if ln == "k":
        return t - 273.15
    if ln == "f":
        return (t - 32) * (5 / 9)
    if ln == "r":
        return (t - 491.67) * (5 / 9)
    return t

def c_to_temp(t: float, n: str):
    """Co"""
    ln = n.lower()
    if ln == "k":
        return t + 273.15
    if ln == "f":
        return (t * (9 / 5)) + 32
    if ln == "r":
        return (t + 273.15) * (9 / 5)
    return t

def main():
    """Main"""
    temp = float(input())
    inputtemp = input()
    outputtemp = input()
    celsius_val = temp_to_c(temp, inputtemp)
    print(f'{c_to_temp(celsius_val, outputtemp):.2f}')
main()
