
from flask import Flask
from utils import create_logger

app = Flask(__name__)

log = create_logger("Main", "main.log")

log.debug("App started")

import urls