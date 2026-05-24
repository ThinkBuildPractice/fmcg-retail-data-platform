from pyspark.sql.functions import col

silver_df = df.dropDuplicates()

silver_df = silver_df.filter(
    col("review_score").isNotNull()
)

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("lakehouse/silver")
