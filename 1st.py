import streamlit as st
st.title('campus x')
col1,col2=st.columns(2)

with col1:
<<<<<<< HEAD
    st.image('https://th.bing.com/th/id/R.6af6fd9c37f0de4abb34ea0fd20acce3?rik=55mqMmrTutVR0Q&pid=ImgRaw&r=0')
=======
    st.image('https://images.shiksha.com/mediadata/images/1645702564phpzkLseO.jpegcl')
>>>>>>> sidebar

with col2:
    st.write("This is my campusx") 


st.sidebar.selectbox("Choose one",['1','2'])
st.sidebar.selectbox("Select one",['Teacher','Student'])
st.sidebar.button('select')