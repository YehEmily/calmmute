import os
import random
import urllib.request

import pandas as pd

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

yoga_poses = ["bridge-pose", "upward-facing-dog", "downward-facing-dog-pose", "hare-pose", "cat-pose", "right-triangle-pose", "easy-plow-pose", "half-moon-pose-left", "pigeon-pose-head-down-on-left-foot", "bound-angle-pose", "tree-pose-left-foot-in-front-of-thigh", "knee-press-both-legs", "garland-pose", "easy-forward-bend-pose-with-legs-half-bent", "left-twist-with-left-leg-bent", "bow-pose", "cow-pose", "upward-extended-feet-pose-with-support", "half-cobra-pose", "chair-pose", "low-lunge-right-leg-forward", "rotation-pose-legs-to-the-right", "downward-facing-dog-pose-right-leg-up", "warrior-pose-right-leg-bent", "reclining-bound-angle-pose", "upward-bow-pose", "crane-pose", "cobra-pose", "tree-pose-right-foot-in-front-of-thigh", "camel-pose-palms-set-against-feet", "bikram-triangle-left", "supported-shoulderstand-right-leg-behind-head", "left-leg-wind-freeing-pose", "easy-supported-shoulderstand-with-tilted-legs", "low-lunge-left-leg-forward", "half-boat-pose", "child-pose", "bikram-triangle-right", "perfect-pose", "half-moon-pose-right"]

@app.route('/health')
def health():
    return 'ok'

@app.route('/', methods = ["GET", "POST"])
@app.route('/#time', methods = ["GET", "POST"])
@app.route('/#feeling', methods = ["GET", "POST"])
@app.route('/index.html', methods = ["GET", "POST"])
@app.route('/index.html/#time', methods = ["GET", "POST"])
@app.route('/index.html/#feeling', methods = ["GET", "POST"])
def home_page():
	if request.method == "POST":
		if request.form["mood"]:
			print("Mood detected")
			save_feedback("mood_gauge.txt", request.form["mood"])
		if request.form["time"]:
			#do something
			print("Time detected")
	return render_template('index.html', mood_gauge=retrieve_feedback("mood_gauge.txt"))

@app.route('/time', methods = ["GET", "POST"])
@app.route('/time.html', methods=["GET", "POST"])
def time_page():
	return render_template("time.html")

@app.route('/calmmute', methods = ["GET", "POST"])
@app.route('/calmmute.html', methods = ["GET", "POST"])
def main_page():
	info = pose_information(random_yoga_pose())
	if request.method == "POST":
		if "rating" in request.form:
			save_feedback("feedback_records.txt", request.form["rating"])
	else:
		if "change_pose" in request.form:
			info = pose_information(random_yoga_pose())
	return render_template('calmmute.html', pose=info[0], description=info[1], video=info[2], feedback=retrieve_feedback("feedback_records.txt"))

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

def save_feedback (file_name, rating):
	t = open(file_name, "a+")
	t.write(str(rating) + "\n")
	t.close

def retrieve_feedback (file_name):
	t = open(file_name, "r+")
	unfiltered = t.read()
	filtered = unfiltered.split("\n")
	count = 0
	total = 0.0
	for i in filtered:
		if i != '':
			total += float(i)
			count += 1
	if ((total==0.0) & (count==0)):
		average=0.0
	else:
		average = total/count
	return average


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', debug=True, port=port)
	# print(int(os.environ.get('HOME')))
	# app.run(debug=True)
