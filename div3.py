import streamlit as st
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
    elif user_input== "question":
        with st.chat_message("assistant"):
            st.write("how can i help you")
    else:
        with st.chat_message("assistant"):
            st.write("call on this no 584686497")        


    
