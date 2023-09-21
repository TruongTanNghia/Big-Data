#!/usr/bin/python3


import sys

for line in sys.stdin:
    # Tach cac cot cach nhau boi khoang trang
    columns = line.strip().split()
    
    # Kiem tra xem dong hien tai co du 2 cot hay khong
    if len(columns) == 2:
        # Ghi key la FromNodeId va value la ToNodeId
        print(f"{columns[0]}\t{columns[1]}")
