import streamlit as st 
from streamlit_option_menu import option_menu

st.title("Web Technology")

st.write("###")
# List of video URLs
video_urls = {
    "Internet History":"https://www.youtube.com/watch?v=Oh93xiKv-Jg&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&ab_channel=Education4u",
    "Internet services":"https://www.youtube.com/watch?v=72z8C9WM8x0&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=2&ab_channel=Education4u",
    "World Wide Web(WWW)":"https://www.youtube.com/watch?v=yoJPysX1xzU&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=3&ab_channel=Education4u",
    "HTML tutorial":"https://www.youtube.com/watch?v=4bg2AUp6Y8w&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=4&ab_channel=Education4u",
    "HTML tags - 1":"https://www.youtube.com/watch?v=GMun4-g5Y6E&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=5&ab_channel=Education4u",
    "HTML tags - 2":"https://www.youtube.com/watch?v=rTYhLG7PgCM&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=6&ab_channel=Education4u",
    "HTML tags - 3":"https://www.youtube.com/watch?v=iO2X3D9jFfM&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=7&ab_channel=Education4u",
    "HTML Tables":"https://www.youtube.com/watch?v=A3NIKULhZls&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=8&ab_channel=Education4u",
    "Anchor and Image":"https://www.youtube.com/watch?v=cJ7CM8rvqgU&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=9&ab_channel=Education4u",
    "Frames":"https://www.youtube.com/watch?v=A1XlIDDXgwg&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=10&ab_channel=Education4u",
    "Forms":"https://www.youtube.com/watch?v=4zj9OAHxb5E&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=11&ab_channel=Education4u",
    "Form Attributes":"https://www.youtube.com/watch?v=LfYIwJN2n-I&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=12&ab_channel=Education4u",
    "CSS" :"https://www.youtube.com/watch?v=kk_pfNxU1AM&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=13&ab_channel=Education4u",
    "Internal CSS":"https://www.youtube.com/watch?v=kk_pfNxU1AM&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=13&ab_channel=Education4u",
    "External CSS - 1":"https://www.youtube.com/watch?v=kk_pfNxU1AM&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=13&ab_channel=Education4u",
    "External CSS - 2":"https://www.youtube.com/watch?v=VEZ7CT6w4FY&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=16&ab_channel=Education4u",
    "Inline CSS":"https://www.youtube.com/watch?v=tXdf6MPGPpk&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=17&ab_channel=Education4u",
    "CSS Box Model":"https://www.youtube.com/watch?v=70zTtCEaCG8&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=18&ab_channel=Education4u",
    "CSS List":"https://www.youtube.com/watch?v=kJaJNjNzjqc&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=19&ab_channel=Education4u",
    "DHTML":"https://www.youtube.com/watch?v=a-_SKo17FKA&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=20&ab_channel=Education4u",
    "XML":"https://www.youtube.com/watch?v=pCmPduLzD0k&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=21&ab_channel=Education4u",
    "Declaration and Doc":"https://www.youtube.com/watch?v=iLC12EinND0&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=22&ab_channel=Education4u",
    "WML":"https://www.youtube.com/watch?v=sN1usZH00C4&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=23&ab_channel=Education4u",
    "Javascript":"https://www.youtube.com/watch?v=J2q0x70YDPk&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=24&ab_channel=Education4u",
    "Javascript syntax":"https://www.youtube.com/watch?v=YGOhbWBcOPE&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=25&ab_channel=Education4u",
    "Implementing JS":"https://www.youtube.com/watch?v=Ia09ZN2-_e8&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=26&ab_channel=Education4u",
    "Variables and Scope":"https://www.youtube.com/watch?v=DwWtu7VLTwg&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=27&ab_channel=Education4u",
    "JS functions":"https://www.youtube.com/watch?v=rmvnFH_obhE&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=28&ab_channel=Education4u",
    "JS Array - 1":"https://www.youtube.com/watch?v=nyhRPNOE1X8&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=29&ab_channel=Education4u",
    "JS Array - 2":"https://www.youtube.com/watch?v=XMY5j-ZE238&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=30&ab_channel=Education4u",
    "JS Object - 1":"https://www.youtube.com/watch?v=1YEJS1mMMhA&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=31&ab_channel=Education4u",
    "JS Object - 2":"https://www.youtube.com/watch?v=JMHRlvrAa1A&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=32&ab_channel=Education4u",
    "Built-in JS functions":"https://www.youtube.com/watch?v=LBKNGrPNZSE&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=33&ab_channel=Education4u",
    "JS Event Handling":"https://www.youtube.com/watch?v=2vKBqzl6zAU&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=34&ab_channel=Education4u",
    "Java Servlet":"https://www.youtube.com/watch?v=UoG9kH5BoBY&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=35&ab_channel=Education4u",
    "Servlet Architecture":"https://www.youtube.com/watch?v=Dt9zvPeRPjU&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=36&ab_channel=Education4u",
    "Life Cycle Of Servlet":"https://www.youtube.com/watch?v=SpOWu3NHFIw&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=37&ab_channel=Education4u",
    "Parameter Data - 1":"https://www.youtube.com/watch?v=t4w71DCNuVw&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=38&ab_channel=Education4u",
    "Parameter Data - 2":"https://www.youtube.com/watch?v=wq7pRoKUV1o&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=39&ab_channel=Education4u",
    "Session Tracking":"https://www.youtube.com/watch?v=5SIJnF7hqak&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=40&ab_channel=Education4u",
    "Cookies - 1":"https://www.youtube.com/watch?v=_w2TYBy_7L0&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=41&ab_channel=Education4u",
    "Cookies - 2":"https://www.youtube.com/watch?v=BgEcYGXEklI&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=42&ab_channel=Education4u",
    "Servlet and Concurrency":"https://www.youtube.com/watch?v=p2vPH8Babbg&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=44&ab_channel=Education4u",
    # Add more video URLs as needed
}

links = list(video_urls.keys())

c1,c2 = st.columns([7,3])

title = "Web Technology"
# Sidebar to display video list
with c2:
    selected_video_index = option_menu(title, links,default_index=1)

with c1:
    st.video(video_urls[selected_video_index])
