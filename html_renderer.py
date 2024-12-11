# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st
import pyperclip


# ------------------------------------ MAIN APP ------------------------------------
st.title(":page_facing_up: HTML Renderer")

st.divider()

# Create columns for input and output
html_input_col, html_output_col = st.columns(2, gap='large')

# Create a text area with sample html in it
with html_input_col:
    st.subheader(':gray[Enter HTML here:]')
    html = st.text_area("Enter HTML here:", """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Erin Cameron's Website</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>

    <main>
        <!-- Hero Section -->
        <section id="home" class="hero">
            <h1>Welcome to Erin Cameron's Website</h1>
            <p>Your go-to hub for projects, portfolio, and more!</p>
        </section>

        <!-- About Section -->
        <section id="about">
            <h2>About Me</h2>
            <p>Hi! I'm Erin Cameron, a Computer Science enthusiast, with an interest in Web Development, Data Analytics and Cyber Security.</p>
        </section>

        <!-- Portfolio Section -->
        <section id="portfolio">
            <h2>Portfolio</h2>
            <div class="projects">
                <div class="project">
                    <h3>Recursive Descent Parser</h3>
                    <p>A Java program that analyzes the validity of an input files’ lexical syntax for a hypothetical imperative programming language.</p>
                </div>
            </div>
        </section>
    </main>
    </br>

    <footer>
        <p>&copy; 2024 Erin Cameron. All rights reserved.</p>
    </footer>
</body>
</html>
""", height=600, label_visibility="collapsed")

# Add columns to ensure buttons gare on the same lines
col1, col2 = st.columns([1, 2.2])

with col1:
    # Add a copy text button
    if st.button('Copy Text'):
        pyperclip.copy(html)
        html_copied = st.success('HTML copied successfully!')
        time.sleep(1) # Wait for 1 second
        html_copied.empty() # Eliminate the success message
with col2:
    # Add a download button for markdown content
    st.download_button('Download HTML', html, file_name='html_output.html', mime='text/html')

# Display the output markdown
with html_output_col:
    st.subheader(':blue[Output:]')
    with st.container(border=True):
        st.html(html)