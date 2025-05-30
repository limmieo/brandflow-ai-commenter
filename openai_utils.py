import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPTS

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_reply(message, brand):
    system_prompt = SYSTEM_PROMPTS.get(brand, SYSTEM_PROMPTS["default"])

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.8,
        max_tokens=60
    )

    return response.choices[0].message.content.strip()
