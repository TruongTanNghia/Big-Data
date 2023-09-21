from pyspark import SparkContext

sc = SparkContext(appName="LinkList")

# Đọc file từ máy tính
lines = sc.textFile("/home/hdoop/Downloads/Data-3")

# Tạo RDD gồm các cặp key-value
# Trong đó key là tên trang web, value là tên các trang web mà trang đó liên kết đến
links = lines.map(lambda line: line.strip().split('\t')) \
             .map(lambda x: (x[0], x[1]))

# GroupByKey để tạo danh sách các trang web liên kết với mỗi trang web
linked_nodes = links.groupByKey() \
                    .mapValues(list)

# In ra kết quả
for (node, links) in linked_nodes.collect():
    print(f"{node}\t{links}")
