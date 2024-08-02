import streamlit as st
import numpy as np
import pandas as pd
import random
import time
from PIL import Image
from page1 import *
from page2 import *


# Heading
st.markdown("<h1 style='text-align: center;'>PicQuest</h1>", unsafe_allow_html=True)
st.write("### "+'Ads Campaign Manager')

# Add image generation process
model_type = st.selectbox(
    'Select to Generate Image or not',
    ('Search Only', 'Search and Generate'),
    key='search_type'
)

def main():
    add_prompt_box = st.text_input(
        "Search Image", key="imageSearch",
        value = 'Best Hotels near me'
    )
    
    submit = st.empty()
    submit = st.button('Search Image', key='searchImageButton')
    if submit:
        page1(st.session_state)
    
    

# Run the app
if __name__ == "__main__":
    main()



# Initialize session state for page if not already done
    # if "page" not in st.session_state:
    #     st.session_state.page = "Page 1"  # Default to Page 1

    # with col1:
    #     if st.sidebar.button("Page 1"):
    #         st.session_state.page = "Page 1"
    # with col2:
    #     if st.sidebar.button("Page 2"):
    #         st.session_state.page = "Page 2"

    # # Render the appropriate page based on the current state
    # if st.session_state.page == "Page 1":
    #     page1()
    # elif st.session_state.page == "Page 2":
    #     page2()