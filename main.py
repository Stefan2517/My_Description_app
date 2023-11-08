import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Stefan Semelbauer")
    content = """
    Passionate technology student looking for learning and professional development opportunities. 
    Follower of constant innovation and exploration in the technological field.
    """
    st.info(content)

prop = """
Below you can find some of the apps I have build in Python. Feel free to contact me!
"""

st.write(prop)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";") #coloanele sunt separate de ;, implicit e setat pe , (virgula)

with col3:
    for index, row in df[:10].iterrows(): #primele 10 coloane
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows(): #apoi celelalte 10
        st.header(row["title"])
