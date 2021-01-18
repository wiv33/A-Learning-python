from pyspark import SparkContext, SparkConf
from pyspark.streaming.context import StreamingContext

conf = SparkConf()
sc = SparkContext(master='local[*]', appName='StreamingSample', conf=conf)
scc = StreamingContext(sc, 3)

rdd = sc.paralleize(['Spark Streaming First Example scc'])
rdd2 = sc.paralleize(['Spark Queue Example API is good'])

inputQueue = [rdd, rdd2]

lines = scc.queueStream(inputQueue, True)
words = lines.flatMap(lambda x: x.split(" "))

words.countByValue().pprint()


scc.start()
scc.awaitTermination()
