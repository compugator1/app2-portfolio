import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Mark Maglio")
    info_content = """
    Hello, I am Mark Maglio.  I am an electrical engineer who has programmed for over 40 years.\n\n
    I am looking forward to showing you what I have built with Python since I started working with it.
    """
    st.info(info_content)

# better to use this method of inputting content to be pronted rather than editing the python commands directly
content = """
Below you can find some of the apps I have built in Python.  Feel free to contact me!
"""
st.write(content)

