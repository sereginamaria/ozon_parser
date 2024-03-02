from flask import Flask
import logging
import sys

app = Flask(__name__, template_folder='../card_creator/templates')

logger = logging.getLogger("parser")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

