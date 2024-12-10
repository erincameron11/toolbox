# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st
import os


# ------------------------------------ MAIN APP ------------------------------------
def main() :    
    st.set_page_config(layout="wide", page_icon=":wrench:")
    
    pages = {
        "ToolBox": [
            st.Page("app.py", title="Home"),
            st.Page("markdown_preview.py", title="Markdown Previewer"),
            # st.Page("json_validator.py", title="JSON Validator"),
            st.Page("word_counter.py", title="Word Counter"),
            st.Page("csv_viewer.py", title="CSV Viewer"),
            st.Page("ping_tester.py", title="Ping Tester"),
            st.Page("json_minifier.py", title="JSON Minifier"),
        ],
    }
    pg = st.navigation(pages)
    pg.run()


if __name__ == "__main__":
    main()