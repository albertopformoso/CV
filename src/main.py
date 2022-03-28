import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, url_for

app = Flask(__name__)

# if len(find_dotenv()) == 0:
#     raise RuntimeError("Can't find your .env file")

load_dotenv(find_dotenv())

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# BLUEPRINTS
from src.error_pages.handlers import error_pages
from src.core.views import core

app.register_blueprint(error_pages)
app.register_blueprint(core)
