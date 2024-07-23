# Object Detection with YOLOv8

This project demonstrates an advanced object detection application utilizing the YOLOv8 model. It features a Streamlit-based web interface, allowing users to upload images and receive detailed object detection results. The application supports object detection using both the COCO and Open Images V7 datasets, providing robust and versatile performance.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Model](#model)
- [Links](#links)

## Features

- **Streamlit Integration**: Interactive and user-friendly web interface for easy image uploads and real-time analysis.
- **Dual Dataset Support**: Detect objects using either COCO or Open Images V7 datasets, enhancing detection versatility.
- **High Efficiency**: Utilizes the YOLOv8 model for fast and accurate object detection.
- **Automatic Image Conversion**: Ensures uploaded images are in the correct format for analysis, enhancing compatibility.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/HalemoGPA/slash_ai_task.git
    cd slash_ai_task
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## Usage

To use the application, visit the [Streamlit App](https://gobject.streamlit.app/).

1. **Upload an image file** using the file uploader.
2. **Click the "Analyze Image" button** to start the object detection process.
3. **View the detected components** displayed below the uploaded image.

## Files

- **app.py**: The main application file containing the Streamlit interface.
- **utils.py**: Utility functions for image processing.
- **yolo_model.py**: Functions for loading the YOLO model and detecting objects.

## Model

The project employs the YOLOv8 model for object detection. Depending on the user's choice, it can load either:
- `yolov8l.pt` for COCO dataset.
- `yolov8l-oiv7.pt` for Open Images V7 dataset.


## Links

- **Streamlit Application**: [Object Detection App](https://gobject.streamlit.app/)
