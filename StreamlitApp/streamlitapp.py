import streamlit as st
import numpy as np
import pandas as pd
import random
import time
from PIL import Image
from page1 import *
from page2 import *


# Heading
st.write("# "+'PicQuest')

def main():
    # Create columns for navigation buttons
    col1, col2 = st.columns([1, 1])

    st.sidebar.title("Navigation")
    
    # Initialize session state for page if not already done
    if "page" not in st.session_state:
        st.session_state.page = "Page 1"  # Default to Page 1

    with col1:
        if st.sidebar.button("Page 1"):
            st.session_state.page = "Page 1"
    with col2:
        if st.sidebar.button("Page 2"):
            st.session_state.page = "Page 2"

    # Render the appropriate page based on the current state
    if st.session_state.page == "Page 1":
        page1()
    elif st.session_state.page == "Page 2":
        page2()

# Run the app
if __name__ == "__main__":
    main()
