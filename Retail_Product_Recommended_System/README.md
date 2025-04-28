# Retail Recommendation System

## 📌 Project Overview
This project is a **Retail Recommendation System** that analyzes customer purchase history and recommends products using **Collaborative Filtering**. It processes a retail dataset and predicts the most relevant products for customers based on their purchase patterns.

## 🚀 Features
- **Data Processing**: Reads and cleans retail transaction data.
- **Collaborative Filtering**: Uses a trained model to predict customer preferences.
- **Product Recommendation**: Suggests top 10 products for a given customer.

## 📂 Project Structure
```
Retail-Recommendation-System/
│── src/
│   ├── components/
│   │   ├── dataset/
│   │   │   ├── OnlineRetail.xlsx  # Raw Dataset
│   │   │   ├── clean_dataset.csv  # Processed Data
│   │   │   ├── clean_df.csv       # Data for Model
│   │   ├── model/
│   │   │   ├── model.pkl  # Pre-trained Recommendation Model
│   ├── exception/
│   │   ├── ExceptionBase.py  # Custom Exception Handling
│── RecommendationSystem.ipynb  # Jupyter Notebook for EDA & Model Training
│── main.py  # Script to run the recommendation system
│── requirements.txt  # Dependencies
│── README.md  # Project Documentation
```

## 🛠️ Setup Instructions
### 1️⃣ Install Dependencies
Ensure you have Python installed, then run:
```sh
pip install -r requirements.txt
```

### 2️⃣ Run the Recommendation System
```sh
python main.py
```

### 3️⃣ Provide Customer ID
The system will prompt you to enter a `customer_id`, and it will return the top recommended products.

## 📦 Dependencies
- Python 3.8+
- Pandas
- NumPy
- Scikit-learn
- Surprise (for collaborative filtering)

## 💡 How It Works
1. **Load the dataset**: The system reads transaction data from `clean_dataset.csv`.
2. **Train the model**: Uses collaborative filtering to analyze purchase history.
3. **Make recommendations**: Given a `customer_id`, the system predicts the most relevant products.

## 🏆 Results
The model successfully generates personalized recommendations, improving user engagement and sales potential.

## 📝 Future Improvements
- Enhance model accuracy with deep learning techniques.
- Deploy as a web application using Flask or FastAPI.
- Integrate real-time recommendation updates based on live transactions.

---
✅ Developed by Prem Raj

