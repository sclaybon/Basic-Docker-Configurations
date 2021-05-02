import streamlit as st

#basic streamlit 
x = st.slider('Pemdas Slider')
st.write(x, 'times x plus x is', x * x + x)