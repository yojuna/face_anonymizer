# README

Perform real time face detection and blurring over batches of images and video streams.
Useful for projects requiring deanonymization due to data privacy requirements.

Uses the 'face_recognition' library which is built on top of dlib.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Aknowledgements](#ackowledgements)
- [TODO's](#todo's)

## Installation / Setup

```sh
pip install opencv-python
pip install install face_recognition
```

## Usage

For deanonymizing faces in images, use ```blurer.py```
For applying to a video stream, use ```blurer_video.py```


```sh
for images:

$ python blurer.py --image example.jpg --method pixelated --blocks 30


for video stream:

$ python blurer_video.py --method pixelated --blocks 30
```

Arguments:
```
"-i", "--image", required=True, help="path to input image"
"-m", "--method", type=str, default="simple", choices=["simple", "pixelated"], help="face blurring/anonymizing method"
"-b", "--blocks", type=int, default=20, help="# of blocks for the pixelated blurring method"
```

## Acknowledgements

Adam Geitgey's face_recognition library https://github.com/ageitgey/face_recognition

## TODO's

1. optimise batch processing
