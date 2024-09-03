import pandas as pd

from fastapi import FastAPI
from fastapi import UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
#from face_rec.face_detection import annotate_face

import numpy as np
import cv2
import io

from ultralytics import YOLO


app = FastAPI()

def load_model():
    model = YOLO('models_weights/best.pt')
    return model

app.state.model = load_model()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"], ) # Allows all headers



# Define a root `/` endpoint
@app.get('/')

def index():
    return {
    'greeting': 'Hello'
    }


@app.post('/predict_image')
async def receive_image(img: UploadFile=File(...)):
    ### Receiving and decoding the image

    contents = await img.read()

    nparr = np.fromstring(contents, np.uint8)

    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray

    model = app.state.model

    prediction = model.predict(cv2_img, save=False, imgsz=640, vid_stride=1, conf=0.25)


    ### Do cool stuff with your image.... For example face detection
    ### Encoding and responding with the image
    #im = cv2.imencode('.png', cv2_img)[1] # extension depends on which format is sent from Streamlit
    #return Response(content=im.tobytes(), media_type="image/png")
    #return  Response(content=prediction.tobytes(), media_type="image/png")


    boxes = prediction[0].boxes


    prediction = {"classes":boxes.cls.numpy().tolist(), "confidence":boxes.conf.numpy().tolist(), "boxes":boxes.xyxy.numpy().tolist()}

    return prediction
