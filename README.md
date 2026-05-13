# AI Grievance System (NYC 311 NLP Project)

## 📌 Project Overview
This project is an AI-powered grievance classification system developed using Natural Language Processing (NLP) and Machine Learning techniques.

The system automatically analyzes citizen complaints from the NYC 311 dataset and routes them to the appropriate government department such as Police, Transport, Water Department, or Road Maintenance.

---

## 🎯 Objectives
- Automate complaint routing
- Reduce manual workload
- Improve grievance management efficiency
- Perform intelligent text classification using NLP

---

## 🧠 Features
- Text preprocessing and cleaning
- Stopword removal and lemmatization
- TF-IDF vectorization
- Logistic Regression classification model
- Department categorization
- Cross-validation evaluation
- Confusion matrix visualization
- Complaint prediction system

---

## 🛠 Tech Stack
- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 📊 Dataset
NYC 311 Service Requests Dataset from Kaggle

---

## 📁 Project Structure

```text
ai-grievance-system/
│
├── data/
│   └── nyc311.csv
│
├── notebooks/
│   ├── week1_nyc311_eda.ipynb
│   └── week2_model.ipynb
│
├── models/
│   ├── complaint_classifier.pkl
│   └── tfidf_vectorizer.pkl
│
├── outputs/
├── plots/
├── src/
│   └── preprocessing.py
│
├── README.md
