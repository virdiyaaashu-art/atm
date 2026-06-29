import streamlit as st
st.header("test")
q1=st.radio("q1.What is the national animal of India?",["Lion","Elephant","Tiger","Deer"])
q2=st.radio("q2.What is the national bird of India?",["Sparrow","Peacock","Parrot","Crow"])
q3=st.radio("q3.What is the national flower of India?",["Rose","Sunflower","Lotus","Lily"])
q4=st.radio("q4.What is the national fruit of India?",["Apple","Mango","Banana","Orange"])
q5=st.radio("q5.What is the capital of India?",["Mumbai","Chennai","New Delhi","Kolkata"])
q6=st.radio("q6.Which planet is called the Red Planet?",["Earth","Mars","Venus","Jupiter"])
q7=st.radio("q7.How many days are there in a week?",[5,6,7,8])
q8=st.radio("q8.Which animal is known as the King of the Jungle?",["Tiger","Lion","Elephant","Bear"])
q9=st.radio("q9.Which is the largest animal on Earth?",["Elephant","Blue Whale","Giraffe","Shark"])
q10=st.radio("q10.How many colors are there in a rainbow?",[5,6,7,8,])
mark=0
if st.button("submit"):
    if q1=="Tiger":
        mark=mark+1
    if q2=="Peacock":
        mark=mark+1
    if q3=="Lotus":
         mark=mark+1
    if q4=="Mango":
         mark=mark+1
    if q5=="New Delhi":
        mark=mark+1
    if q6=="Mars":
        mark=mark+1
    if q7==7:
        mark=mark+1
    if q8=="Lion":
        mark=mark+1
    if q9=="Blue Whale":
        mark=mark+1
    if q10==7:
        mark=mark+1
    st.write(mark)
    if mark>8:
        st.write("vary good")
        st.balloons()
    elif mark<=8 and mark>6:
        st.write("good")
    elif mark<=6 and mark>4:
        st.write("avg")
       
    else:
        st.write("try again")




