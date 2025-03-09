# abalone-age-prediction
This project focuses on developing a machine learning model to predict the age of abalones using physical measurements.

[Visit the live website](https://abalone-age-prediction-wtct.onrender.com)

---

## 🚀 Features

- ✅ User-friendly **web interface** for entering abalone attributes  
- ✅ **Machine Learning model** (Random Forest) to predict abalone age  
- ✅ **MongoDB integration** for storing predictions  
- ✅ **Minimalist & responsive design**

---
- ## 📂 Project Setup

To run this project locally, follow these steps:

1. **Clone the repository**:
2. **Install dependencies**:
3. **Set up MongoDB Atlas**:
    - Create a MongoDB Atlas account and set up a cluster.
    - Connect MongoDB Compass to your Atlas cluster for easier management.
    - Create `.env` file and create `MONGODB_URI` variable and set its value to the connection string.
    
4. **Run the application: First, set the Flask application environment variable**:
    - On Windows:
      ```bash
      set FLASK_APP=app.py
      
    - On MacOS/Linux:
      ```bash
      exports FLASK_APP=app.py

    Then, run the application:
     ```bash
     flask run

---




