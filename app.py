import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Load the trained model
model = load_model('brain_tumor_test.h5')

# Define class labels
labels = ['Glioma Tumor', 'Meningioma Tumor', 'No Tumor', 'Pituitary Tumor']

# Streamlit App Layout
st.set_page_config(page_title="Brain Tumor Classification", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
    .title {
        font-size: 32px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .sub-title {
        font-size: 18px;
        color: #555;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<p class="title">Brain Tumor Classification</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Upload an MRI scan to classify the type of brain tumor</p>', unsafe_allow_html=True)

# File Upload
uploaded_file = st.file_uploader("Upload an MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert image for OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    
    # Preprocess Image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img, (150, 150)) / 255.0
    img_array = img_resized.reshape(1, 150, 150, 3)

    # Create two columns: Image (left) & Chart (right)
    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(img, caption="Uploaded MRI Scan", width=300)

    # Predict Button
    if st.button("Classify Tumor"):
        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions)
        predicted_class = labels[predicted_index]
        confidence = round(100 * np.max(predictions), 2)

        # Display Results
        st.success(f"**Prediction:** {predicted_class}")
        st.info(f"**Confidence:** {confidence}%")

        # Show Confidence Distribution (Right Column)
        with col2:
            fig, ax = plt.subplots(figsize=(4, 3))  # Smaller chart size
            ax.barh(labels, predictions[0], color=["red", "blue", "green", "orange"])
            ax.set_xlim(0, 1)
            ax.set_xlabel("Confidence")
            ax.set_title("Prediction Confidence")
            plt.tight_layout()
            st.pyplot(fig)
