#!/usr/bin/python3
'''reducer.py'''

import sys

current_node = None
linked_nodes = []

for line in sys.stdin:
    # Tach key va value cua dong hien tai
    node, linked_node = line.strip().split('\t')
    
    # Kiem tra xem key cua dong hien tai co trung voi key cua dong truoc do hay khong
    if node != current_node:
        # In ra danh sach cac Web lien ket voi Web truoc do (neu co)
        if current_node is not None:
            print(f"{current_node}\t{linked_nodes}")
        # Cap nhat lai Web hien tai va danh sach Web lien ket moi
        current_node = node
        linked_nodes = [linked_node]
    else:
        # Them Web lien ket moi vao danh sach
        linked_nodes.append(linked_node)

# In ra danh sach cac Web lien ket voi Web cuoi cung
if current_node is not None:
    print(f"{current_node}\t{linked_nodes}")
