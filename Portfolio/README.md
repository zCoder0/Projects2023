# Portfolio Analytics Dashboard

Welcome to the **Portfolio Analytics Dashboard**! 🚀 This project is a **Streamlit-based web application** that provides an **interactive portfolio visualization**, allowing users to explore **skills, education, and locations** dynamically.

## 📌 Features
- 📊 **Portfolio Dashboard**: Interactive UI to showcase skills, education, and work locations.
- 🔥 **Skills Heatmap**: Visualize programming proficiency using a heatmap.
- 📚 **Education Overview**: Displays academic performance via data visualizations.
- 🌍 **Location Tracking**: Uses Folium to display work and home locations on a map.
- 💬 **AI Chatbot**: Ask questions about the portfolio with an AI-powered chatbot.

---
## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/zCoder0/Projects/portfolio.git
cd portfolio
```

### 2️⃣ Create & Activate Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```sh
streamlit run index.py
```

---
## 🔧 Project Structure
```
📂 portfolio-dashboard/
│── 📄 index.py                  # Main Streamlit app
│── 📄 load_datas.py              # Data loading module
│── 📄 project_structure.py       # Project setup file
│── 📄 requirements.txt           # Dependencies
│── 📄 setup.py                   # Setup script
│── 📄 dashboard_data.json        # Sample data
│── 📂 src/                       # Source code
│   ├── 📂 components/            # Core components
│   │   ├── model.py              # AI Chatbot model
│   │   ├── preprocessing.py      # Data preprocessing
│   │   ├── __init__.py
│   ├── 📂 data_set/               # Data storage
│   ├── 📂 exception/              # Custom exceptions
│   ├── 📂 logger/                 # Logging utilities
│── 📂 faiss-lib/                  # Vector database (Important!)
│── 📄 .env                        # API keys (Keep it secret)
```

---
## 🌐 Deployment (Free Hosting)

### 1️⃣ Create a `Procfile` (for Railway or Heroku)
```
web: streamlit run index.py --server.port $PORT
```

### 2️⃣ Deploy on **Railway** (Recommended Free Option)
1. Push code to GitHub.
2. Create a new Railway project.
3. Connect GitHub repository.
4. Add **Environment Variables**:
   - `PORT = 8080`
   - `API_KEY = your_api_key`
5. Deploy & Get Live Link!

---
## 📜 License
This project is licensed under the **MIT License**.

---
## 👨‍💻 Author
**Prem Raj**  
📧 Email: [rajp37590@gmail.com](mailto:rajp37590@gmail.com)  
🔗 LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/prem-raj-sivakumar-998aa628a/)  

