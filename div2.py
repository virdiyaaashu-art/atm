import streamlit as st
st.title("Product Status")

st.badge("New")
st.badge("Sale", color="green")
st.badge("Premium", color="blue")
st.badge("Out of Stock", color="red")
st.badge("Coming Soon", color="grey")


st.divider()


st.title("simple chat app")
user_input=st.chat_input("type your message...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    if user_input=="hi":   
        with st.chat_message("assitant"):
         st.write("hello")
    elif user_input=="Hru":
        with st.chat_message("assistant"):
            st.write("i m f9!")
    else:
        with st.chat_message("assistant"):
            st.write("plz contact this no 9429459848")        
