import streamlit as st
from yolo_model import load_model, detect_components
from utils import load_image

st.title("Object Detection")


@st.cache_resource
def get_model(coco=False):
    if coco:
        model_path = "yolov10x.pt"
    else:
        model_path = "yolov8x-oiv7.pt"
    return load_model(model_path)


uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png", "webp"]
)

if uploaded_file is not None:
    try:
        image = load_image(uploaded_file)
        st.image(
            uploaded_file, caption="Uploaded Image.", use_column_width=False, width=500
        )

        if st.button("Analyze Image"):
            with st.spinner("Analyzing..."):
                model_coco = get_model(True)
                detected_items_coco = detect_components(image, model_coco)
                model_open = get_model(False)
                detected_items_open = detect_components(image, model_open)
                len_coco, len_open = len(detected_items_coco), len(detected_items_open)
                if len_coco > len_open and len_coco > 0:
                    st.success("Detected components in the image:")
                    st.write(", ".join(detected_items_coco))
                elif len_open > 0:
                    st.success("Detected components in the image:")
                    st.write(", ".join(detected_items_open))
                else:
                    st.warning("No components detected.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload an image file to start the analysis.")
