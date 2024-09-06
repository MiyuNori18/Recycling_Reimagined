import streamlit as st
from PIL import Image
import requests
import numpy as np

#local
from annotations import create_image

# Set page tab display
st.set_page_config(
   page_title="Image Recognition",
   page_icon= '♻️',
   layout="wide",
   initial_sidebar_state="expanded",
)

url = 'http://34.116.206.113:8000'

###Header
st.header('Recycling Reimagined!♻️')
st.markdown("---")


### Create a native Streamlit file upload input
st.markdown("### Attach an image to scan it👇")
img_file_buffer = st.file_uploader('Upload image')



if img_file_buffer is not None:

  col1, col2 = st.columns(2)

  with col1:
    ### Display the image user uploaded
    pil_image =Image.open(img_file_buffer)
    np_image = np.array(pil_image)
    st.image(pil_image, caption="Here's the image you uploaded ☝️")

  with col2:
     with st.spinner("Computing..."):
       ### Get bytes from the file buffer
       img_bytes = img_file_buffer.getvalue()

       ### Make request to  API (stream=True to stream response as bytes)
       res = requests.post(url + "/predict_image", files={'img': img_bytes})
       print(res)

       if res.status_code == 200:
         ### Display the image returned by the API
         st.write(res.json())

         prediction = res.json()


         image = create_image(np_image, prediction)

         st.image(image)
       else:
         st.markdown("**Oops**, something went wrong 😓 Please try again. ♻️")
         print(res.status_code, res.content)
