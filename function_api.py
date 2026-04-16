import os,io
from dotenv import load_dotenv
from google import genai
load_dotenv()
from PIL import Image

api_key = os.getenv("GEMINI_API_KEY25") 
client = genai.Client(api_key=api_key)


def issue_generator(images):
    pill_img = []
    for img in images:
        pill_img.append(Image.open(img))
    prompt = """Analyze the code snapshot and write in short where and why the error occuring
    without fixation.Add markdown to differentiate different section"""
    response = client.models.generate_content(
        model = "gemini-flash-lite-latest", 
        contents = [pill_img,prompt]
    )
    return response.text

def solve_generator(images,sol):
    pill_img = []
    for img in images:
        pill_img.append(Image.open(img))
    if sol=="Hints":
        prompt = "Generate hints of the error from the images to fix it without code and with proper markdown to look output nice"
    elif sol=="Solution with code":
        prompt = "Generate code by fixing the error of the image with proper markdown to look output nice"
    response = client.models.generate_content(
        model = "gemini-flash-lite-latest", 
        contents = [pill_img,prompt]
    )
    return response.text