import streamlit as st
import socket
import sys

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

st.title('hello world by ' + local_ip)
x = st.slider('x')
st.write(x, 'squared is', x * x)