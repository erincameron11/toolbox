# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st
import pyperclip
import time


# ------------------------------------ MAIN APP ------------------------------------
st.title(":eyes: Markdown Previewer")

st.divider()

# Create columns for input and output
markdown_input_col, markdown_output_col = st.columns(2, gap='large')

# Create a text area with sample markdown in it
with markdown_input_col:
    st.subheader(':blue[Enter Markdown here:]')
    markdown = st.text_area("Enter Markdown here:", """# Example Output
---
What to do:
1. Type markdown in this text area
2. Press Enter
3. View your previewed markdown to the right - make edits, and preview it real-time!
""", height=400, label_visibility="collapsed")

# Add columns to ensure buttons are on the same lines
col1, col2 = st.columns([1, 2.2])

with col1:
    # Add a copy text button
    if st.button('Copy Text'):
        pyperclip.copy(markdown)
        text_copied = st.success('Text copied successfully!')
        time.sleep(1) # Wait for 5 seconds
        text_copied.empty() # Eliminate the success message
with col2:
    # Add a download button for markdown content
    st.download_button('Download Markdown', markdown, file_name='markdown_output.md', mime='text/markdown')

# Display the output markdown
with markdown_output_col:
    st.subheader(':blue[Output:]')
    with st.container(border=True):
        st.write(markdown)