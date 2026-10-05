#!/usr/bin/env python3
import sys

# 1. ดึงพารามิเตอร์ที่ผู้ใช้พิมพ์เข้ามาทั้งหมด (ไม่รวมชื่อไฟล์สคริปต์)
arguments = sys.argv[1:]

# 2. ตรวจสอบเงื่อนไข: ถ้าพารามิเตอร์น้อยกว่า 2 ตัว ให้พิมพ์ none
if len(arguments) < 2:
    print("none")
else:
    # 3. ถ้าพารามิเตอร์ตั้งแต่ 2 ตัวขึ้นไป ให้กลับด้านลำดับจากหลังมาหน้า
    # การใช้ [::-1] คือวิธีสลับตำแหน่งลิสต์จากท้ายสุดมาหน้าสุดของ Python
    reversed_arguments = arguments[::-1]
    
    # 4. วนลูปพิมพ์ทีละตัวออกมา
    for arg in reversed_arguments:
        print(arg)
