# 💳 Credit Card Fraud Analytics Dashboard

An interactive **Streamlit dashboard** designed to analyze credit card transaction data, uncover fraud patterns, and deliver actionable business insights through intuitive visualizations.

---![Uploading image.png…]()


## 📊 Project Overview

This project focuses on **fraud detection analytics** using a financial transactions dataset.
Instead of only building a machine learning model, the dashboard emphasizes:

* Exploratory Data Analysis (EDA)
* Fraud behavior understanding
* Risk-based insights
* Interactive data exploration

---

## 🚀 Features

* 🔍 **Interactive Filters**

  * Filter transactions by amount and transaction hour

* 📈 **Fraud Analysis**

  * Fraud vs Non-Fraud distribution
  * Transaction amount trends
  * Hourly fraud patterns

* ⚠️ **Risk Scoring System**

  * Rule-based risk score using:

    * Foreign transactions
    * Location mismatch
    * Transaction velocity
    * Device trust score

* 📊 **Advanced Insights**

  * Top fraud-prone merchant categories
  * Correlation heatmap
  * Behavioral fraud patterns

* 🧠 **Insights Panel**

  * Key business findings derived from data

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas & NumPy**
* **Matplotlib & Seaborn**

---

## 📂 Project Structure

```
creditcard/
│── app.py
│── credit_card_fraud_10k.csv
│── README.md
```

---

## ▶️ Run Locally

Follow these steps to run the project on your system:

### 1. Clone the repository

```
git clone <your-repo-link>
cd creditcard
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Launch the dashboard

```
python -m streamlit run app.py
```

### 4. Open in browser

```
http://localhost:8501
```

---

## 📌 Key Insights

* Fraud is significantly higher in **foreign transactions** and **location mismatches**
* **High transaction velocity** is a strong fraud indicator
* **Low device trust score** correlates strongly with fraudulent activity
* Certain **merchant categories** show higher fraud risk

---

## 🎯 Future Improvements

* Integrate machine learning-based fraud prediction
* Deploy dashboard online (Streamlit Cloud)
* Add real-time transaction monitoring
* Enhance UI with interactive visualizations (Plotly)



