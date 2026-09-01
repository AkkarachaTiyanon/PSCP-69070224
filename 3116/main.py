def generate_school_password(school_name: str) -> str:
    # 1. นับจำนวนอักขระทั้งหมดในชื่อโรงเรียน (รวมช่องว่าง)
    N = len(school_name)

    # ดึงอักขระตัวแรกและตัวสุดท้าย แปลงเป็นตัวพิมพ์ใหญ่เพื่อหาค่า ASCII
    first_char = school_name[0].upper()
    last_char = school_name[-1].upper()

    ascii_first = ord(first_char)
    ascii_last = ord(last_char)

    # ----------------------------------------------------
    # การสร้างรหัสชั้นที่ 1
    # ----------------------------------------------------
    layer1 = []
    for pos in range(1, 11):
        val_initial = pos - 1  # ค่าประจำหลัก (0-9)

        if pos % 2 != 0:  # หมายเลขหลักหารด้วย 2 ไม่ลงตัว (หลักคี่)
            val1 = ascii_first + val_initial
        else:  # หมายเลขหลักหารด้วย 2 ลงตัว (หลักคู่)
            val1 = ascii_last - val_initial

        layer1.append(val1)

    layer2 = []
    for val1 in layer1:
        rem = val1 % N  # หารด้วยจำนวนอักขระ (N) เอาเศษเหลือ
        if rem > 9:  # ถ้าเศษเหลือมากกว่า 9 ให้หารด้วย 10 เอาเศษเหลือแทน
            rem = rem % 10
        layer2.append(rem)

    # ----------------------------------------------------
    # การสร้างรหัสชั้นที่ 3
    # ----------------------------------------------------
    # คัดเลือกรหัส 6 ตัวกึ่งกลาง (หลักที่ 3 ถึง 8 หรือ index 2 ถึง 7)
    middle_6 = layer2[2:8]

    # แปลงเป็นข้อความตัวเลขต่อกัน 6 หลัก
    return "".join(map(str, middle_6))


# รับค่าข้อมูลนำเข้าผ่าน input()
if __name__ == "__main__":
    # ใช้ input() รับค่าบรรทัดเดียว
    school_name = input()

    if school_name:
        result = generate_school_password(school_name)
        print(result)