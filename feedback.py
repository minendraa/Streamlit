import streamlit as st

st.title("Feedback form")

name=st.text_input("Enter your name: ")
rating=st.slider("Rate your experience (1 = Bad, 5 = Excellent)",1,5)
comments = st.text_area("Any additional comments")

if st.button("Submit"):
    st.success("Feedback submitted successfully!!")
    st.write("Submitted info: ")
    st.write(f"Name: {name}")
    st.write(f"Rating: {rating}")
    st.write(f"Comments: {comments if comments else 'No comments'}")
    