# 🛡️ IntelliFraud-AI

<div align="center">

# AI Powered Financial Fraud Detection System

### Enterprise Machine Learning Platform for Real-Time Financial Fraud Detection

Detect fraudulent financial transactions using Artificial Intelligence, Machine Learning, FastAPI, Streamlit and Interactive Business Intelligence Dashboards.

<br>

[![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)](https://www.python.org)

[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)

[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io)

[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-MachineLearning-orange?style=for-the-badge&logo=scikitlearn)](https://scikit-learn.org)

[![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge&logo=plotly)](https://plotly.com)

[![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)](LICENSE)

[![Status](https://img.shields.io/badge/Status-Production_Ready-brightgreen?style=for-the-badge)]()

</div>

---

# 🚀 Live Demo

## 🌐 Frontend

https://ai-powered-financial-fraud-detection-6o5j.onrender.com

---

## ⚡ Backend API

https://ai-powered-financial-fraud-detection-6mcp.onrender.com

---

## 📖 Swagger Documentation

https://ai-powered-financial-fraud-detection-6mcp.onrender.com/docs

---

# ⭐ Project Highlights

- 🤖 Artificial Intelligence Powered Fraud Detection
- 📊 Interactive Analytics Dashboard
- ⚡ FastAPI REST API
- 📈 Executive Business Dashboard
- 📂 Batch Prediction Support
- 📄 Downloadable Reports
- 🌐 Cloud Deployment on Render
- 🔥 Production Ready Architecture
- 🛡 Enterprise Grade Project Structure
- 📊 Interactive Plotly Visualizations

---

# 📚 Table of Contents

- Overview
- Real World Problem
- Proposed Solution
- Features
- System Architecture
- Technology Stack
- Dataset
- Machine Learning Pipeline
- Project Structure
- Dashboard
- API
- Installation
- Deployment
- Future Roadmap
- Developer
- License

---

# 📌 Overview

IntelliFraud-AI is a complete end-to-end Machine Learning application designed to detect fraudulent financial transactions in real time.

The project combines Artificial Intelligence, Data Engineering, REST APIs, and Interactive Business Dashboards into a single enterprise-level solution.

The application allows organizations to identify suspicious transactions within milliseconds while providing powerful business intelligence dashboards for fraud analysis.

Unlike traditional fraud detection systems based on manually defined rules, IntelliFraud-AI uses Machine Learning algorithms capable of learning complex fraud patterns automatically.

The platform has been developed following modern software engineering practices using a modular architecture that separates data processing, model training, API development, and user interface components.

---

# 🌍 Real World Problem

Every day banks, payment gateways and financial institutions process millions of online transactions.

Manual verification of every transaction is impossible.

Traditional rule-based fraud detection systems suffer from several limitations:

- Slow detection
- High operational costs
- Large number of false alarms
- Difficulty adapting to new fraud patterns
- Poor scalability
- High financial losses

Fraudsters continuously modify their behaviour, making static rule-based systems ineffective.

Organizations require intelligent systems capable of automatically learning fraud behaviour from historical transaction data.

---

# 💡 Proposed Solution

IntelliFraud-AI provides an AI-driven fraud detection platform capable of automatically classifying financial transactions into:

- Legitimate Transaction
- Fraudulent Transaction

The complete workflow includes:

- Data Validation
- Data Cleaning
- Feature Engineering
- Model Training
- Model Evaluation
- Best Model Selection
- REST API Deployment
- Interactive Dashboard
- Business Analytics
- Cloud Deployment

The solution provides real-time fraud prediction together with confidence scores and interactive visualization for business users.

---



# ✨ Features

## 🤖 Artificial Intelligence

- Fraud Prediction
- Machine Learning Classification
- Confidence Score
- Multiple Model Comparison
- Automatic Best Model Selection

---

## 📊 Analytics

- Executive Dashboard
- Fraud Distribution
- Transaction Explorer
- Correlation Heatmap
- Business Insights
- Interactive Charts

---

## ⚡ Backend

- FastAPI
- REST API
- Swagger Documentation
- Health Monitoring
- Prediction APIs

---

## 🖥 Frontend

- Streamlit
- Interactive Dashboard
- Plotly Visualizations
- Batch Prediction
- Report Download
- Modern UI

---
# 🏗️ System Architecture

```text
                         ┌──────────────────────────────┐
                         │        End User              │
                         └──────────────┬───────────────┘
                                        │
                                        ▼
                      ┌────────────────────────────────────┐
                      │      Streamlit Frontend            │
                      │ Dashboard • Analytics • Reports    │
                      └────────────────┬───────────────────┘
                                       │
                              HTTP REST Requests
                                       │
                                       ▼
                      ┌────────────────────────────────────┐
                      │         FastAPI Backend            │
                      │ Prediction API • Health API        │
                      └────────────────┬───────────────────┘
                                       │
                 ┌─────────────────────┴──────────────────────┐
                 │                                            │
                 ▼                                            ▼
      ┌─────────────────────────┐              ┌────────────────────────┐
      │  Machine Learning Model │              │   Model Artifacts      │
      │     Random Forest       │              │ Scaler • Metadata      │
      └─────────────────────────┘              └────────────────────────┘
                 │
                 ▼
      ┌─────────────────────────┐
      │ Fraud Prediction Result │
      └─────────────────────────┘
```

---

# 🔄 Complete Workflow

```text
Credit Card Dataset
          │
          ▼
Data Validation
          │
          ▼
Data Cleaning
          │
          ▼
Exploratory Data Analysis
          │
          ▼
Feature Engineering
          │
          ▼
Train Test Split
          │
          ▼
Feature Scaling
          │
          ▼
Machine Learning Models
          │
          ▼
Model Evaluation
          │
          ▼
Best Model Selection
          │
          ▼
Model Serialization
          │
          ▼
FastAPI Backend
          │
          ▼
Streamlit Dashboard
          │
          ▼
Real-Time Fraud Detection
```

---

# 📂 Project Structure

```text
IntelliFraud-AI
│
├── backend/
│   ├── api.py
│   ├── prediction.py
│   ├── schemas.py
│   └── utils.py
│
├── frontend/
│   ├── Home.py
│   └── pages/
│       ├── Dashboard.py
│       ├── Single_Prediction.py
│       ├── Batch_Prediction.py
│       ├── Analytics.py
│       ├── Reports.py
│       ├── About.py
│       └── Settings.py
│
├── config/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   ├── feature_columns.pkl
│   └── metadata.json
│
├── reports/
│
├── screenshots/
│
├── src/
│   ├── preprocessing/
│   ├── models/
│   ├── visualization/
│   └── utils/
│
├── requirements.txt
├── run.py
├── README.md
└── LICENSE
```

---

# 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.13 |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Backend | FastAPI |
| Frontend | Streamlit |
| Visualization | Plotly |
| API Documentation | Swagger |
| Deployment | Render |
| Version Control | Git & GitHub |

---

# 📊 Dataset

The project uses the **Credit Card Fraud Detection Dataset**.

| Attribute | Value |
|-----------|-------|
| Total Transactions | 284,807 |
| Legitimate Transactions | 284,315 |
| Fraud Transactions | 492 |
| Features | 30 |
| Target Variable | Class |
| Fraud Ratio | 0.172% |

### Dataset Characteristics

- Highly Imbalanced Dataset
- Binary Classification Problem
- Real-world Banking Transactions
- Suitable for Fraud Detection Research

> **Note:** Due to GitHub's 100 MB file size limitation, this repository includes a lightweight sample dataset for demonstration. The complete dataset can be downloaded from Kaggle and processed locally using `python run.py`.

---

# 🤖 Machine Learning Pipeline

The complete Machine Learning pipeline consists of:

- ✅ Data Validation
- ✅ Data Cleaning
- ✅ Exploratory Data Analysis
- ✅ Feature Engineering
- ✅ Train-Test Split
- ✅ Feature Scaling
- ✅ Model Training
- ✅ Model Evaluation
- ✅ Model Comparison
- ✅ Best Model Selection
- ✅ Model Serialization
- ✅ API Deployment
- ✅ Interactive Dashboard
- ✅ Cloud Deployment

---# 🤖 Machine Learning Models

IntelliFraud-AI evaluates multiple supervised machine learning algorithms to identify the most effective model for fraud detection.

| Model | Description |
|--------|-------------|
| Logistic Regression | Linear baseline classification model |
| Decision Tree | Rule-based classification model |
| Random Forest | Ensemble learning model |
| Gradient Boosting | Sequential ensemble model |
| XGBoost *(Optional)* | Advanced gradient boosting model |

---

# 🏆 Best Model Selection

After evaluating all machine learning models using multiple evaluation metrics, the **Random Forest Classifier** was selected as the final production model.

### Why Random Forest?

- High classification accuracy
- Excellent precision and recall
- Handles imbalanced datasets efficiently
- Resistant to overfitting
- Fast prediction speed
- Suitable for production deployment

---

# 📈 Model Evaluation Metrics

The project evaluates each model using the following metrics.

| Metric | Description |
|--------|-------------|
| Accuracy | Overall prediction correctness |
| Precision | Percentage of predicted fraud transactions that are actually fraud |
| Recall | Ability to identify fraudulent transactions |
| F1 Score | Harmonic mean of Precision and Recall |
| ROC-AUC | Overall classification capability |

---

# 📊 Model Performance

> **Note:** Actual performance metrics are generated after executing the training pipeline (`python run.py`). Performance depends on the trained model and preprocessing pipeline.

| Model | Status |
|--------|--------|
| Logistic Regression | Evaluated |
| Decision Tree | Evaluated |
| Random Forest | Selected as Best Model |
| Gradient Boosting | Evaluated |

---

# 📸 Project Screenshots

## 🏠 Home Page

<p align="center">
<img src="screenshots/home.png" width="95%">
</p>

---

## 📊 Dashboard

<p align="center">
<img src="screenshots/dashboard.png" width="95%">
</p>

---

## 📈 Analytics

<p align="center">
<img src="screenshots/analytics.png" width="95%">
</p>

---

## 🤖 Single Prediction

<p align="center">
<img src="screenshots/prediction.png" width="95%">
</p>

---

## 📂 Batch Prediction

<p align="center">
<img src="screenshots/batch_prediction.png" width="95%">
</p>

---

## 📄 Reports

<p align="center">
<img src="screenshots/reports.png" width="95%">
</p>

---

## ⚙️ Settings

<p align="center">
<img src="screenshots/settings.png" width="95%">
</p>

---

# 🌐 Live Deployment

## 🚀 Frontend

https://ai-powered-financial-fraud-detection-6o5j.onrender.com

---

## ⚡ Backend API

https://ai-powered-financial-fraud-detection-6mcp.onrender.com

---

## 📖 Swagger API Documentation

https://ai-powered-financial-fraud-detection-6mcp.onrender.com/docs

---

# 🔌 REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Home |
| GET | `/health` | Backend Health Check |
| GET | `/docs` | Swagger Documentation |
| POST | `/predict` | Predict Single Transaction |
| POST | `/batch-predict` | Predict Batch CSV Transactions |

---

# 📊 Dashboard Modules

The Streamlit application includes the following modules.

- 🏠 Home
- 📊 Executive Dashboard
- 🤖 Single Prediction
- 📂 Batch Prediction
- 📈 Advanced Analytics
- 📄 Reports Center
- ℹ️ About
- ⚙️ Settings

---

# 💼 Business Applications

This project can be adapted for:

- 🏦 Banking Fraud Detection
- 💳 Credit Card Fraud Detection
- 💸 Digital Payment Monitoring
- 🛒 E-Commerce Fraud Detection
- 📱 Mobile Banking Security
- 🌍 Online Payment Gateways
- 🏢 FinTech Platforms
- 🔒 Financial Risk Management

---
# ⚙️ Installation Guide

## Clone the Repository

```bash
git clone https://github.com/janvichauhan1639-source/IntelliFraud-AI.git
```

---

## Navigate to the Project Directory

```bash
cd IntelliFraud-AI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate the environment

```bash
.venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Complete Machine Learning Pipeline

```bash
python run.py
```

This command automatically performs:

- Data Validation
- Data Cleaning
- Feature Engineering
- Train-Test Split
- Model Training
- Model Evaluation
- Model Comparison
- Best Model Selection
- Artifact Generation

---

## Start FastAPI Backend

```bash
uvicorn backend.api:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Start Streamlit Frontend

```bash
streamlit run frontend/Home.py
```

---



# 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Artificial Intelligence
- Machine Learning
- Data Cleaning
- Feature Engineering
- Feature Scaling
- Exploratory Data Analysis
- Model Evaluation
- Ensemble Learning
- REST API Development
- FastAPI
- Streamlit
- Plotly
- Cloud Deployment
- Git & GitHub
- Software Engineering
- Business Intelligence

---

# 🚀 Future Enhancements

Future improvements planned for IntelliFraud-AI include:

- Explainable AI (SHAP)
- LIME Integration
- Deep Learning Models
- AutoML Support
- Docker Containerization
- Kubernetes Deployment
- CI/CD Pipeline
- JWT Authentication
- PostgreSQL Integration
- Redis Cache
- Kafka Streaming
- Email Notifications
- SMS Fraud Alerts
- Live Transaction Monitoring
- User Authentication
- Role-Based Access Control
- Mobile Application
- Multi-Language Support

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve IntelliFraud-AI:

1. Fork the repository

2. Create a new feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to your branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software under the terms of the MIT License.

---

# 🙏 Acknowledgements

Special thanks to:

- Kaggle Credit Card Fraud Detection Dataset
- Python Community
- FastAPI
- Streamlit
- Plotly
- Scikit-Learn
- Open Source Contributors

---

# 👨‍💻 Developer

## Janvi Chauhan

### AI & Machine Learning Developer

### Technical Skills

- Python
- Machine Learning
- Artificial Intelligence
- FastAPI
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Plotly
- REST APIs
- Data Visualization
- Git & GitHub

---

## GitHub Profile

https://github.com/janvichauhan1639-source

---

## Repository

https://github.com/janvichauhan1639-source/IntelliFraud-AI

---

# 🌟 If You Like This Project

If you found this project useful:

⭐ Star this repository

🍴 Fork this repository

📢 Share it with your friends

💡 Suggest improvements

🤝 Contribute to the project

Your support motivates future development.

---

# 📬 Contact

For questions, suggestions, or collaboration opportunities, feel free to connect through GitHub.

GitHub:

https://github.com/janvichauhan1639-source

---

<div align="center">

# 🛡️ IntelliFraud-AI

### Enterprise AI Powered Financial Fraud Detection Platform

Built with ❤️ using

**Python • Scikit-Learn • FastAPI • Streamlit • Plotly**

---

**Version 1.0.0**

© 2026 Janvi Chauhan

</div>
