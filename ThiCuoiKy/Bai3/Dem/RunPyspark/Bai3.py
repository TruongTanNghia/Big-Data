from pyspark import SparkContext

sc = SparkContext(appName="LinkCount")
lines = sc.textFile("/home/hdoop/Downloads/Data-3")

counts = (
    lines
    .map(lambda line: line.strip().split('\t'))
    .map(lambda x: (x[1], 1))
    .reduceByKey(lambda x, y: x + y)
)

for (node, count) in counts.collect():
    print(f"{node}\t{count}")
