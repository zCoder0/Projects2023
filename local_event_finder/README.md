# Event Finder & Booking System

## 📌 Overview
The **Event Finder & Booking System** is a web application that allows users to book event-related services, such as **halls, DJ services, wedding decoration, birthday parties, and more**. It also features a **recommendation system** that suggests relevant services based on user history and preferences.

## 🔹 Features
✅ **User Registration & Login**  
✅ **Book Event Services** (Halls, DJ, Wedding Decoration, etc.)  
✅ **View and Manage Bookings**  
✅ **Recommendation System** (Personalized suggestions based on past bookings)  
✅ **Admin Dashboard for Service Management**  
✅ **Bootstrap-based Responsive UI**  

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, Bootstrap, jQuery  
- **Backend:** Django (Python), MySQL  
- **Database:** MySQL  
- **Machine Learning:** Python (Pandas, Scikit-learn) for recommendations  
- **Deployment:** Apache / Gunicorn & Nginx  

## 🎯 How It Works
### 1️⃣ User Books a Service
Users can choose a category (e.g., DJ, Hall, Wedding Decoration) and book a service by filling out a booking form.

### 2️⃣ Recommendation System
- **Collaborative Filtering:** Suggests services based on other similar users' bookings.  
- **Content-Based Filtering:** Finds similar services based on category.  

### 3️⃣ View Bookings & Recommendations
Users can view their bookings and see personalized **recommended services** based on their booking history.

## 📌 Installation Guide
### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/event-finder.git
cd event-finder
```

### 🔹 Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Step 3: Configure Database (MySQL)
1. Create a MySQL database:
```sql
CREATE DATABASE event_finder;
```
2. Update **settings.py** with database credentials.
3. Apply migrations:
```bash
python manage.py migrate
```

### 🔹 Step 4: Run the Development Server
```bash
python manage.py runserver
```

## 📌 Database Schema
### **Bookings Table**
```sql
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT NOT NULL,
    user_id INT NOT NULL,
    booker_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mobile VARCHAR(15) NOT NULL,
    address TEXT NOT NULL,
    category ENUM('Hall', 'Conference Rooms', 'Private Party Venues', 'DJ Services', 'Wedding & Stage Decoration', 'Birthday Party') NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    guests INT DEFAULT NULL,
    dj_name VARCHAR(100) DEFAULT NULL,
    theme VARCHAR(255) DEFAULT NULL,
    birthday_age INT DEFAULT NULL,
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
```

## 📌 Recommendation System Implementation
### **Collaborative Filtering Algorithm (Python & Pandas)**
```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def get_user_recommendations(user_id):
    bookings_df = pd.read_sql("SELECT user_id, service_id FROM bookings", con)
    user_service_matrix = bookings_df.pivot_table(index='user_id', columns='service_id', aggfunc='size', fill_value=0)
    user_similarity = cosine_similarity(user_service_matrix)
    similar_users = user_similarity[user_id].argsort()[::-1][1:6]
    recommended_services = []
    for similar_user in similar_users:
        similar_user_services = bookings_df[bookings_df['user_id'] == similar_user]['service_id'].values
        recommended_services.extend(similar_user_services)
    return list(set(recommended_services))
```



