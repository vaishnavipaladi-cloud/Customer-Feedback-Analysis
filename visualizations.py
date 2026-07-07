import plotly.express as px
import pandas as pd

def sentiment_pie_chart(df):
    counts = df['sentiment_label'].value_counts().reset_index()
    counts.columns = ['Sentiment', 'Count']
    fig = px.pie(counts, names='Sentiment', values='Count',
                 color='Sentiment',
                 color_discrete_map={'Positive':'#2ecc71','Negative':'#e74c3c','Neutral':'#f39c12'},
                 title='Sentiment Distribution')
    return fig

def rating_bar_chart(df):
    counts = df['rating'].value_counts().sort_index().reset_index()
    counts.columns = ['Rating', 'Count']
    fig = px.bar(counts, x='Rating', y='Count',
                 title='Rating Distribution',
                 color='Count', color_continuous_scale='Blues')
    return fig

def sentiment_by_product(df):
    grouped = df.groupby(['product', 'sentiment_label']).size().reset_index(name='Count')
    fig = px.bar(grouped, x='product', y='Count', color='sentiment_label',
                 barmode='group',
                 color_discrete_map={'Positive':'#2ecc71','Negative':'#e74c3c','Neutral':'#f39c12'},
                 title='Sentiment by Product')
    return fig

def rating_trend(df):
    df['month'] = df['date'].dt.to_period('M').astype(str)
    trend = df.groupby('month')['rating'].mean().reset_index()
    fig = px.line(trend, x='month', y='rating',
                  title='Average Rating Over Time', markers=True)
    return fig

def sentiment_by_category(df):
    grouped = df.groupby(['category', 'sentiment_label']).size().reset_index(name='Count')
    fig = px.bar(grouped, x='category', y='Count', color='sentiment_label',
                 barmode='stack',
                 color_discrete_map={'Positive':'#2ecc71','Negative':'#e74c3c','Neutral':'#f39c12'},
                 title='Sentiment by Category')
    return fig