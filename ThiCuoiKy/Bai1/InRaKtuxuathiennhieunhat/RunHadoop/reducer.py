#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter
import sys

# Tạo một từ điển trống để lưu trữ tần suất của các từ
word_counts = {}

# Lấy dữ liệu từ thiết bị nhập chuẩn
for line in sys.stdin:
    # Loại bỏ ký tự trắng ở đầu và cuối chuỗi và tách thành các từ đơn lẻ
    words = line.strip().split()

    # Tăng tần suất cho mỗi từ
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

# Sắp xếp các từ theo thứ tự giảm dần và lấy 20 từ đầu tiên
top_words = sorted(word_counts.items(), key=itemgetter(1), reverse=True)[:50]

# In ra top 20 từ
for word, count in top_words:
    print(f"{word}\t{count}")
print('{}\t{}'.format(word, count))
