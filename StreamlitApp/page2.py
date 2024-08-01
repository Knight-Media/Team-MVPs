import streamlit as st
import sys
import requests
import os
from PIL import Image
import streamlit.components.v1


# Define a function for each page
def page2():
    st.write("### "+'RealTime UseCase')
    add_prompt_box = st.text_input(
        "Search Image", key="imageSearch",
        value = 'Best Hotels near me'
    )

    submit = st.empty()
    submit = st.button('Search Image', key='searchImageButton')
    if submit:
        st.write(f'just for demo purpose')
        
        with open("/Users/manoj.kuma/Project/Media-Hackathon/Team-MVPs/StreamlitApp/htmlDemo.html", "r") as file:
            html_content = file.read()
            st.components.v1.html(html_content, width=1000, height=1200, scrolling=True)
        
        # with open("/Users/manoj.kuma/Project/Media-Hackathon/Team-MVPs/StreamlitApp/htmlDemo.html", "r") as file:
        #     html_content = file.read()
        #     st.components.html(html_content, height=500)
        # st.components.v1.iframe(, width=None, height=None, scrolling=False)