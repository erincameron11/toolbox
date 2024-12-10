# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st


# ------------------------------------ MAIN APP ------------------------------------
st.title("JSON Validator")

st.divider()

st.write(":warning: Under Construction...")

st.subheader(':gray[Enter JSON here:]')
json = st.text_area("Enter JSON here:", "", height=250, label_visibility="collapsed")

def validate(json):
    """
    JSON General Rules
        Keys must always be strings enclosed in double quotes (" ").
        Strings must be enclosed in double quotes, not single quotes (' ' is not valid).
        Trailing commas (after the last element in an object or array) are not allowed.
        Whitespace (spaces, tabs, newlines) is allowed and generally ignored except inside strings.
    Steps:
    1. Check that the JSON starts with either a {} (object) or [] (array).
    2. Ensure keys are strings enclosed in double quotes.
    3. Check that values are one of the valid JSON types (string, number, boolean, object, array, or null).
    4. Ensure proper nesting of objects and arrays.
    5. Ensure there are no trailing commas.
    6. Check for balanced brackets ({}, []).
    """
    # Locate the first character, if it is a { = object, [ = array
    first_char = json[0]
    if first_char != '{' and first_char != '[':
        return False, 'JSON SThe first character should be a { or [.'
    else:
        return True, 'JSON Valid: The first character is a { or [.'


def json_object_validator(json):
    """
    Represents a collection of key/value pairs enclosed in curly braces {}.
    Keys must be strings enclosed in double quotes "key".
    Each key is separated by a colon :, followed by its associated value.
    Pairs are separated by commas.
    """
    # Check the first character is an opening double quote "
    first_char = json[0]
    if first_char != '"':
        return False, 'JSON Object Error: key must start with double quote.'
    # Skip all the string characters until the closing double quote "
    json_length = len(json)
    # while index < json_length:
        

    
if st.button('Validate'):
    # valid, error = validate(json)
    # valid, error = json_object_validator(json)
    # st.write(str(valid))
    st.subheader(":warning: Under Construction...")
# if something:
# st.subheader(':blue[Your JSON is valid!]')
# else
# st.subheader(':red[Your JSON is invalid!]')