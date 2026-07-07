# 📊 Customer Feedback Analysis Dashboard

## 🏢 Internship Project — Build IT Technologies

---

## 📌 Project Overview
A Customer Feedback Analysis System built using Python, Streamlit, and NLP techniques that analyzes customer reviews, detects sentiments, and displays interactive dashboards.

The **Customer Feedback Analysis Dashboard** is an intelligent analytics system 
that collects, processes, and analyzes customer reviews and feedback using 
**Natural Language Processing (NLP)** and **Data Analytics** techniques.

The system automatically classifies customer feedback into **Positive**, 
**Negative**, and **Neutral** sentiments using VADER and TextBlob sentiment 
analysis engines.

The interactive dashboard built with **Streamlit** and **Plotly** provides 
real-time visual insights into customer satisfaction, product performance, 
rating trends, and keyword analysis — helping businesses make data-driven 
decisions.

### 🎯 Problem Statement
Businesses receive thousands of customer reviews but struggle to manually 
analyze them. This system automates the entire feedback analysis process 
and presents meaningful insights through interactive visualizations.

### 💡 Solution
An end-to-end automated Customer Feedback Analysis System that:
- Reads and processes raw customer review data
- Detects sentiment using NLP techniques
- Displays interactive charts and dashboards
- Allows filtering, searching, and exporting data

---

## ✅ Features
- 📈 Sentiment Analysis (Positive / Negative / Neutral)
- 📊 Interactive Dashboard with Filters
- ☁️ Word Cloud of most used words
- 📅 Rating Trend Over Time
- 🛍️ Product & Category Analysis
- 🔍 Search & Filter Reviews
- ⬇️ Download Filtered Data as CSV

---

## 🛠️ Tech Stack
| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Streamlit | Dashboard UI |
| Pandas | Data Processing |
| NLTK | Natural Language Processing |
| TextBlob | Sentiment Analysis |
| Plotly | Interactive Charts |
| WordCloud | Word Visualization |
| Matplotlib | Plotting |

---

## 📊 Dataset
- **110 customer reviews**
- **5 Products:** Wireless Headphones, Bluetooth Speaker, Smartphone Case, Laptop Stand, USB Hub
- **Columns:** review_id, customer_name, age, gender, product, category, rating, review_text, sentiment_label, location, date

---

## ⚙️ How to Run

### Step 1 — Clone the repository
```bash
git clone https://github.com/vaishnavipaladi-cloud/Customer-Feedback-Analysis.git
cd Customer-Feedback-Analysis
```

### Step 2 — Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Download NLTK data
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')"
```

### Step 5 — Run the app
```bash
streamlit run app.py
```

### Step 6 — Open in browser
http://localhost:8501

---

## 📸 Dashboard Preview
- Key Metrics — Total Reviews, Avg Rating, Positive %, Negative %
- Sentiment Distribution Pie Chart
- Rating Distribution Bar Chart
- Product & Category Analysis Charts
- Rating Trend Over Time
- Word Cloud
- Searchable Customer Review Table

---

## 🎯 Learning Outcomes
- Data preprocessing techniques
- NLP fundamentals
- Sentiment analysis workflows
- Dashboard development
- Customer analytics
- Data visualization techniques

---

## 👩‍💻 Developed By
**Vaishnavi**  
Data Science & Analytics Intern  
**Company:** Build IT Technologies
