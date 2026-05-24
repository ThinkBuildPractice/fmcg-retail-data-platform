from pyspark.sql.functions import col

clean_df = df.dropDuplicates()

clean_df = clean_df.filter(
    col("review_score").isNotNull()
)

clean_df.write.mode("overwrite").parquet(
    "silver/orders_clean"
)
