#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math
import os
from moviepy.editor import VideoFileClip

from laneMarker import laneMarker

lm = laneMarker()
############################ Test Images ############################

test_dir = "test_images/"
test_images = os.listdir(test_dir)
for test_image in test_images:
	image = mpimg.imread(test_dir+test_image)
	img = lm.process_image(image)
	plt.imshow(img)
	figManager = plt.get_current_fig_manager()
	figManager.window.showMaximized()
	plt.show()

############################ Test videos ############################

white_output = 'solidWhiteRight_out.mp4'
clip1 = VideoFileClip("solidWhiteRight.mp4")
white_clip = clip1.fl_image(lm.process_image)
white_clip.write_videofile(white_output, audio=False)

yellow_output = 'solidYellowLeft_out.mp4'
clip2 = VideoFileClip('solidYellowLeft.mp4')
yellow_clip = clip2.fl_image(lm.process_image)
yellow_clip.write_videofile(yellow_output, audio=False)

challenge_output = 'challenge_out.mp4'
clip2 = VideoFileClip('challenge.mp4')
challenge_clip = clip2.fl_image(lm.process_image)
challenge_clip.write_videofile(challenge_output, audio=False)
