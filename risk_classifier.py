from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_article_risk(article_text):
    prompt = f"""
You are a financial analyst assistant.

Read the article content below and question:
- Is the stock Safe or Risky? Just Answer Safe or Risky

ARTICLE:
{article_text}
"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()
