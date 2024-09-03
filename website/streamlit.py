import streamlit as st
from PIL import Image
import requests

# Set page tab display
st.set_page_config(
   page_title="Simple Image Uploader",
   page_icon= '🖼️',
   layout="wide",
   initial_sidebar_state="expanded",
)

url = 'http://127.0.0.1:8000'


### Create a native Streamlit file upload input
st.markdown("### Let's do a simple face recognition 👇")
img_file_buffer = st.file_uploader('Upload an image')

if img_file_buffer is not None:

  col1, col2 = st.columns(2)

  with col1:
    ### Display the image user uploaded
    st.image(Image.open(img_file_buffer), caption="Here's the image you uploaded ☝️")

#   with col2:
#     with st.spinner("Wait for it..."):
#       ### Get bytes from the file buffer
#       img_bytes = img_file_buffer.getvalue()

#       ### Make request to  API (stream=True to stream response as bytes)
#       res = requests.post(url + "/predict_image", files={'img': img_bytes})

#       if res.status_code == 200:
#         ### Display the image returned by the API
#         st.write(res.json())
#         #st.image(res.content, caption="Image returned from API ☝️")
#       else:
#         st.markdown("**Oops**, something went wrong 😓 Please try again.")
#         print(res.status_code, res.content)
