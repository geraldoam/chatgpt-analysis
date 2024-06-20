import os
from dotenv import load_dotenv

load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_AI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")
response = model.generate_content("Fala meu parceiro, qual seu nome?")

print(response.text)
