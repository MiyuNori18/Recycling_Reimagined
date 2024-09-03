import cv2
import numpy as np

import requests


#url = 'http://127.0.0.1:8000'
#prediction = requests.post(url + "/predict_image", files={'img': img_bytes})

def create_image(original_image_array: np.array, bound_boxes: dict) -> np.array:
    """
    Takes both:
    - The original image array
    - The result from the bounding boxes

    And returns an image with both elements in array format
    """
    # Create an OpenCV image from the numeric array
    opencv_image = cv2.cvtColor(original_image_array, cv2.COLOR_RGB2BGR)

    # Annotate bounding boxes on the OpenCV image
    for box_info in bound_boxes:
        coordinates = box_info
        #object_type = box_info["classes"]
        #probability = box_info["confidence"]

        coordinates = [int(coord) for coord in coordinates]

        #breakpoint()
        # Draw rectangle on the image
        cv2.rectangle(opencv_image, pt1=(coordinates[0], coordinates[1]), pt2=(coordinates[2], coordinates[3]), color=(0, 255, 0), thickness=3)

        # Rectangle holding the text
        #cv2.rectangle(#### )

        # Rectangle holding the score
        #cv2.rectangle(#### )

        # Annotate with object type and probability
        #cv2.putText(#### )
        #cv2.putText(####)

    annotated_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)


    return annotated_image
