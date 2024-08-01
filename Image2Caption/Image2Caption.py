# Libraries
import base64
import io
from openai import OpenAI
from Credentials import *


from PIL import Image
import requests
import os

def getImage(source):
    try:
        # Check if the source is a URL
        if source.startswith("http://") or source.startswith("https://"):
            response = requests.get(source, stream=True)
            response.raise_for_status()
            image = Image.open(response.raw)
        else:
            # Assume the source is a file path
            if not os.path.exists(source):
                raise FileNotFoundError(f"The file path {source} does not exist.")
            image = Image.open(source)
            
        return image
    except (requests.exceptions.RequestException, FileNotFoundError, IOError) as e:
        print(f"Error in get_image...take action \n Error: {e}")


def encode_image(image):
  buffered = io.BytesIO()
  image.save(buffered, format="PNG")
  image_bytes = buffered.getvalue()
  
  # Encode the image bytes to base64
  return base64.b64encode(image_bytes).decode('utf-8')

client = OpenAI(api_key = OPEN_AI_API_KEY)

def generateImageCaption(base64_image):
    ques = f"""
Describe the image in minimum number of tokens, max {MAX_TOKENS_TO_GENERATE} tokens allowed. 
Try to include differnt possible aspect of image such as Subject, Action, Products, Brands, Location.
Make result descriptive, meaningful and use simple language.
Focus on main subject.
"""
    try:
        response = client.chat.completions.create(
            model=IMAGE2TEXTMODEL,
            messages=[
                {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": ques,
                    },
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                    },
                ],
                }
            ],
            max_tokens=MAX_TOKENS_TO_GENERATE+10,
        )
        return response.choices[0].message.content
    except:
        return "Error in API Calling...Take Action before too it's get too late"
    

def getImageCaption(url):
    image = getImage(url)
    base64_image = encode_image(image)
    caption = generateImageCaption(base64_image)
    return caption