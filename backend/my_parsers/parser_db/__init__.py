import sys

import psycopg2 as pg
import logging

connection = pg.connect(
    host='10.0.0.1',
    database='masha',
    port=5433,
    user='masha',
    password='mashamasha01'
)

cursor = connection.cursor()

logger = logging.getLogger("db")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)