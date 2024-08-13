# import datetime
#
# import requests
# from airflow import DAG
# from airflow.operators.python import PythonOperator
#
# from datetime import timedelta
# from typing import Optional
# from pendulum import Date, DateTime, Time, timezone
# from airflow.plugins_manager import AirflowPlugin
# from airflow.timetables.base import DagRunInfo, DataInterval, TimeRestriction, Timetable
# from airflow.timetables.events import EventsTimetable
# from multiple_crons_timetable import MultiCronTimetable
# from db import db
# from ozon_parser import schema
# from telegram import telegram_notifier
#
# def check_availability_of_products():
#     list = db.count_of_categories()
#
#     inf_mess = 'На ближайшие 14 дней:'
#
#     for el in list:
#         if el[0] == 'Брюки' and el[1] < 24 * 2:
#             inf_mess += '\n Брюки - нужно ' + str(24*2 - el[1])
#
#     telegram_notifier.availability_of_products(inf_mess)
#
#
#
# check_availability_of_products_dag = DAG(
#     dag_id="check_availability_of_products_dag",
#     start_date=datetime.datetime(2024, 8, 1),
#     timetable=MultiCronTimetable(['0 6 * * *'], timezone='Europe/Moscow', period_length=10, period_unit='minutes'),
# )
#
# PythonOperator(
#     task_id="send_corset",
#     python_callable=check_availability_of_products,
#     dag=check_availability_of_products_dag
# )
