import streamlit as st
from PIL import Image
from rembg import remove

st.title("Background Remover")

uploaded_file = st.file_uploader("Upload your Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(img, use_container_width=True)

    if st.button("Remove Background"):
        with st.spinner("Removing background, please wait..."):
            output = remove(img)

        st.subheader("Background Removed")
        st.image(output, use_container_width=True)
