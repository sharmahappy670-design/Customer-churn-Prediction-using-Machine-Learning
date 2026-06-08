%%writefile README.md

# 📊 Customer Churn Prediction Using Machine Learning

## 🧠 Project Overview
This project predicts whether a customer will churn (leave) or stay using Machine Learning techniques. It helps businesses identify at-risk customers and improve retention strategies.

---

## 🚀 Problem Statement
Customer churn is a major problem for subscription-based companies. The goal is to build a predictive model that can classify whether a customer will leave based on features like tenure and charges.

---

## 📁 Project Structure
- app.py → Streamlit web app
- model.pkl → Trained ML model
- requirements.txt → Dependencies
- README.md → Project documentation

---

## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

---

## 📊 Input Features
- Tenure (months)
- Monthly Charges
- Total Charges

---

## 🎯 Output
- Customer will CHURN ❌
- Customer will NOT CHURN ✅

---

## ▶️ How to Run

```bash
streamlit run app.py
