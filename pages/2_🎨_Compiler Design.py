import streamlit as st 
from streamlit_option_menu import option_menu


st. set_page_config(layout="wide")

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
    
    # Add more video URLs as needed
}

links = list(video_urls.keys())

tab1, tab2 = st.tabs(["VIdeos", "Notes"])



with tab1:
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

with tab2:
    st.markdown("""
## Unit - 1:
Updated soon...

                
## Unit - 2:
Updated soon...

                
## Unit - 3:
Updated soon...
           
                

## Unit - 4:
Updated soon...
       

            

## Unit - 5:
                
Updated soon...
""")