import sys

from flask import Flask
import logging
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

logger = logging.getLogger('parser_web-server')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)



