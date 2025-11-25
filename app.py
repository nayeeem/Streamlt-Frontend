import streamlit as st

# Title and text
st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

# Input and output
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Slider example
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is {age}.")
