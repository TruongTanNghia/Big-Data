from pyspark import SparkContext

sc = SparkContext("local", "WordCount112")

# Đọc dữ liệu từ file input vào RDD
lines = sc.textFile("/home/hdoop/Downloads/gutenberg/*.txt").cache()

# Thực hiện phép Map để tạo các cặp (word, 1)
words = lines.flatMap(lambda line: line.strip().split()).map(lambda word: (word, 1))

# Thực hiện phép Reduce để đếm số lần xuất hiện của các từ
wordCounts = words.reduceByKey(lambda x, y: x + y)

# In ra kết quả
for (word, count) in wordCounts.collect():
    print(word, count)
# spark-submit
spark.stop()
