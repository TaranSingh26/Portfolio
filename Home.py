import streamlit as st
import pandas

st.set_page_config(layout="wide")
col_1, col_2 = st.columns(2)

with col_1:
    st.image("images/me.jpeg")

with col_2:
    st.title("Tarandeep Singh")
    content = """
    
    Hi, I'm Tarandeep Singh I'm an undergraduate student pursuing a Bachelor of Technology 
    at the National Institute of Technology, Jalandhar. With a strong foundation in programming, 
    CAD, and simulation, I’m a curious and driven learner who enjoys building solutions that address 
    real-world challenges. I also bring leadership experience to collaborative projects and thrive 
    in dynamic, problem-solving environments. Let’s connect and explore what we can create together.
    
    """

    st.info(content)

content_2 = """

Below are some projects I am currently working on.

"""

st.text(content_2)

col_3, empty_col, col_4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col_3:

    for index, row in df[:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], use_container_width=True)
        st.write(f"[Source Code]({row['url']})")

with col_4:

    for index, row in df[4:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")