import os
import sys
import cv2
import numpy as np
import pandas as pd
from mtcnn import MTCNN
from sklearn.metrics.pairwise import cosine_similarity
from keras_facenet import FaceNet
from src.exception.ExceptionBase import ProjectException

# Disable OneDNN for better compatibility if needed
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

class FaceRecognize:

    def __init__(self):
        try:
            self.facenet = FaceNet()
            self.detector = MTCNN()
            self.known_faces = {}
            self.dataset_path = "src/components/dataset"
            os.makedirs(self.dataset_path, exist_ok=True)
            print("[INFO] Face Recognition Initialized")
        except Exception as e:
            raise ProjectException(e, sys)


    def face_detect(self, image, name="Face1"):
        try:
            img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            faces = self.detector.detect_faces(img_rgb)

            for face in faces:
                if 'box' in face:
                    x, y, w, h = face['box']
                    x, y = abs(x), abs(y)
                    face_crop = img_rgb[y:y + h, x:x + w]
                    crop = cv2.resize(face_crop, (160, 160))

                    self.name = name
                    return crop

            print("[WARNING] No face detected.")
            return None
        except Exception as e:
            raise ProjectException(e, sys)


    def face_embedding(self, crop_image):
        try:
            embedding = self.facenet.embeddings([crop_image])[0]
            self.known_faces[self.name] = embedding
            return embedding
        except Exception as e:
            raise ProjectException(e, sys)


    def save_datas(self):
        try:
            save_path = os.path.join(self.dataset_path, f"{self.name}.npy")
            np.save(save_path, self.known_faces[self.name])
            print(f"[INFO] Saved: {save_path}")
        except Exception as e:
            raise ProjectException(e, sys)


    def load_knowfaces(self):
        try:
            known_faces = {}
            for file in os.listdir(self.dataset_path):
                if file.endswith('.npy'):
                    name = file.replace(".npy", "")
                    data = np.load(os.path.join(self.dataset_path, file), allow_pickle=True)
                    known_faces[name] = data
            return known_faces
        except Exception as e:
            raise ProjectException(e, sys)


    def recognize_face(self, test_embedding, known_faces, threshold=0.6):
        try:
            identity = "Unknown"
            best_score = -1

            for name, saved_embedding in known_faces.items():
                score = cosine_similarity([test_embedding], [saved_embedding])[0][0]
                print(f"[DEBUG] Score with {name}: {score}")
                if score > best_score and score > threshold:
                    best_score = score
                    identity = name

            return identity
        except Exception as e:
            raise ProjectException(e, sys)


    def live_face_recognition(self):
        try:
            video = cv2.VideoCapture(0)
            known_faces = self.load_knowfaces()

            while True:
                ret, frame = video.read()
                if not ret:
                    print("[ERROR] Failed to grab frame.")
                    break

                crop = self.face_detect(frame)
                if crop is not None:
                    embedding = self.face_embedding(crop)
                    name = self.recognize_face(embedding, known_faces)
                    cv2.putText(frame, name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                cv2.imshow("Live Face Recognition", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            video.release()
            cv2.destroyAllWindows()

        except Exception as e:
            raise ProjectException(e, sys)
