import streamlit as st
import time

progress = st.progress(0)

for i in range(101):
    time.sleep(0.07)
    progress.progress(i)


# Show success message
st.success("Completed!")
time.sleep(1)
# Launch balloons
st.balloons()