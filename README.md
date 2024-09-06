
# Mission

Adapt a pretrained model to assign the target of classifying processed trash to help separating into different containers.

## Model

From Ultralytics / model = YOLO("yolov9t.pt")


## Clasess

```
classes_dict = {

    0: "cardboard",
    1: "glass",
    2: "metal",
    3: "organic waste",
    4: "paper",
    5: "plastic"

    }
```

## Datasets

- [Roboflow: Trash Detection Computer Vision Project](https://universe.roboflow.com/image-processing-home-assignment/trash-detection-kfzaq)
Version v10 2024-01-21
Licence: CC 4.0

- Own generated dataset adapting to ower simulated conveyor belt
