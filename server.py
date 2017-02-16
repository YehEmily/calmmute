import os
import spotipy

import pandas as pd
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/health')
def health():
    return 'ok'

@app.route('/')
@app.route('/index.html')
def home_page():
    return render_template('index.html')

@app.route('/about.html')
def about_page():
	return render_template('about.html')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', debug=True, port=port)
	# print(int(os.environ.get('HOME')))
	# app.run(debug=True)