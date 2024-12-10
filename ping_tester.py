# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st
import socket
import time


# ------------------------------------ MAIN APP ------------------------------------
def ping_server(host, port=80):
    """
    Checks the server's connectivity using a TCP socket and measures the response time.

    Parameters
    ----------
    host : str
        The hostname or IP address of the server to ping.
    port : int
        The port to attempt the connection (default is 80 for HTTP).

    Returns
    -------
    str
        A message indicating whether the server is reachable, and the measured response time.
    """
    try:
        # Record the start time
        start_time = time.time()
        with socket.create_connection((host, port), timeout=5) as s:
            # Record the end time
            end_time = time.time()
            # Calculate the connection time and convert to milliseconds
            connection_time = (end_time - start_time) * 1000
            return f'{host} is reachable on port {port}.', f'Connection time: {connection_time:.2f} ms'
    except (socket.timeout, socket.error) as e:
        return f'{host} is unreachable.', 'Please enter a valid host.'


st.title(":globe_with_meridians: Ping Tester")

st.write('Measures the connection time in milliseconds and checks the availability of the server or IP address using a TCP socket.')

st.divider()

# Input field for the server address
st.subheader(':gray[Enter the server or IP address to ping:]')
host = st.text_input("Enter the server or IP address to ping:", 'erincameron11.github.io', label_visibility='collapsed')

# Add a Ping button
if st.button('Ping'):
    # If the user has filled in a host / IP
    if host:
        result1, result2 = ping_server(host)
        st.subheader(f':blue[{result1}]')
        st.subheader(f':blue[{result2}]')