#!/usr/bin/python3
'''reducer.py'''

import sys

current_node = None
current_count = 0

for line in sys.stdin:
    # Tach key va value cua dong hien tai
    node, count = line.strip().split('\t')
    
    # Kiem tra xem key cua dong hien tai co trung voi key cua dong truoc do hay khong
    if node != current_node:
        # In ra key va tong so luong cua key truoc do (neu co)
        if current_node is not None:
            print(f"{current_node}\t{current_count}")
        # Cap nhat lai key va tong so luong moi
        current_node = node
        current_count = 1
    else:
        # Cong them 1 vao tong so luong cua key hien tai
        current_count += 1

# In ra key va tong so luong cua key cuoi cung
if current_node is not None:
    print(f"{current_node}\t{current_count}")
