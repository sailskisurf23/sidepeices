from pyspark import SparkContext
logFile = "sidepeices/log.txt"
sc = SparkContext("local", "first spark app")
logData = sc.textFile(logFile).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
print("Lines with a: {}, lines with b: {}".format(numAs,numBs))
