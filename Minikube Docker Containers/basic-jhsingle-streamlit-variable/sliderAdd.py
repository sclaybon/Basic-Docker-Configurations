import streamlit as st

#basic streamlit 
x = st.slider('X plus X slider')
st.write(x, 'plus x is', x + x)