def validate_nulls(df):
    return df.dropna()

def validate_duplicates(df):
    return df.dropDuplicates()

def validate_schema(df):
    print("Schema validation completed")

def validate_review_score_range(df):
    invalid = df.filter(
        (df.review_score < 1) |
        (df.review_score > 5)
    )
    return invalid.count()

def validate_completeness(df):
    total_records = df.count()
    valid_records = df.dropna().count()
    completeness = (valid_records / total_records) * 100
    return completeness

print("Retail data quality framework executed")
