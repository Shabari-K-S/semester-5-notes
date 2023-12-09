import streamlit as st 
from streamlit_option_menu import option_menu


st. set_page_config(layout="wide",page_title="Compiler Design",page_icon="🎨")


st.title("Compiler Design")


st.write("###")
st.write("###")
st.write("###")
# List of video URLs
video_urls = {
    "Introduction":"https://www.youtube.com/watch?v=5ZmFlxrNaN8&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=1&pp=iAQB",
    "Different Phase Of Compiler":"https://www.youtube.com/watch?v=TApMNhQPaCM&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=2&pp=iAQB",
    "Symbol Table":"https://www.youtube.com/watch?v=Dd3DWRpqI40&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=3&pp=iAQB",
    "Symbol Table Example":"https://www.youtube.com/watch?v=hVaAXOGxMWo&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=4&pp=iAQB",
    "Lexical Analyzer":"https://www.youtube.com/watch?v=4nx8LEGy9kI&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=5&pp=iAQB",
    "Lexical Analyzer - Example 1":"https://www.youtube.com/watch?v=izGDMglQzgY&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=7&pp=iAQB",
    "Lexical Analyzer - Example 2":"https://www.youtube.com/watch?v=POWFABRCujo&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=8&pp=iAQB",
    "Error And Recovery":"https://www.youtube.com/watch?v=J8cFZCUdfj8&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=9&pp=iAQB",
    "Formal Grammar":"https://www.youtube.com/watch?v=U-rg4nHeYiw&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=10&pp=iAQB",
    "Classificatio off Formal Grammar - 1":"https://www.youtube.com/watch?v=HkqgBqUjjS0&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=11&pp=iAQB",
    "Classification of Formal Grammar - 2":"https://www.youtube.com/watch?v=MONaMMwSz2E&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=12&pp=iAQB",
    "Deviation of CFG":"https://www.youtube.com/watch?v=3rzTRtjUM_I&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=13&pp=iAQB",
    "Ambiguity":"https://www.youtube.com/watch?v=gUaAKAj-rqA&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=14&pp=iAQB",
    "Ambiguity Example":"https://www.youtube.com/watch?v=i-xrAmOR314&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=15&pp=iAQB",
    "Ambiguity Example 2":"https://www.youtube.com/watch?v=_rcDHRk1_zo&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=16&pp=iAQB",
    "Problem Of Ambiguity in CFG":"https://www.youtube.com/watch?v=WqpkuM8UVss&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=17&pp=iAQB",
    "Associativity":"https://www.youtube.com/watch?v=zdlDl5fYuAA&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=18&pp=iAQB",
    "Precendence":"https://www.youtube.com/watch?v=fHQlQQELCYM&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=19&pp=iAQB",
    "Associativity and Precedence":"https://www.youtube.com/watch?v=q8uBrWsD4q4&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=20&pp=iAQB",
    "Associativity and Precedence - Example":"https://www.youtube.com/watch?v=OTWq5SkLg48&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=21&pp=iAQB",
    "Recurssion in CFG":"https://www.youtube.com/watch?v=g2hlbqob0lo&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=23&pp=iAQB",
    "Problem of Left Recurssion":"https://www.youtube.com/watch?v=IO5ie7GbJGI&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=24&pp=iAQB",
    "Elimination of Left Recurssion":"https://www.youtube.com/watch?v=PFey5FpKlFM&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=25&pp=iAQB",
    "Non-Deterministic CFG":"https://www.youtube.com/watch?v=BlVzfIghVw8&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=26&pp=iAQB",
    "Non-Deterministic CFG (Solved Problem)":"https://www.youtube.com/watch?v=s9N3_7ADZno&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=27&pp=iAQB",
    "Parser":"https://www.youtube.com/watch?v=OIKL6wFjFOo&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=29&pp=iAQB",
    "Top Down Parser -  Recursive Decent Parser":"https://www.youtube.com/watch?v=iddRD8tJi44&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=30&pp=iAQB",
    "Top Down Parser - LL(1) Parser":"https://www.youtube.com/watch?v=v_wvcuJ6mGY&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=31&pp=iAQB",
    "First and Follow":"https://www.youtube.com/watch?v=oOCromcWnfc&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=32&pp=iAQB",
    "First and Follow (Solved Problem)":"https://www.youtube.com/watch?v=jv4dwxukVvU&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=33&pp=iAQB",
    "LL(1) Parser Table":"https://www.youtube.com/watch?v=DT-cbznw9aY&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=35&pp=iAQB",
    "LL(1) Parsing":"https://www.youtube.com/watch?v=clkHOgZUGWU&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=36&pp=iAQB",
    "LL(1) Parsing (Solved Problem)":"https://www.youtube.com/watch?v=5P7ehgZ6EIs&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=37&pp=iAQB",
    "Bottom Up Parser":"https://www.youtube.com/watch?v=kQMIQQmmkj8&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=39&pp=iAQB",
    "Semantic Analysis":"https://www.youtube.com/watch?v=0i8q9Gubu6Q&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=40&pp=iAQB",
    "Intermediate COde Generator":"https://www.youtube.com/watch?v=SiYxGP0O68s&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=41&pp=iAQB",
    "Runtime Environment and Code Optimization":"https://www.youtube.com/watch?v=SaKfQX_tQrs&list=PLBlnK6fEyqRjT3oJxFXRgjPNzeS-LFY-q&index=42&pp=iAQB",

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
