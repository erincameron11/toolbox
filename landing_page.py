# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st
import os


# ------------------------------------ MAIN APP ------------------------------------
def main() :    
    st.set_page_config(layout="wide")
    
    pages = {
        "ToolBox": [
            st.Page("app.py", title="Home"),
            st.Page("markdown_preview.py", title="Markdown Previewer"),
            # st.Page("json_formatter.py", title="JSON Formatter"),
            st.Page("word_counter.py", title="Word Counter"),
        ],
    }
    pg = st.navigation(pages)
    pg.run()


if __name__ == "__main__":
    main()