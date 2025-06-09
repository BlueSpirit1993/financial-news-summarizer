import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI

from fetch_articles import fetch_article_text
from summarize_news import summarize_article
from fetch_news_by_ticker import get_news_for_ticker
from risk_classifier import classify_article_risk

# ✅ Must be first Streamlit command
st.set_page_config(page_title="Financial News Analyzer", layout="wide")

# ✅ API setup
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ Sidebar inputs
st.sidebar.title("📈 Market Screener")
default_tickers = ['AAPL', 'TSLA', 'MSFT', 'NFLX', 'AMZN','D05.SI','APP']
tickers = st.sidebar.multiselect("Select Stocks", default_tickers, default=default_tickers)

# ✅ Market Screener button
if st.sidebar.button("🧠 Run Market Screener"):
    st.subheader("📊 Risk Overview")
    results = []

    for ticker in tickers:
        st.write(f"📈 {ticker}")
        articles = get_news_for_ticker(ticker)
        stock_risks = []

        for article in articles:
            with st.spinner(f"Analyzing news for {ticker}: {article['title']}"):
                result = classify_article_risk(article['summary'])
                stock_risks.append(result)

        risky_count = sum("Risky" in r for r in stock_risks)
        status = "⚠️ Risky" if risky_count > 2 else "✅ Safe"

        results.append({
            "Ticker": ticker,
            "Status": status,
            # "Last Headline": articles[0]['title'],
            # "Analysis": stock_risks[0]
        })

    # ✅ Display results table
    df = pd.DataFrame(results)
    st.dataframe(df)
