from flask import Flask

app = Flask(__name__)

from app import routes  # If you have routes.py