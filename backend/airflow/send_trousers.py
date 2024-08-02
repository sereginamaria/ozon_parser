import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import timedelta
from typing import Optional
from pendulum import Date, DateTime, Time, timezone
from airflow.plugins_manager import AirflowPlugin
from airflow.timetables.base import DagRunInfo, DataInterval, TimeRestriction, Timetable
from airflow.timetables.events import EventsTimetable
from multiple_crons_timetable import MultiCronTimetable


def send_trousers(**kwargs):
    print('1')
    print('Hello from {kw}'.format(kw=kwargs['my_keyword']))
#     тут надо отправить запрос на /send_post и передать категорию и субкатегорию


send_trousers_dag = DAG(
    dag_id="send_trousers_dag",
    start_date=datetime.datetime(2024, 8, 1),
    timetable=MultiCronTimetable(['0 12 * * mon', '0 16 * * wed', '0 12 * * fri', '0 18 * * sat', '*/5 * * * *'], timezone='Europe/Moscow', period_length=10, period_unit='minutes'),
)

PythonOperator(
    task_id="parse_trousers",
    python_callable=send_trousers,
    dag=send_trousers_dag,
    op_kwargs={'my_keyword': 'Airflow'}


)

send_trousers_dag = DAG(
    dag_id="send_trousers_dag",
    start_date=datetime.datetime(2024, 8, 1),
    timetable=MultiCronTimetable(['0 12 * * mon', '0 16 * * wed', '0 12 * * fri', '0 18 * * sat', '*/5 * * * *'], timezone='Europe/Moscow', period_length=10, period_unit='minutes'),
)

PythonOperator(
    task_id="parse_trousers",
    python_callable=send_trousers,
    dag=send_trousers_dag,
    op_kwargs={'my_keyword': 'Airflow'}


)