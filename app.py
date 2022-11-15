from random import randrange
from flask import Flask, render_template, request
import hashlib
#import controlador
from datetime import datetime
#import envio_correo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    #hola