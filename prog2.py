import streamlit as st
import time
progress=st.progress(0)
for i in range(101):
    time.sleep(0.07)
    progress.progress(i)
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrEuuX8J7389qvjjHtPvnHRFf9WFA5BNvEuuCYdpgzSz24BoCRUnslips&s=10")
    time.sleep(1)
    
