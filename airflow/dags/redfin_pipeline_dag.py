from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import os

# Import the ingestion function
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'scripts'))
from load_csv_to_postgres import load_csv

default_args = {
    'owner': 'airflow',
}

dag = DAG(
    'redfin_data_pipeline',
    default_args=default_args,
    description='Pipeline to load Redfin data and transform with dbt',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

ingest_task = PythonOperator(
    task_id='ingest_csv',
    python_callable=load_csv,
    dag=dag,
)

dbt_task = BashOperator(
    task_id='dbt_run',
    bash_command='cd /opt/airflow/dbt && dbt run',
    dag=dag,
)

report_task = BashOperator(
    task_id='report',
    bash_command='echo "Redfin pipeline finished"',
    dag=dag,
)

ingest_task >> dbt_task >> report_task
