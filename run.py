from flask import Flask, send_from_directory,request,jsonify
from flask_bootstrap import Bootstrap
from amazon import app





if __name__ == '__main__':
    app.run(host ='0.0.0.0' ,port =5000)