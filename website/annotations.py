import cv2
import numpy as np

import requests


#url = 'http://127.0.0.1:8000'
#prediction = requests.post(url + "/predict_image", files={'img': img_bytes})

classes_dict = {
    0: "cardboard",
    1: "glass",
    2: "metal",
    3: "organic waste",
    4: "paper",
    5: "plastic",
    6: "background"



    }





def create_image(original_image_array: np.array, prediction: dict) -> np.array:
    """
    Takes both:
    - The original image array
    - The result from the bounding boxes

    And returns an image with both elements in array format
    """
    # Create an OpenCV image from the numeric array
    opencv_image = cv2.cvtColor(original_image_array, cv2.COLOR_RGB2BGR)



    classes_dict = {
    0: "cardboard",
    1: "glass",
    2: "metal",
    3: "organic waste",
    4: "paper",
    5: "plastic",
    6: "background"

    }

    # Color to RGB
    colors_dict = {

    "blue": (35, 44, 126),
    "green": (47, 119, 63),
    "brown": (121, 85, 61),
    "yellow": (244, 239, 48),
    "default": (230,5,100)

    }

    # Annotate bounding boxes on the OpenCV image
    for index, coordinates in enumerate(prediction['boxes']):

        object_type = classes_dict[prediction["classes"][index]]
        probability = prediction["confidence"][index]

        coordinates = [int(coord) for coord in coordinates]

        #breakpoint()
        # Draw rectangle on the image
        cv2.rectangle(opencv_image, pt1=(coordinates[0], coordinates[1]), pt2=(coordinates[2], coordinates[3]), color=(0, 255, 0), thickness=4)

        text = f'{object_type} {round(probability, 2)}'

        # Calculate text size


        text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

        text_w, text_h = text_size



        # Add background
        #cv2.rectangle(opencv_image, (coordinates[0],coordinates[1]-5), (coordinates[0]+200,coordinates[1]-45), (230,5,100), -1)
        cv2.rectangle(opencv_image, (coordinates[0],coordinates[1]-40), (coordinates[0]+text_w,coordinates[1]+text_h-20), (230,5,100), -1)

        # Rectangle holding the text
        cv2.putText(opencv_image, text=text, org=(coordinates[0],coordinates[1]-10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255,255,255), thickness=1, lineType=cv2.LINE_AA)
        #cv2.rectangle(#### )

        # Rectangle holding the score
        #cv2.rectangle(#### )

        # Annotate with object type and probability
        #cv2.putText(#### )
        #cv2.putText(####)

    annotated_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)


    return annotated_image
