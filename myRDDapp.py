from pyspark import SparkContext

# class pyspark.RDD(
#     jrdd,
#     ctx,
#     drdd_deserializer = AutoBatchedSerializer(pickleSerializer())
# )

sc = SparkContext("local", "count app")
words = sc.parallelize(
    ["scala",
   "java",
   "hadoop",
   "spark",
   "akka",
   "spark vs hadoop",
   "pyspark",
   "pyspark and spark"]
)

counts = words.count()
print("Number of elements in RDD: {}".format(counts))
