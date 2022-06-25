from cProfile import run
from flask import Flask, render_template, request
from requests import request as req
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app,run('0.0.0.0')