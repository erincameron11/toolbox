# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st
import pyperclip
import time


# ------------------------------------ MAIN APP ------------------------------------
def minify(json):
    """
    Remove all whitespaces, tabs and linebreaks from a JSON string.

    Parameters
    ----------
    json : str
        The JSON string to be minified.

    Returns
    -------
    str
        A new string representing the minified JSON without any whitespace, tab, linebreak characters.
        
    Example
    --------
    Input: minify('
            {
                "name": "Erin", 
                "age": 32, 
                "city": "Toronto"
            }
        ')
    Output: '{"name":"Erin","age":32,"city":"Toronto"}'
    """
    minified_json = ''
    for index in range(0, len(json)):
        if json[index] != '\n' and json[index] != '\t' and json[index] != '\r' and json[index] != ' ':
            minified_json += json[index]
    return minified_json

st.title(":scissors: JSON Minifier")

st.write('Converts JSON into a single line without any extra spaces or indentation for more efficient data transfer or storage.')

st.divider()

# Add subheader and text input for JSON
st.subheader(':gray[Enter JSON here:]')
json = st.text_area('Enter JSON here:', "", height=250, label_visibility='collapsed')

# Initialize the session state for minified_json
if 'minified_json' not in st.session_state:
    st.session_state.minified_json = ''

# If the Minify button was clicked
if st.button('Minify'):
    # Check if JSON text field is empty
    if not json:
        # Store in the session_state
        st.session_state.minified_json = minify(json)
        st.error('Please enter JSON before clicking the Minify button!')
    else:
        # Store in the session_state, and display the output
        st.session_state.minified_json = minify(json)

# If it exists, display minified JSON output
if st.session_state.minified_json:
    st.subheader(':blue[Output:]')
    st.write(st.session_state.minified_json)

    # Add a copy JSON button
    if st.button('Copy Minified JSON'):
        # if st.session_state.minified_json:
            st.session_state.minified_json = minify(json)
            if not st.session_state.minified_json:
                st.error('Nothing to copy. Please minify JSON first.')
            else:
                pyperclip.copy(st.session_state.minified_json)
                st.success('Minified JSON copied successfully!')