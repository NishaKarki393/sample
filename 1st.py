import streamlit as st
st.title('campus x')
col1,col2=st.columns(2)

with col1:
    st.image('https://images.shiksha.com/mediadata/images/1645702564phpzkLseO.jpegcl')

with col2:
    st.write("This is my campusx") 


st.sidebar.selectbox("Choose one",['1','2'])