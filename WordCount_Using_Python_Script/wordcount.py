from pyspark import SparkContext, SparkConf
conf=SparkConf().setAppName("Priyansh_word_Count")
import logging
s_logger =logging.getLogger('py4j.java_gateway')
s_logger.setLevel(logging.ERROR)
sc=SparkContext(conf=conf)
text_file =sc.textFile("Word.txt")
counts =text_file.flatMap(lambda line :line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a,b: a+b)
for word in counts.collect():
    print(word)
#counts.save.AsTextFile()
sc.stop()    
