from flask import Flask
from model import connect_to_db
import os

app = Flask(__name__)