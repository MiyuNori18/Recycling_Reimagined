

import av
import cv2
import requests
import streamlit as st
from annotations import create_image
from streamlit_webrtc import RTCConfiguration, webrtc_streamer

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)


def video_frame_callback(frame):

    format = "bgr24"
    img = frame.to_ndarray(format=format)

    _, encoded_image = cv2.imencode(".jpg", img)
    img_bytes = encoded_image.tobytes()

    url = 'http://34.116.206.113:8000'

    res = requests.post(url + "/predict_image", files={'img': img_bytes})

    prediction = res.json()

    created_image = create_image(img, prediction)  # Assuming create_image is defined somewhere

    return av.VideoFrame.from_ndarray(created_image, format=format)


webrtc_streamer(
    key="example",
    video_frame_callback=video_frame_callback,
    rtc_configuration=RTC_CONFIGURATION,
)
