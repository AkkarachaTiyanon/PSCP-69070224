"""e"""
def main():
    """find aabb"""
    x1,y1,w1,h1 = map(int,input().split(" "))
    x2,y2,w2,h2 = map(int,input().split(" "))

    # rope หาจุดเริ่มทับโดย หาจุดห่างกว่า 0
    start_overlap_X = max(x1,x2)
    # หาจุดสิ้นสุดที่จะทับได้
    end_overlap_X = min(x1+w1,x2+w2)

    # rope หาจุดเริ่มทับโดย หาจุดห่างกว่า 0
    start_overlap_Y = max(y1,y2)
    # หาจุดสิ้นสุดที่จะทับได้
    end_overlap_Y = min(y1+h1,y2+h2)

    # ก x ย
    overlap_area = (start_overlap_X - end_overlap_X) * (start_overlap_Y - end_overlap_Y)
    if overlap_area > 0:
        print(overlap_area)
    else:
        print("no overlapping")
main()
