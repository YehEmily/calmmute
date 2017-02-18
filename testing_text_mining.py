import random
import urllib

yoga_poses = ["bridge-pose", "upward-facing-dog", "downward-facing-dog-pose", "hare-pose", "cat-pose", "right-triangle-pose", "easy-plow-pose", "half-moon-pose-left", "pigeon-pose-head-down-on-left-foot", "bound-angle-pose", "tree-pose-left-foot-in-front-of-thigh", "knee-press-both-legs", "garland-pose", "easy-forward-bend-pose-with-legs-half-bent", "left-twist-with-left-leg-bent", "bow-pose", "cow-pose", "upward-extended-feet-pose-with-support", "half-cobra-pose", "chair-pose"]

def random_yoga_pose ():
	pose = random.randint(0, len(yoga_poses)-1)
	# print pose
	return yoga_poses[pose]

def pose_description (pose):
	start = '"content"'
	end = '"cover_original"'
	page = urllib.urlopen("http://yoga.com/pose/" + pose).read()
	video = pose_video(pose)
	output = [' '.join(pose.split("-")).upper(), page[page.find(start)+11:page.find(end)-2], video]
	print (output)
	# page[len(start):-len(end)]

def pose_video (pose):
	page = urllib.urlopen("http://yoga.com/pose/" + pose).read()
	start = page.find("https://s3.amazonaws.com")
	end = page.find("mp4")
	return page[start:end+3]



pose_description(random_yoga_pose())