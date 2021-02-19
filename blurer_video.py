# import the necessary packages
from face_blur_static import anonymize_face_pixelate, anonymize_face_simple
import face_recognition
import numpy as np
import argparse
import time
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--method", type=str, default="simple",
	choices=["simple", "pixelated"],
	help="face blurring/anonymizing method")
ap.add_argument("-b", "--blocks", type=int, default=20,
	help="# of blocks for the pixelated blurring method")
args = vars(ap.parse_args())


# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
video_capture = cv2.VideoCapture(0)
time.sleep(2.0)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    # face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
	# if a face is detected and the array is not null
	if face_locations:
		# loop over the detections
		for face_location in face_locations:
			top, right, bottom, left = face_location
			face = frame[top:bottom, left:right]

			# check to see if we are applying the "simple" face
			# blurring method
			if args["method"] == "simple":
				face = anonymize_face_simple(face, factor=3.0)
			# otherwise, we must be applying the "pixelated" face
			# anonymization method
			else:
				face = anonymize_face_pixelate(face,
					blocks=args["blocks"])

			# store the blurred face in the output image
			frame[startY:endY, startX:endX] = face


	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break	

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()