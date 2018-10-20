from pyspark import SparkContext
sc = SparkContext("local", "Collect app")
words = sc.parallelize (
   ["scala",
   "java",
   "hadoop",
   "spark",
   "akka",
   "spark vs hadoop",
   "pyspark",
   "pyspark and spark"]
)

coll = words.collect()
print("Elements in RDD: {}".format(coll))

words_filter = words.filter(lambda x: 'spark' in x)
filtered = words_filter.collect()
print('Filtered RDD -> %s' % (filtered))

words_map = words.map(lambda x: (x,1))
mapping = words_map.collect()
print("key value pair -> {}".format(mapping))
