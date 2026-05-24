gold_df = clean_df.groupBy(
    "review_score"
).count()

gold_df.write.mode("overwrite").parquet(
    "gold/customer_satisfaction"
)
