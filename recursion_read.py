import os
import chroma
import image2CCaption
import random

vector = chroma.vectordb(r"path-to-db", "test-collection", "api-key")

def register_images(path: str):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            register_images(full_path)
        else:
            caption = image2CCaption.getImageCaption(full_path)
            vector.add_embeddings(random.getrandbits(128), caption, full_path)