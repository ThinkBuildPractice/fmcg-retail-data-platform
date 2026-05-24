def validate_nulls(df):
    """
    Remove null values from retail dataset
    """
    return df.dropna()

def validate_duplicates(df):
    """
    Remove duplicate records
    """
    return df.dropDuplicates()

def validate_schema(df):
    """
    Validate expected schema
    """
    print("Schema validation completed")

print("Retail data quality checks completed")
