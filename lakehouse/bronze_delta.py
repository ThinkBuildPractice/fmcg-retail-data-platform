from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Bronze Delta Layer") \
    .getOrCreate()

df = spark.read.csv(
    "order_score_prediction_1.csv",
    header=True,
    inferSchema=True
)

df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("lakehouse/bronze")
