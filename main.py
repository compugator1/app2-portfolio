import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Mark Maglio")
    content = """
    Hello, I am Mark Maglio.  I am an electrical engineer who has programmed for over 40 years.\n\n
    I am looking forward to showing you what I have built with Python since I started working with it.
    """
    st.info(content)