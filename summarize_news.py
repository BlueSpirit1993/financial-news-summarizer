import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_prompt(template_file, article_text):
    with open(template_file, "r") as f:
        prompt = f.read().replace("{{article_text}}", article_text)
    return prompt

def summarize_article(article_text):
    prompt = load_prompt("prompts/summary_prompt.txt", article_text)
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()
