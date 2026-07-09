import streamlit as st
st.title("Popover Example")
with st.popover("View Details"):
    st.write("Name: Tattvam Kaneriya")
    st.write("Course: Streamlit ")
    st.write("Semester: 5")