import streamlit as st 
from streamlit_option_menu import option_menu


st. set_page_config(layout="wide")

st.title("Cryptography and Cyber Security")


st.write("###")
st.write("###")
st.write("###")
# List of video URLs
video_urls = {
    "OSI Architecture":"https://www.youtube.com/watch?v=UG26SS9pjwE&ab_channel=NesoAcademy",
    "Security Attack":"https://www.youtube.com/watch?v=yIm0Ol9Dg4Y&ab_channel=NesoAcademy",
    "Security Services":"https://www.youtube.com/watch?v=bRgL_Dry7uw&ab_channel=NesoAcademy",
    "Security Mechanism":"https://www.youtube.com/watch?v=H5ifNVeDXkg&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=6&pp=iAQB",
    "Network security Model":"https://www.youtube.com/watch?v=zd0U1zNBYNk&ab_channel=NesoAcademy",
    "Ceaser Cipher - 1":"https://www.youtube.com/watch?v=JtbKh_12ctg&ab_channel=NesoAcademy",
    "Ceaser Cipher - 2":"https://youtu.be/na5rapg1XsI?si=9SDZB3AoPW1NOjvn",
    "Playfair Cipher - 1":"https://youtu.be/UURjVI5cw4g?si=3N0Lg_6UQQbwf3Xf",
    "Playfair Cipher - 2":"https://youtu.be/whEJfas9MAI?si=c0_Tf0nz5T3z95Wb",
    "Monoalphabetic Cipher":"https://youtu.be/J-utjSeUq_c?si=_6GpY2dEgNa0SCd4",
    "Hill Cipher Encryption":"https://youtu.be/-EQ8UomTrAQ?si=jaG44c1yZI0YJ4Cw",
    "Hill Cipher Decryption":"https://youtu.be/JK3ur6W4rvw?si=OVirZzXMRFsGUJre",
    "Polyalphabetic Cipher (Vigenère Cipher)":"https://youtu.be/Ic4BzVggNY8?si=q0Ehr4xI02HEfpWi",
    "Polyalphabetic Cipher (Vernam Cipher) ":"https://youtu.be/Qojvtgf7SQw?si=Ld4KJyOm2nZwpYc6",
    "One Time Pad":"https://youtu.be/6iYqHn3q8sY?si=iVkt4RSL-oRrmlrr",
    "Rail Fence Technique":"https://youtu.be/knE4G8DGLoY?si=rbZbwOsg5jP3mZ1w",
    "Row Column Transposition Ciphering Technique":"https://youtu.be/cPQXaYUMOjQ?si=es6uUQuPw4gkRv0M",
    
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