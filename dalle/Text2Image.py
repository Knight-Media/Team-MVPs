import openai
from PIL import Image
from openai import OpenAI
import sys
import requests
from io import BytesIO

module_path = './../Image2Caption'
if module_path not in sys.path:
    sys.path.append(module_path)

import Credentials

client = OpenAI(api_key= Credentials.OPEN_AI_API_KEY)

def getImageFromURL(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        return image
    except requests.exceptions.RequestException as e:
        print("Error in fetching generated Image from URL")
        return None
    
def getImageFromText(keyword):
    updated_prompt = f'''
I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS:
Generate a Photo for "{keyword}", photorealistic, photography, high quality, perfectly centered, octane render, bokeh, extremely detailed background, hyperrealism, ambient, hyper detailed, maximum detail, 8k, award - winning photograph
Photo must be realistic, avoid fake scenerio
Generate image which can be used in Advertisement

Avoid image distorted structure and over repetition
'''

    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=updated_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url
        # return response
    except openai.OpenAIError as e:
        print("Error generating image from API")
        print(e.http_status)
        print(e.error)
        return None

