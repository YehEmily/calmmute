import os
import random
import urllib.request

import pandas as pd

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

yoga_poses = ["bridge-pose", "upward-facing-dog", "downward-facing-dog-pose", "hare-pose", "cat-pose", "right-triangle-pose", "easy-plow-pose", "half-moon-pose-left", "pigeon-pose-head-down-on-left-foot", "bound-angle-pose", "tree-pose-left-foot-in-front-of-thigh", "knee-press-both-legs", "garland-pose", "easy-forward-bend-pose-with-legs-half-bent", "left-twist-with-left-leg-bent", "bow-pose", "cow-pose", "upward-extended-feet-pose-with-support", "half-cobra-pose", "chair-pose"]

@app.route('/health')
def health():
    return 'ok'

@app.route('/', methods = ["POST"])
@app.route('/index.html', methods = ["POST"])
def home_page():
	info = pose_information(random_yoga_pose())
	return render_template('index.html', pose=info[0], description=info[1], video=info[2])

# @app.route('/about.html', methods=['GET','POST'])
# def about_page():
# 	return render_template('about.html')

def random_yoga_pose ():
	pose = random.randint(0, len(yoga_poses)-1)
	return yoga_poses[pose]

def pose_video (pose):
	page = urllib.request.urlopen("http://yoga.com/pose/" + pose).read().decode('utf-8')
	start = page.find("https://s3.amazonaws.com")
	end = page.find("mp4")
	
	return page[start:end+3]

def pose_information (pose):
	start = '"content"'
	end = '"cover_original"'
	page = urllib.request.urlopen("http://yoga.com/pose/" + pose).read().decode('utf-8')
	video = pose_video(pose)

	# Output: NAME, DESCRIPTION, VIDEO URL
	output = [' '.join(pose.split("-")).upper(), page[page.find(start)+11:page.find(end)-2], video]
	return output



if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', debug=True, port=port)
	# print(int(os.environ.get('HOME')))
	# app.run(debug=True)
