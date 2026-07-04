import streamlit as st
import time
st.title("status example")
if st.button("start a prosess"):
    with st.status("Processing...", expanded=True) as status:
        st.write("step 1: Reading Data...")
        time.sleep(2)
        st.write("step 2: Cleanig Data... ")
        time.sleep(2)
        st.write("step 3: Traning Model...")
        time.sleep(2)
        status.update(
            label="Process Completed ✅",
            state="complete"
        )
        st.balloons()
        st.snow()

st.write("Done!")


