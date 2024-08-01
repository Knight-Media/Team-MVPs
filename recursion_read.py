import os
import sys
import random
import time

module_path = './VectorDB'
if module_path not in sys.path:
    sys.path.append(module_path)
    
module_path2 = './Image2Caption'
if module_path2 not in sys.path:
    sys.path.append(module_path2)

import Image2Caption
import chroma
import Credentials



vector = chroma.vectordb(r"/Users/manoj.kuma/Project/Media-Hackathon/Team-MVPs/VectorDB/ChromaDB", "image-collection", Credentials.OPEN_AI_API_KEY)

i = 0

def register_images(path: str):
    global i
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            register_images(full_path)
        else:
            i = i+1
            if(i<50):
                time.sleep(5)
                print('task done: ', i)
                if full_path.count(".DS_Store") == 0:
                    caption = Image2Caption.getImageCaption(full_path)
                    vector.add_embeddings(str(random.getrandbits(128)), caption, full_path)
                
register_images(r"/Users/manoj.kuma/Project/Media-Hackathon/Team-MVPs/DataSet")
print(i)