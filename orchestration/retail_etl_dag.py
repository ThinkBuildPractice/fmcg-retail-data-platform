from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def bronze_ingestion():
    print("Ingesting raw retail dataset")

def silver_transformation():
    print("Cleaning and transforming retail data")

def gold_analytics():
    print("Generating business analytics layer")

with DAG(
    dag_id="retail_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    bronze_task = PythonOperator(
        task_id="bronze_ingestion",
        python_callable=bronze_ingestion
    )

    silver_task = PythonOperator(
        task_id="silver_transformation",
        python_callable=silver_transformation
    )

    gold_task = PythonOperator(
        task_id="gold_analytics",
        python_callable=gold_analytics
    )

    bronze_task >> silver_task >> gold_task
