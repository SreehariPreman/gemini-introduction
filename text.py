import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

input = input("enter your questions: ")
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(input)
print(response.text)