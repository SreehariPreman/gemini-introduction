from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()  # load all the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image, user_prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], user_prompt])
    return response.text
user_prompt =input("enter your question: ")

# Load the image
image_path = "data/i_love_you.jpg"
image = Image.open(image_path)

# Define input prompt
input_prompt = """
    You are an expert in understanding sign language. We will upload a a image
    and you will have to answer any questions based on the uploaded image
"""

# Call the function to get response
response = get_gemini_response(input_prompt, [image], user_prompt)

# Print or use the response as needed
print(response)

