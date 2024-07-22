import psycopg2 as pg
import logging

connection = pg.connect(
    host='195.133.32.87',
    database='masha',
    port=5433,
    user='masha',
    password='mashamasha01'
)

cursor = connection.cursor()

logger = logging.getLogger("db")
logger.setLevel(logging.INFO)