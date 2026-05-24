from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Bronze Layer").getOrCreate()

df = spark.read.csv(
    "order_score_prediction_1.csv",
    header=True,
    inferSchema=True
)

df.write.mode("overwrite").parquet("bronze/orders")
