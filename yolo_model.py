from ultralytics import YOLO
import numpy as np


def load_model(model_path="yolov8x-oiv7.pt"):
    # Load the YOLOv8x model from the local path
    model = YOLO(model_path)
    return model


def detect_components(image, model):
    image_array = np.array(image)

    results = model(image_array)
    names = model.names
    detected_items = set()
    for result in results:
        for cls in result.boxes.cls:
            detected_items.add(names[int(cls)])
    return list(detected_items)
