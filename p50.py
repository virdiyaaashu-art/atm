import streamlit as st
num=st.number_input("enter no")
num=(int)(num)
if st.button("click"):
    for i in range(1,num+1):
        if i%5==0:
            st.write(i)