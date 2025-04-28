# 🧠 Face Recognition System

A real-time Face Recognition system built using **Streamlit**, **FaceNet**, and **MTCNN**. This application allows users to register their face and recognize it later using facial embeddings and cosine similarity.

---

## 🚀 Features

- ✅ Register faces with a name
- 🔍 Recognize uploaded or live webcam faces
- 🖼️ Crop and embed faces using FaceNet
- 🎯 Real-time face detection using MTCNN
- 🖥️ Simple web UI using Streamlit

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```
- python 3.11
- numpy 
- keras
- keras_facenet
- scikit_learn
- pandas
- opencv-python
- mtcnn
- tensorflow
- streamlit
- pillow

# 1. Clone the Repository
```bash
git clone https://github.com/your-username/face-recognition-app.git
cd face-recognition-app
```

# 2. Clone the Repository
```bash
streamlit run main.py
```

# 🧬 How It Works
- **Face Detection:** Uses MTCNN to detect faces from images.

- **Face Embedding:** Uses pre-trained FaceNet to convert face into a 128-D embedding.

- **Recognition:** Uses cosine similarity to compare face embeddings with stored known faces.

- **Dataset:** All registered faces are stored as .npy files in src/components/dataset

# 📁 Project Structure

```bash
.
├── main.py
├── README.md
├── requirements.txt
├── src
│   ├── components
│   │   ├── model
│   │   │   └── face_model.py
│   │   └── dataset
│   └── exception
│       └── ExceptionBase.py
```

# 📌 Notes
- Press q to quit webcam-based recognition.

- You can add confidence thresholds or multiple face matching logic easily.

- Improve accuracy by capturing multiple embeddings per user.


# 👨‍💻 Author
**Prem Raj**
📧 rajp37590@gmail.com
🔗  [LinkedIn](https://www.linkedin.com/in/prem-raj-sivakumar-998aa628a/)
