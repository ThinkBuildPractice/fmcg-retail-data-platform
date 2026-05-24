gold_df = silver_df.groupBy(
    "review_score"
).count()

gold_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("lakehouse/gold")
