import streamlit  as st
st.title("student marks")
data={
    "arshu":20,
    "rahul":100,
    "priya":90,
    "riya":70,
    "aman":95,
}
st.bar_chart(data)        