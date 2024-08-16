import sys

from flask import Flask
import logging
from flask_cors import CORS

app = Flask(__name__, template_folder='../card_creator/templates')
CORS(app)

logger = logging.getLogger('web-server')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)


