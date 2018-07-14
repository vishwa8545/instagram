from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask('amazon')
app.secret_key = "secreatkey"

from amazon import api

