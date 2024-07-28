import os
import datetime as dt

import requests
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2020, 2, 11),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
    'depends_on_past': False,
}

def hello():
    print('hello')


with DAG(dag_id='test_dag', default_args=args, schedule_interval=None) as dag:
    say_hello = PythonOperator(
        task_id='hello',
        python_callable=hello,
        dag=dag
    )