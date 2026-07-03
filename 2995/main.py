"""main func"""
def main():
    """input"""
    studentid = input()
    if (len(studentid) == 8 and studentid[2] == "1" and studentid[3] == "6"):
        print("yes")
    else:
        print("no")
main()
