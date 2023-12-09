import streamlit as st 
from streamlit_option_menu import option_menu


st. set_page_config(layout="wide")

st.title("Distributed Computing")



st.write("###")
# List of video URLs
video_urls = {
    
    # Add more video URLs as needed
}

links = list(video_urls.keys())





c1,c2 = st.columns([7,3])

title = "Computer Networks"
# Sidebar to display video list
with c2:
    selected_video_index = option_menu(title, links,default_index=0)

with c1:
    st.markdown('### **'+selected_video_index+'**')
    st.video(video_urls[selected_video_index])


js = '''
<script>
    var body = window.parent.document.querySelector(".menu");
    console.log(body);
    body.scrollTop = 0;
</script>
'''

st.components.v1.html(js)
