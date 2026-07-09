import streamlit as st
@st.dialog("Student Information")
def show_dialog():
    st.write("Name: Tattvam Kaneriya")
    st.write("Course: Streamlit ")
    st.write("Semester: 5")
if st.button("Open Dialog"):
        show_dialog()
    

