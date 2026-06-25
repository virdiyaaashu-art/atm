import streamlit as st
st.header("image converter")
st.title("1.RCB 2.SRH 3.RR 4.GT 5.CSK")
num=st.number_input("enter no")
if st.button("submit"):
    if num==1:
        st.image("https://cricketinshight.in/wp-content/uploads/2026/06/RCB-WON-CHAMPION.jpg")
    if num==2:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBKW0hHGEvpkZealuBR2vZasrsP5hGxIXOVdVgdnRe8eTh_1HUtLA8ldgm&s=10")
    if num==3:
        st.image("https://www.wallsnapy.com/img_gallery/riyan-parag-rr-captain-ipl-poster-wallpaper-4k-622.jpg")
    if num==4:
        st.image("https://static.toiimg.com/thumb/width-400,resizemode-4,msid-91880207/91880207.jpg")
    if num==5:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROmEiC73dQdxebcKngedlJVv-nEM4dtHxPje6VERMZ2agYEZeCQSHU8P4&s=10")               