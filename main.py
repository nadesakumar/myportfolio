import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image(".\images\photo.png")

with col2:
    content = """Hi, I am Nadesakumar. I am a human being with over 30 years of experience. My interests keep changing
    and my personality with it. I am still pursuing my passion and this is by far the closest I have gotten to it. 
    I am very intrigued and interested by Python programming and I am hoping to showcase what I am doing with this website."""
    st.title("Nadesakumar")
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me")

