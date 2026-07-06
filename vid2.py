import streamlit as st
age=st.slider("select age 0,100,20")
st.write("Age:", age)
experience = st.select_slider(
    "Experience Level",
    options=["Beginner", "Intermediate", "Advanced", "Expert"]
)
st.write("Experience:", experience)
uploaded=st.file_uploader("upload a file",type=["txt","pdf","png","jpg"])
if uploaded is not None:
    st.success(f"Uploaded: {uploaded.name}")
meeting = st.time_input("Meeting Time")
st.write("Time:", meeting)
picture=st.camera_input("take a picture")
if picture:
    st.image(picture)
colour=st.color_picker("Choose Color", "#00FF00")
st.write("Selected Color:", colour)    
dark = st.toggle("Enable Dark Mode")
st.write("Dark Mode:", dark)
fruit = st.pills(
    "Favorite Fruit",
    ["Apple", "Banana", "Orange", "Mango"]
)
st.write("Selected Fruit:", fruit)
