# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st


# ------------------------------------ MAIN APP ------------------------------------
st.title(":v: Word Count")

st.divider()

st.subheader(':gray[Enter text here:]')
text = st.text_area("Enter text here:", "", height=200, label_visibility="collapsed")

# Locate the individual words and characters
words = text.split()
characters = len(text)

if st.button('Count'):
    st.subheader(f':blue[{len(words)} words {characters} characters]')