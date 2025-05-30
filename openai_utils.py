import openai
from prompts import SYSTEM_PROMPTS

openai.api_key = "YOUR_OPENAI_KEY"  # Replace with your actual key

def generate_reply(message, brand):
    system_prompt = SYSTEM_PROMPTS.get(brand, SYSTEM_PROMPTS["default"])

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.8,
        max_tokens=60
    )

    return response['choices'][0]['message']['content'].strip()