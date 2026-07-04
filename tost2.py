import streamlit as st
import time

st.title("Toast Example")

if st.button("Show Toast"):
    st.toast("Hru  🎉")
    time.sleep(1)
    st.toast("welcome 😊")
