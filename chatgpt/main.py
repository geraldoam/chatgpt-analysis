from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

completion = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

def chat(message):
    response = completion.chat.completions.create(
        model="gpt-3.5-turbo",
        messages={"role": "user", "content": message}
    )

    return response

if __name__ == '__main__':
    user_message = input("eu: ")

    response = chat(user_message)
    print("masqueico: ", response)
