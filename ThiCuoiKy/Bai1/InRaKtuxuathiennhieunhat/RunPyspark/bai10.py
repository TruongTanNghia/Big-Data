import os, shutil
from pyspark import SparkContext


# create Spark context with necessary configuration
sc = SparkContext("local", "Text processing with PySpark Example")

# read data from text file into lines  
lines = sc.textFile("/home/hdoop/Downloads/Big-Data-main/Lab3_NCDC_WeatherData/data/preprocessed")

# Tách các dòng ra thành mảng các từ vựng
# Bài trước chưa dùng lệnh này
words = lines.flatMap(lambda line: line.split(" "))

# Đếm số lần xuất hiện, tuple là ngoặc tròn 1 cặp từ,1 
# reduce là gộp lại theo key, key là từ vựng   ('thien',1) thien là key ('thien',1)
wordFrequencies = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
# ascending=false: phủ định của tăng dần là sắp xếp giảm dần
# sắp xếp lại kết quả đo được bằng lệnh sory by x[0]= thien, x[1]= 1 con số chỉ tần xuất xuất hiện từ đó
wordFrequencies = wordFrequencies.sortBy(lambda x: x[1],ascending=False).take(20)

# def g(x):
#     print(x)
# wordFrequencies.foreach(g)
# print(type(wordFrequencies))
print(wordFrequencies)

# # save the set of <word, frequency> to disk
# savingPath = "/home/hdoop/pyspark-output"

# if os.path.isdir(savingPath):
#     shutil.rmtree(savingPath, ignore_errors=True)
# wordFrequencies.saveAsTextFile(savingPath)
