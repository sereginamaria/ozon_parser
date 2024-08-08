import datetime

import requests
from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import timedelta
from typing import Optional
from pendulum import Date, DateTime, Time, timezone
from airflow.plugins_manager import AirflowPlugin
from airflow.timetables.base import DagRunInfo, DataInterval, TimeRestriction, Timetable
from airflow.timetables.events import EventsTimetable
from multiple_crons_timetable import MultiCronTimetable

from airflow import send_post


send_accessories_dag = DAG(
    dag_id="send_accessories_dag",
    start_date=datetime.datetime(2024, 8, 1),
    timetable=MultiCronTimetable(['0 6 * * tue', '0 6 * * thu'], timezone='Europe/Moscow', period_length=10, period_unit='minutes'),
)

PythonOperator(
    task_id="send_accessories",
    python_callable=send_post,
    dag=send_accessories_dag,
    op_kwargs={'category': 'Аксессуары'}
)
