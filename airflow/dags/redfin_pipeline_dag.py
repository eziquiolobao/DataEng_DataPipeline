from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import os

# Import the ingestion function
import sys
# Add ../scripts (one directory up from /opt/airflow/dags) to PYTHONPATH
script_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
if script_dir not in sys.path:
    sys.path.append(script_dir)
from load_csv_to_snowflake import load_csv

default_args = {
    'owner': 'airflow',
}

dag = DAG(
    'house_sales_pipeline',
    default_args=default_args,
    description='Pipeline to load Redfin data into Snowflake and transform with dbt',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

ingest_task = PythonOperator(
    task_id='ingest_csv',
    python_callable=load_csv,
    op_kwargs={
        'account': os.getenv('SNOWFLAKE_ACCOUNT'),
        'user': os.getenv('SNOWFLAKE_USER'),
        'password': os.getenv('SNOWFLAKE_PASSWORD'),
        'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
        'database': os.getenv('SNOWFLAKE_DATABASE'),
        'schema': os.getenv('SNOWFLAKE_SCHEMA', 'PUBLIC'),
        'role': os.getenv('SNOWFLAKE_ROLE', 'SYSADMIN'),
        'csv_path': os.getenv('REDFIN_CSV_PATH'),
    },
    dag=dag,
)

dbt_task = BashOperator(
    task_id='dbt_run',
    bash_command='cd /opt/airflow/dbt && dbt run',
    dag=dag,
)

report_task = BashOperator(
    task_id='report',
    bash_command='echo "House sales pipeline finished"',
    dag=dag,
)

ingest_task >> dbt_task >> report_task
