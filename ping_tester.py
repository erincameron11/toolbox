# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st
from ping3 import ping


# ------------------------------------ MAIN APP ------------------------------------
st.title(":globe_with_meridians: Ping Tester")
# Other Options: :signal_strength: :satellite:

st.divider()

def ping_server(host):
    """
    Pings the server and measures the response time.

    Parameters
    ----------
    host : str
        The hostname or IP address of the server to ping.

    Returns
    -------
    str
        A message indicating whether the server is reachable and, if so, 
        the response time in milliseconds.
    """
    response_time = ping(host)
    # If there is no response time, the host is unreachable
    if response_time is None:
        return f"{host} is unreachable."
    # If there is a response time, return it
    else:
        response_time_ms = response_time * 1000
        return f"{host} responded in {response_time_ms:.2f} ms."

# Input field for the server address
st.subheader(':gray[Enter the server or IP address to ping:]')
host = st.text_input("Enter the server or IP address to ping:", 'erincameron11.github.io', label_visibility='collapsed')

# Add a Ping button
if st.button('Ping'):
    # If the user has filled in a host / IP
    if host:
        result = ping_server(host)
        st.subheader(f':blue[{result}]')
    else:
        st.write('Please enter a valid host.')