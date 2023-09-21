from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("LinkCount")
sc = SparkContext.getOrCreate(conf=conf)

n = 50  # số lượng trang Web top được liên kết đến nhiều nhất

# đường dẫn tới file cần đọc
file_path = "/home/hdoop/Downloads/Data-3"

# đọc file và đếm số lượng liên kết đến từng trang Web
counts = (
    sc.textFile(file_path)
    .map(lambda line: line.strip().split('\t'))
    .map(lambda x: (x[1], 1))
    .reduceByKey(lambda x, y: x + y)
)

# lấy top n trang Web được liên kết đến nhiều nhất
top_nodes = (
    counts
    .map(lambda x: (x[1], x[0]))  # đổi vị trí key và value để có thể sắp xếp
    .sortByKey(ascending=False)
    .take(n)
)

# in ra top n trang Web được liên kết đến nhiều nhất
for (count, node) in top_nodes:
    print(f"{node}\t{count}")


