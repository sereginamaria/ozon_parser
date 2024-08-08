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


send_tshirts_dag = DAG(
    dag_id="send_tshirts_dag",
    start_date=datetime.datetime(2024, 8, 1),
    timetable=MultiCronTimetable(['0 10 * * tue', '0 18 * * thu', '0 14 * * sat'], timezone='Europe/Moscow', period_length=10, period_unit='minutes'),
)

PythonOperator(
    task_id="send_tshirts",
    python_callable=send_post,
    dag=send_tshirts_dag,
    op_kwargs={'category': 'Футболка'}
)
