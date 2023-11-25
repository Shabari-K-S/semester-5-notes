import streamlit as st 
from streamlit_option_menu import option_menu

st.title("Computer Network")

st.write("###")
st.write("###")
st.write("###")
# List of video URLs
video_urls = {
    "Hi":"https://www.youtube.com/watch?v=cIlicbQnRyM",
    "hello":"https://www.youtube.com/watch?v=Mo45zViVSC4",
    # Add more video URLs as needed
}

links = list(video_urls.keys())

c1,c2 = st.columns([7,3])

title = "Unit-1"
# Sidebar to display video list
with c2:
    selected_video_index = option_menu(title, links,default_index=1)

with c1:
    st.video(video_urls[selected_video_index])
