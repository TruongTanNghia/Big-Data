#!/usr/bin/python3
'''reducer.py'''

import sys

# Khởi tạo giá trị năm, nhiệt độ, số lượng nhiệt độ và tổng nhiệt độ
(last_year, max_temp, min_temp, total_temp, count) = (None, -sys.maxsize, sys.maxsize, 0, 0)

for line in sys.stdin:
    # Lấy cặp giá trị <k, v> = <year, temp> từ stdin
    (year, temp) = line.strip().split("\t")

    # Nếu năm đọc vào khác năm đang xét -> (1) đưa ra stdout năm trước đó cùng với nhiệt độ cao nhất, thấp nhất và trung bình
    if last_year is not None and last_year != year:
        avg_temp = total_temp / count
        print("%s\t%s\t%s\t%s" % (last_year, max_temp, min_temp, avg_temp))

        # và (2) chuyển <năm, nhiệt độ> đọc vào thành <năm, nhiệt độ> đang xét:
        (last_year, max_temp, min_temp, total_temp, count) = (year, int(temp), int(temp), int(temp), 1)

    else:
        # Nếu năm đọc vào trùng với năm đang xét -> tìm nhiệt độ lớn nhất, nhỏ nhất và tính nhiệt độ trung bình:
        (last_year, total_temp, count) = (year, total_temp + int(temp), count + 1)
        max_temp = max(max_temp, int(temp))
        min_temp = min(min_temp, int(temp))

# In ra kết quả cho năm cuối cùng:
if last_year is not None:
    avg_temp = total_temp / count
    print("%s\t%s\t%s\t%s" % (last_year, max_temp, min_temp, avg_temp))
