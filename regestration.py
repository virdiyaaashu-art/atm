import streamlit as st

st.set_page_config(page_title="Registration Form", page_icon="📝")

st.title("📝 Registration Form")

with st.form("registration_form"):

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    mobile = st.text_input("Mobile Number")
    dob = st.date_input("Date of Birth")

    gender = st.radio(
        "Gender",
        ["Male", "Female", "Other"],
        horizontal=True
    )

    country = st.selectbox(
        "Country",
        ["India", "USA", "Canada", "Australia"]
    )

    address = st.text_area("Address")

    agree = st.checkbox("I accept the Terms & Conditions")

    submit = st.form_submit_button("Register")

if submit:
    if not agree:
        st.error("Please accept the Terms & Conditions.")
    elif name == "" or email == "" or password == "":
        st.warning("Please fill all required fields.")
    else:
        st.success("🎉 Registration Successful!")

        st.subheader("Registration Details")

        st.write("**Full Name:**", name)
        st.write("**Email:**", email)
        st.write("**Mobile:**", mobile)
        st.write("**Date of Birth:**", dob)
        st.write("**Gender:**", gender)
        st.write("**Country:**", country)
        st.write("**Address:**", address)