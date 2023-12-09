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
    "Chandy Misra Haas for AND Model":"https://www.youtube.com/watch?v=KHeUv2wwt3g&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=36&pp=iAQB",
    "Chandy Misra Haas for OR Model":"https://www.youtube.com/watch?v=KHeUv2wwt3g&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=36&pp=iAQB",
    "Introduction to Consensus":"https://www.youtube.com/watch?v=uoy9ZnqB_84&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=38&pp=iAQB",
    "Byzantine agreement and other problem":"https://www.youtube.com/watch?v=_f9tQ0nTWKc&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=39&pp=iAQB",
    "Consensus Algorithm for Crash Failure":"https://www.youtube.com/watch?v=alchs2BBrAY&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=40&pp=iAQB",
    "Upper Bound on Byzantine process":"https://www.youtube.com/watch?v=aB-sxVShbLQ&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=41&pp=iAQB",
    "Byzantine Tree Recursive Algorithm":"https://www.youtube.com/watch?v=5gY15nZqrmc&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=42&pp=iAQB",
    "Byzantine Tree Iterative Algorithm":"https://www.youtube.com/watch?v=nUp7E_gbdYY&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=43&pp=iAQB",
    "Phase King Algorithm":"https://www.youtube.com/watch?v=AvSv2-nn_wA&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=44&pp=iAQB",
    "Checkpoint Basic":"https://www.youtube.com/watch?v=YMvgYJj7yMM&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=45&pp=iAQB",
    "Checkpoint Background and Definition":"https://www.youtube.com/watch?v=bfafK2t4xG0&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=46&pp=iAQB",
    "Type of Messages":"https://www.youtube.com/watch?v=cKOAa_CUgS8&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=47&pp=iAQB",
    "Issues in Failure Recovery":"https://www.youtube.com/watch?v=rvPp90o9Krw&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=48&pp=iAQB",
    "Checkpoint based Recovery - 1":"https://www.youtube.com/watch?v=fWp4AVla2cI&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=49&pp=iAQB,
    "Checkpoint based Recovery - 2":"https://www.youtube.com/watch?v=Ft93YGLNg_A&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=51&pp=iAQB",
    "Checkpoint based Recovery - 3":"https://www.youtube.com/watch?v=1M75AYwepjU&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=50&pp=iAQB",
    "Coordinate Checkpoint algorithm":"https://www.youtube.com/watch?v=Anz_52xBhjc&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=52&pp=iAQB",
    "Algorithm for Asynchronus Checkpoint and recovery - 1":"https://www.youtube.com/watch?v=eluy9_a0MT8&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=53&pp=iAQB",
    "Algorithm for Asynchronus Checkpoint and recovery - 2":"https://www.youtube.com/watch?v=-CRAI7yfgXo&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=54&pp=iAQB",
    "Introduction to Cloud Computing":"https://www.youtube.com/watch?v=SvcKxpAV-7A&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=55&pp=iAQB",
    "Characteristic of Cloud Computing":"https://www.youtube.com/watch?v=_qpUcuya5pU&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=56&pp=iAQB",
    "Cloud Deployment model":"https://www.youtube.com/watch?v=kdGgEdMxavY&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=57&pp=iAQB",
    "Cloud Service Model":"https://www.youtube.com/watch?v=Uc4B4odVGtY&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=58&pp=iAQB",
    "Message Ordering Paradigms":"https://www.youtube.com/watch?v=bg1ny7g0dQI&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=59&pp=iAQB",
    "Synchronous Program Order on Asynchronous System":"https://www.youtube.com/watch?v=RnMyyJQkcJk&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=60&pp=iAQB",
    "Casual Order":"https://www.youtube.com/watch?v=BKtid1yJ4HQ&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=61&pp=iAQB",
    "Total Order":"https://www.youtube.com/watch?v=agh2o3vvZHA&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=62&pp=iAQB",
    "Virtualization and Loading Balance":"https://www.youtube.com/watch?v=yhLI8Mln4EI&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=63&pp=iAQB",
    "Asynchronus Execution with Synchronus Communication":"https://www.youtube.com/watch?v=U89NWcw9jsg&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=64&pp=iAQB"
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
