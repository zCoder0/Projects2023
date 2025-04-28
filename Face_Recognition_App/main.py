# main.py

import streamlit as st
from src.exception.ExceptionBase import ProjectException
from src.components.model.face_model import FaceRecognize
import cv2
import numpy as np
import sys
from PIL import Image

# Title
st.set_page_config(page_title="Face Recognition App", layout="centered")
st.title("🧠 Face Recognition System")

# Initialize face recognizer
face = FaceRecognize()

# Upload section
uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Convert uploaded image to proper format
        image = Image.open(uploaded_file).convert("RGB")
        image_np = np.array(image)
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        
        st.image(image, caption="📷 Uploaded Image", use_container_width=True)

        name = st.text_input("Enter Your Name", value="Prem Raj")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("📌 Register Face"):
                crop = face.face_detect(image_bgr, name=name)
                if crop is not None:
                    emb = face.face_embedding(crop)
                    face.save_datas()
                    st.success("✅ Face Registered Successfully")
                else:
                    st.warning("⚠️ No face detected.")

        with col2:
            if st.button("🔍 Recognize Face"):
                crop = face.face_detect(image_bgr, name="Test")
                if crop is not None:
                    test_embedding = face.face_embedding(crop)
                    known_faces_dict = face.load_knowfaces()
                    result = face.recognize_face(test_embedding, known_faces_dict)
                    st.success(f"✅ Recognized as: {result}")
                else:
                    st.warning("⚠️ No face detected.")

    except Exception as e:
        ProjectException(e, sys)
        st.error(f"❌ Error: {e}")

# Webcam toggle
st.markdown("---")
if st.checkbox("📹 Start Live Recognition (Webcam)"):
    st.warning("👀 Live webcam recognition runs in OpenCV window. Close it to return here.")
    face.live_face_recognition()
