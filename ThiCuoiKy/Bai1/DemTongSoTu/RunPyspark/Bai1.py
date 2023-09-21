from pyspark.sql import SparkSession
from operator import itemgetter

spark = SparkSession.builder.appName("WordCountdemtongsotu").getOrCreate()
lines = spark.read.text("/home/hdoop/Downloads/gutenberg/*.txt").rdd.map(lambda r: r[0])

counts = (
    lines
    .flatMap(lambda x: x.split())
    .map(lambda word: (word, 1))
    .reduceByKey(lambda x, y: x + y)
)

count_all_word = counts.values().sum()

print(f"Tong So Tu La: {count_all_word}")

spark.stop()
