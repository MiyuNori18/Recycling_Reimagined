import streamlit as st
import datetime
import requests

'''
This is a first website draft.

'''

 # Set page tab display
st.set_page_config(
   page_title="Upload your Invoice",
   page_icon= '🧾',
   layout="wide",
   initial_sidebar_state="expanded",
)
# Example local Docker container URL
# url = 'http://api:8000'
# Example localhost development URL
url = 'http://localhost:8000'
# url = os.getenv('API_URL')

# App title and description
st.header('Simple Image Uploader 📸')

st.markdown("---")

### Create a native Streamlit file upload input
st.markdown("### Let's do a simple Invoice Extraction👇")
img_file_buffer = st.file_uploader('Upload an Invoice')


    with st.spinner("Wait for it..."):
      ### Get bytes from the file buffer
      img_bytes = img_file_buffer.getvalue()

      ### Make request to  API (stream=True to stream response as bytes)
      res = requests.post(url + "/upload_image", files={'img': img_bytes})

      if res.status_code == 200:
        ### Display the image returned by the API
        st.image(res.content, caption="Invoice Extracted ☝️")
      else:
        st.markdown("**Oops**, something went wrong 😓 Please try again.")
        print(res.status_code, res.content)

        '''
