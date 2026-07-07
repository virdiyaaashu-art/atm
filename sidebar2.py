import streamlit as st
st.title("Main Page")
st.sidebar.title("Menu")
name = st.sidebar.text_input("Enter your name")
course = st.sidebar.selectbox(
    "Select Course",
    ["B.Tech", "BCA", "MCA", "MBA"]
)
if name:
    st.write("Name:", name)
    st.write("Course:", course)
st.title("Student Portal")
tab1, tab2, tab3 = st.tabs(
    ["Personal Details", "Academic Details", "Contact"]
)
with tab1:
    st.header("Personal Details")
    st.write("Name: tattvam kaneriya")
    st.write("Age: 8")
    with tab2:
        st.header("Academic Details")
    st.write("Course: B.Tech")
    st.write("Semester: 5")

with tab3:
    st.header("Contact")
    st.write("Email: tattvamkaneriya@gmail.com")
    
    
  
