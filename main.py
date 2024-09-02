
from api.fast import app
from fastapi import FastAPI

from ultralytics import YOLO

'''
vid_stride	int	1	Frame stride for video inputs. Allows skipping frames in videos to speed up processing at the cost of temporal resolution. A value of 1 processes every frame, higher values skip frames.
imgsz	int or tuple	640	Defines the image size for inference. Can be a single integer 640 for square resizing or a (height, width) tuple. Proper sizing can improve detection accuracy and processing speed.
conf	float	0.25	Sets the minimum confidence threshold for detections. Objects detected with confidence below this threshold will be disregarded. Adjusting this value can help reduce false positives.
'''

model("/Users/antonwenemoser/code/MiyuNori18/Recycling_Reimagined/models_weights/best.pt")
