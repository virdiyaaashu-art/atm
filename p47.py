import streamlit as st
st.header("music list")
st.title("1.Ranchhod Rangila 2.Dwarika No Naath 3.Namo Namo 4.Moti Veraana 5.Radha Gori Gori")
num=st.number_input("enter no")
num=int(num)
if st.button("submit"):
    if num==1:
        st.video("https://youtu.be/-6oAZwTGD2c?si=K2J6WZDFAo6z5N7j")
    if num==2:
        st.video("https://youtu.be/4CMFhc8N6gk?si=-hwSmHLR1guJ19tL")
    if num==3:
        st.video("https://youtu.be/yALvgZi-84o?si=9PXzUTZSEClL1zgA")
    if num==4:
        st.video("https://youtu.be/Jv8KRwF1zQs?si=byZlwzJK0fcxM7-y")
    if num==5:
        st.video("https://youtu.be/xVU2UDaFOfE?si=5TaVpHkgkJP0rCFq")                