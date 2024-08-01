from fastapi import FastAPI
import sys
from pydantic import BaseModel
import random



app = FastAPI()

module_path = '../VectorDB'
if module_path not in sys.path:
    sys.path.append(module_path)
    
module_path2 = '../Image2Caption'
if module_path2 not in sys.path:
    sys.path.append(module_path2)

import Image2Caption
import chroma
import Credentials

vector = chroma.vectordb(r"/Users/paliwal.v/Documents/Media.Net Hackathon Team MVPs/gitfolder/VectorDB/ChromaDB", "image-collection", Credentials.OPEN_AI_API_KEY)


class Url(BaseModel):
    url: str

@app.post("/image/")
async def create_item(Url: Url):
    caption = Image2Caption.getImageCaption(Url.url)
    vector.add_embeddings(str(random.getrandbits(128)), caption, Url.url)
    return (vector.collection.count(), caption)


@app.get("/count/")
async def create_item():
    return (vector.collection.count())


@app.get("/query/{title}")
async def create_item(title):
    return vector.query(title)
