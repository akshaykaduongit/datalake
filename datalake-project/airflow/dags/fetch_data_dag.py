from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from src.data_fetchers.fetch_from_api import fetch_data_from_api
from src.data_fetchers.fetch_from_db import fetch_data_from_db
from src.data_fetchers.fetch_from_file import fetch_data_from_file

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('fetch_data_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    fetch_api_data = PythonOperator(
        task_id='fetch_api_data',
        python_callable=fetch_data_from_api,
    )

    fetch_db_data = PythonOperator(
        task_id='fetch_db_data',
        python_callable=fetch_data_from_db,
    )

    fetch_file_data = PythonOperator(
        task_id='fetch_file_data',
        python_callable=fetch_data_from_file,
    )

    fetch_api_data >> fetch_db_data >> fetch_file_data