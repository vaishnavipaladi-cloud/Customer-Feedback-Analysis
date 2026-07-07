import streamlit as st
import pandas as pd
from sentiment_analysis import load_data, analyze_sentiment_vader, get_keywords, clean_text
from visualizations import (sentiment_pie_chart, rating_bar_chart,
                             sentiment_by_product, rating_trend, sentiment_by_category)
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Feedback Analysis", layout="wide")
st.title("📊 Customer Feedback Analysis Dashboard")

# Load data
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "customer_feedback (2).csv")
df = load_data(csv_path)

# Run VADER sentiment on review text
df[['vader_sentiment', 'vader_score']] = df['review_text'].apply(
    lambda x: pd.Series(analyze_sentiment_vader(x))
)

# Sidebar Filters
st.sidebar.header("🔍 Filters")
selected_sentiment = st.sidebar.multiselect("Sentiment", ['Positive', 'Negative', 'Neutral'],
                                             default=['Positive', 'Negative', 'Neutral'])
selected_product = st.sidebar.multiselect("Product", df['product'].unique(),
                                           default=df['product'].unique().tolist())
selected_rating = st.sidebar.slider("Minimum Rating", 1, 5, 1)

filtered_df = df[
    (df['sentiment_label'].isin(selected_sentiment)) &
    (df['product'].isin(selected_product)) &
    (df['rating'] >= selected_rating)
]

# KPI Cards
st.subheader("📌 Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Reviews", len(filtered_df))
col2.metric("Avg Rating", f"{filtered_df['rating'].mean():.2f}")
col3.metric("Positive %", f"{(filtered_df['sentiment_label']=='Positive').mean()*100:.1f}%")
col4.metric("Negative %", f"{(filtered_df['sentiment_label']=='Negative').mean()*100:.1f}%")

# Charts Row 1
st.subheader("📈 Sentiment & Ratings")
c1, c2 = st.columns(2)
with c1:
    st.plotly_chart(sentiment_pie_chart(filtered_df), use_container_width=True)
with c2:
    st.plotly_chart(rating_bar_chart(filtered_df), use_container_width=True)

# Charts Row 2
st.subheader("🛍️ Product & Category Analysis")
c3, c4 = st.columns(2)
with c3:
    st.plotly_chart(sentiment_by_product(filtered_df), use_container_width=True)
with c4:
    st.plotly_chart(sentiment_by_category(filtered_df), use_container_width=True)

# Trend
st.subheader("📅 Rating Trend Over Time")
st.plotly_chart(rating_trend(filtered_df), use_container_width=True)

# Word Cloud
st.subheader("☁️ Word Cloud")
all_text = ' '.join(filtered_df['review_text'].apply(clean_text))
wc = WordCloud(width=800, height=300, background_color='white').generate(all_text)
fig, ax = plt.subplots(figsize=(10, 4))
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# Review Table
st.subheader("📋 Customer Reviews")
search = st.text_input("Search reviews by keyword")
display_df = filtered_df[['customer_name', 'product', 'rating', 'sentiment_label', 'review_text', 'date']]
if search:
    display_df = display_df[display_df['review_text'].str.contains(search, case=False)]
st.dataframe(display_df, use_container_width=True)

# Download
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Download Filtered Data as CSV", csv, "filtered_feedback.csv", "text/csv")