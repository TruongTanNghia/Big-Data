#!/usr/bin/python3
'''reducer.py'''

import sys
from collections import defaultdict

node_counts = defaultdict(int)

for line in sys.stdin:
    # Tach key va value cua dong hien tai
    node, count = line.strip().split('\t')
    node_counts[node] += int(count)

# Chon ra 50 ToNodeId co so lan xuat hien nhieu nhat
top_nodes = sorted(node_counts.items(), key=lambda x: x[1], reverse=True)[:50]

# In ra danh sach 50 ToNodeId
for node, count in top_nodes:
    print(f"{node}\t{count}")
