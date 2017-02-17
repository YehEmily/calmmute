import os

import pandas as pd

from flask import Flask, redirect, render_template, request, url_for
import audiosearch

app = Flask(__name__)

#audiosearch clinet
#client=Client("f8700011bc7fc583fe4e1aa40ce8989c4d6d88b176a875046f1d96b3f9d74519", "15b0ee547a4faf02bc09f268486a88f2ef9f0710044c2a679a8cebecb04186f2")
#show = client.get_show(1161)
print(show)

@app.route('/health')
def health():
    return 'ok'

@app.route('/')
@app.route('/index.html')
def home_page():
    return render_template('index.html')

@app.route('/about.html', methods=['GET','POST'])
def about_page():
	return render_template('about.html')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', debug=True, port=port)
	# print(int(os.environ.get('HOME')))
	# app.run(debug=True)
