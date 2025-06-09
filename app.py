import streamlit as st
from fetch_articles import fetch_article_text
from summarize_news import summarize_article

st.set_page_config(page_title="Financial News Analyzer", layout="wide")
st.title("📰 Financial News Summarizer & Risk Extractor")

url = st.text_input("Paste the URL of a financial news article")

if url:
    with st.spinner("Fetching article..."):
        try:
            article_text = fetch_article_text(url)
        except Exception as e:
            st.error(f"Error fetching article: {e}")
            st.stop()

    st.subheader("📝 Full Article Text")
    st.write(article_text)

    with st.spinner("Generating Summary..."):
        summary = summarize_article(article_text)

    st.subheader("📌 Summary")
    st.write(summary)
