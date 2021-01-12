from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import Form
import logging

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)
#miggrgate = Migrate(app, db, render_as_batch=True)
logging.basicConfig(filename='example.log', level=logging.DEBUG)

from app import views, models
