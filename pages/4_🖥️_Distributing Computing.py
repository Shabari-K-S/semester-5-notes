import streamlit as st 
from streamlit_option_menu import option_menu


st. set_page_config(layout="wide")

st.title("Distributed Computing")



st.write("###")
# List of video URLs
video_urls = {
    "What is distrbuted Computing":"https://www.youtube.com/watch?v=lySvlsHtBzM&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=3&pp=iAQB",
    "Benefits of distrbuted Computing":"https://www.youtube.com/watch?v=1DecxFubdlw&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=4&pp=iAQB",
    "Relation with System Components":"https://www.youtube.com/watch?v=32vwQz67JKk&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=5&pp=iAQB",
    "Distributec vs parallal Computing":"https://www.youtube.com/watch?v=-r33V9Pw4iE&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=6&pp=iAQB",
    "Message Passing vs Shared Memory":"https://www.youtube.com/watch?v=FZ2fBkK31Wc&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=7&pp=iAQB",
    "Primitives for Distributed Computing - 1":"https://www.youtube.com/watch?v=rdIzsfc7caU&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=8&pp=iAQB",
    "Primitives for Distributed Computing - 2":"https://www.youtube.com/watch?v=xrxuPOPXkkc&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=9&pp=iAQB",
    "Synchoronous vs Asynchoronous":"https://www.youtube.com/watch?v=wGr65b5HXKA&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=10&pp=iAQB",
    "Design Issues and Challenge - 1":"https://www.youtube.com/watch?v=Ej3OiG2-6B8&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=11&pp=iAQB",
    "Design Issues and Challange - 2":"https://www.youtube.com/watch?v=rWMMyY3mq_g&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=12&pp=iAQB",
    "Distributed program":"https://www.youtube.com/watch?v=TvtFacEeU2o&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=13&pp=iAQB",
    "Model of Communication network":"https://www.youtube.com/watch?v=pSew2vnmumA&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=14&pp=iAQB",
    "Global State of Distribution System":"https://www.youtube.com/watch?v=0ae_V9BQvEQ&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=15&pp=iAQB",
    "Logical Clock Basics":"https://www.youtube.com/watch?v=Hu208M7T6R4&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=17&pp=iAQB",
    "Physical Clock Synchronization using NTP":"https://www.youtube.com/watch?v=QEHxlxJF7g8&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=18&pp=iAQB",
    "Framework for logical clock":"https://www.youtube.com/watch?v=a5MaMWXB_e0&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=19&pp=iAQB",
    "Scalar Time":"https://www.youtube.com/watch?v=BPHgY4iI5ms&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=20&pp=iAQB",
    "Vector Time":"https://www.youtube.com/watch?v=ueWDUxGHF_k&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=21&pp=iAQB",
    "Global State":"https://www.youtube.com/watch?v=T25bnhg5piM&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=22&pp=iAQB",
    "System model Definition":"https://www.youtube.com/watch?v=esym6rotTy4&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=23&pp=iAQB",
    "Chandral Lamport Snapshot Algorithm":"https://www.youtube.com/watch?v=l101NMxx2hc&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=24&pp=iAQB",
    "Introduction to MUX":"https://www.youtube.com/watch?v=rNBfoQj6RME&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=25&pp=iAQB",
    "Preliminaries of MUX":"https://www.youtube.com/watch?v=zQb-9dR4Hlw&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=26&pp=iAQB",
    "Lamport Algorithm of MUX":"https://www.youtube.com/watch?v=IHmixOPOFRM&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=27&pp=iAQB",
    "lamport Algorithm Proof":"https://www.youtube.com/watch?v=yJeIe2ZfWG0&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=28&pp=iAQB",
    "Ricart Agarwala Algorithm - 1":"https://www.youtube.com/watch?v=_bTLQC9bHPM&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=29&pp=iAQB",
    "Ricart Agarwala Algorithm - 2":"https://www.youtube.com/watch?v=KInZ3ukchks&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=30&pp=iAQB",
    "Susuki Kasami Algorithm - 1":"https://www.youtube.com/watch?v=ezaKOAUBomw&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=31&pp=iAQB",
    "Susuki Kasami Algorithm - 2":"https://www.youtube.com/watch?v=hizWxLaQD0E&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=32&pp=iAQB",
    "Deadlock Basic - 1":"https://www.youtube.com/watch?v=xfXfaToNIZE&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=33&pp=iAQB",
    "Deadlock Basic - 2":"https://www.youtube.com/watch?v=G5OvWW_EfXI&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=34&pp=iAQB",
    "Models Of Deadlock":"https://www.youtube.com/watch?v=qRlxuLIf7Do&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=35&pp=iAQB",

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
