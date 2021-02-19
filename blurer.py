# import the necessary packages
from face_blur_static import anonymize_face_pixelate
from face_blur_static import anonymize_face_simple
from face_location import get_face_positions
import numpy as np
import argparse
import cv2
import os

# construct the argument parse and parse the arguments

#--image: The path to your input image containing faces
#--face: The path to your face detector model directory
#--method: Either the simple blurring or pixelated
#          methods can be chosen with this flag. 
#          The simple method is the default
#--blocks: For pixelated face anonymity, you must provide 
#          the number of blocks you want to use, or you can 
#          keep the default of 20
#--confidence: The minimum probability to filter weak face 
#              detections is set to 50% by default
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
    help="path to input image")
# ap.add_argument("-f", "--face", required=True, 
#     help="path to face detector model directory")
ap.add_argument("-m", "--method", type=str, default="simple",
    choices=["simple", "pixelated"],
    help="face blurring/anonymizing method")
ap.add_argument("-b", "--blocks", type=int, default=20,
    help="# of blocks for the pixelated blurring method")
args = vars(ap.parse_args())

# load our serialized face detector model from disk
# load the input image from disk, clone it, and grab the image spatial
# dimensions
image = cv2.imread(args["image"])
orig = image.copy()

# using the face_recongnition library
# to get the positions of the detected faces
face_positions_list = get_face_positions(args["image"])

for face_position in face_positions_list:
	# check face blurring method
	if args["method"] == "simple":
		face = anonymize_face_simple(face, factor=3.0)
	# otherwise, we must be applying the "pixelated" face
	# anonymization method
	else:
		face = anonymize_face_pixelate(face,
			blocks=args["blocks"])

	# get the face position values
	startY, endX, endY, startX = face_position	

	# store the blurred face in the output image
	image[startY:endY, startX:endX] = face

	# # display the original image and the output image with the blurred
	# # face(s) side by side
	# output = np.hstack([orig, image])
	# cv2.imshow("Output", output)
	# cv2.waitKey(0)

