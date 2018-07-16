from flask import Flask


app = Flask('insta')
app.secret_key = "secreatkey"




from insta import api

