from flask import Flask
import logging

app = Flask(__name__, template_folder='../card_creator/templates')

logger = logging.getLogger('Web-server')
logger.setLevel(logging.INFO)

