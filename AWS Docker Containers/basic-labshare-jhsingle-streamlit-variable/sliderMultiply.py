import streamlit as st

#basic streamlit 
x = st.slider('X times X slider')
st.write(x, 'squared is', x * x)