from gc import collect
import os, shutil
from pyspark import SparkContext
import re
import sys
sc = SparkContext("local", "Text processing with PySpark Example")

(date_when_max_temp,max_temp) = (None,-sys.maxsize)
(date_when_min_temp,min_temp) = (None,sys.maxsize)
(current_date, last_year) = (None,None)
(lines_count, temps_sum) = (0, 0)
lines = sc.textFile("/home/hdoop/Downloads/Big-Data-main/Lab3_NCDC_WeatherData/data/preprocessed/*.txt").cache()
for line in lines.collect():
    year = line[15:19]
    date = line[15:23]
    temp = line[87:92]
    q = line[92:93]
    
    if last_year != None and last_year != year:
         avg_temp = temps_sum / lines_count
         print("%s\t%s\t%s\t%s" % (last_year, max_temp, min_temp, avg_temp))
         (last_year, max_temp, min_temp) = (year, int(temp), int(temp))
         (date_when_max_temp, date_when_min_temp) = (date, date)
         (lines_count, temps_sum) = (1, int(temp))
    else:
        last_year = year
        temp_integer = int(temp)
        if (temp_integer > max_temp and (temp != "+9999" and re.match("[01459]",q))):
            max_temp = temp_integer
            date_when_max_temp = date
        if (temp_integer < min_temp and (temp != "+9999" and re.match("[01459]",q))):
            min_temp = temp_integer
            date_when_min_temp = date
        if (temp != "+9999" and re.match("[01459]",q)):
            lines_count += 1
            temps_sum += temp_integer
            
if last_year:
    avg_temp = temps_sum / lines_count
    print("%s\t%s\t%s\t%s" % (last_year, max_temp, min_temp, avg_temp))
    
