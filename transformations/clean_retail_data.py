from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("Retail Data Processing") \
    .getOrCreate()

df = spark.read.csv(
    "order_score_prediction_1.csv",
    header=True,
    inferSchema=True
)

clean_df = df.dropDuplicates()

clean_df = clean_df.filter(col("review_score").isNotNull())

clean_df.write.mode("overwrite").parquet(
    "processed/clean_retail"
)

print("Retail data processed successfully")
