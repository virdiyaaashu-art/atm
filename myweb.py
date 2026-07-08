import streamlit as st
st.title("my webside")
tab1, tab2, tab3, tab4 = st.tabs([
    "Home",
    "Profile",
    "Register",
    "Image Gallary"
])
with tab1:
    st.header("paragraph")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNalIUTbzljBh6LeXnHY8sD0RbM_HuQj9cl38yDngcwZhBA991V9_TYuEE&s=10")
with tab2:
    st.header("about myself")
    st.title("my name: tattvam kaneriya")
    st.title("my age: 8")
    st.title("my grade:3rd")
with tab3:
    st.header("Registration foam")
    name=st.text_input("enter name:")
    password=st.text_input("enter password")
    email=st.text_input("enter email")
    age=st.number_input("enter age,min_value=1, max_value=100")
    address=st.text_area("enter adderss")
    dob=st.date_input("Enter Date of Birth")
    city = st.selectbox(
    "Enter City",
    ["Ahmedabad", "Rajkot", "Surat", "Vadodara"]
)
    message=st.text_area("enter message")
    st.button("Register")    
with tab4:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0K2RLI6RZACXg1STy5QPtIOs0zy6ZtC5bXmc_ss0l_H6JjVqfZ4ly9go&s=10")
    st.image("https://png.pngtree.com/thumb_back/fh260/background/20240921/pngtree-black-hole-in-space-elements-of-this-image-furnished-by-nasa-image_16240818.jpg")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9WKe1L9spwPPSKdy5AP6zJ8GyuaqHHo-jKgRLB-22G_E8Dt_2yoEJlWY&s=10")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNfcHFcVYY8-T8xJl_XHrewd6RLiuWKyCChf3GsBt3q9GImE3rcPKzUHI&s=10")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ7311pIZBJattF9LxZzrfCT4TtHLz_wBmNdWk7HPkpmfC6KaXfx-ZIUo&s=10")
    st.image("https://i.pinimg.com/736x/55/5d/a8/555da82182113649fe742ce3cdb0e539.jpg")
    st.image("https://file.oyephoto.com/uploads/thumbnail/lord-bholenath-mobile-screen-wallpaper-4k-images-zc1qdji.webp")    


