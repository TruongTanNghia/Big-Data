#!/usr/bin/python3

import sys

for line in sys.stdin:
    # Tach cac cot cach nhau boi khoang trang
    columns = line.strip().split()
    
    # Kiem tra xem dong hien tai co du 2 cot hay khong
    if len(columns) == 2:
        # Ghi key la ToNodeId va value la 1
        print(f"{columns[1]}\t1")
