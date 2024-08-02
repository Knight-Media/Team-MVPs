import streamlit as st
import sys
import requests
import os
from PIL import Image

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

# Define a function for each page
def page1():
    
    st.write("### "+'Ads Campaign Manager')
    
    add_prompt_box = st.text_input(
        "Search Image", key="imageSearch",
        value = 'Best Hotels near me'
    )

    submit = st.empty()
    submit = st.button('Search Image', key='searchImageButton')
    if submit:
        api = "http://172.16.174.76:8000/query/"
        query_link = api + st.session_state.imageSearch
        try:
            response = requests.get(query_link)
            # print(response.text)
            # st.write(response.json()[1]['path'])
        except:
            st.error("Error in initial API call")
            
        image = getImage(response.json()[1]['path'])
        
        st.image(image,caption='Search Image', width =1028, output_format='auto')
        st.write(f'{response.json()[0]}')
    
    
    
    
def page2():
    st.write("# Page 2")
    st.write("This is the content of Page 2.")
    
    
    
    
    
# module_path = '/Users/manoj.kuma/Project/Media-Hackathon/Team-MVPs/VectorDB'
# if module_path not in sys.path:
#     sys.path.append(module_path)
    
# module_path2 = '/Users/manoj.kuma/Project/Media-Hackathon/Team-MVPs/Image2Caption'
# if module_path2 not in sys.path:
#     sys.path.append(module_path2)

# import chroma
# import Credentials