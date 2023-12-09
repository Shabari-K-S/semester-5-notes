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
    "Stegenography":"https://www.youtube.com/watch?v=Te8Cao2Smsk&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=26&pp=iAQB",
    "Number Theory":"https://www.youtube.com/watch?v=5PY2RvI_JnA&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=29&pp=iAQB",
    "Prime number Theory":"https://www.youtube.com/watch?v=5J3l894CiMI&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=30&pp=iAQB",
    "Modular Arithmetic - 1":"https://www.youtube.com/watch?v=M42uDLGRSpI&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=31&pp=iAQB",
    "Modular Arithmetic - 2":"https://www.youtube.com/watch?v=P7P03gg3msE&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=32&pp=iAQB",
    "Modular Exponentation - 1":"https://www.youtube.com/watch?v=_gYUlvcnjs0&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=33&pp=iAQB",
    "Modular Exponentation - 2":"https://www.youtube.com/watch?v=bg0P_3UiG5I&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=34&pp=iAQB",
    "GCD - Euclidean Algorithm - 1":"https://www.youtube.com/watch?v=yHwneN6zJmU&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=35&pp=iAQB",
    "GCD - Euclidean Algorithm - 2":"https://www.youtube.com/watch?v=svBx8u5bMEg&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=36&pp=iAQB",
    "Relative Prime( Co-Prime) Number":"https://www.youtube.com/watch?v=csIL-mWTQss&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=37&pp=iAQB",
    "Euler’s Totient Function (Phi Function)":"https://www.youtube.com/watch?v=DwQ7-k9LkJ4&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=38&pp=iAQB",
    "Euler’s Totient Function (Solved Examples)":"https://www.youtube.com/watch?v=osge0_lZTaY&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=39&pp=iAQB",
    "Fermit's Little Theorem":"https://www.youtube.com/watch?v=3Cb0ys-jppU&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=40&pp=iAQB",
    "Eular's Theorem":"https://www.youtube.com/watch?v=DyOv20d4c70&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=41&pp=iAQB",
    "Primitive Roots":"https://www.youtube.com/watch?v=DKy98FWHwdg&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=42&pp=iAQB",
    "Multiplicative Inverse":"https://www.youtube.com/watch?v=YwaQ4m1eHQo&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=43&pp=iAQB",
    "Extended Euclidean Algorithm (Example Solved)":"https://www.youtube.com/watch?v=lq285DDdmtw&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=44&pp=iAQB",
    "Chinese Remainder Theorem (Example Solved)":"https://www.youtube.com/watch?v=e8DtzQkjOMQ&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=47&pp=iAQB",
    "Group and Abilean Group":"https://www.youtube.com/watch?v=8TjYHK804mU&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=54&pp=iAQB",
    "Cyclic Group":"https://www.youtube.com/watch?v=OGCRccWi4OE&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=55&pp=iAQB",
    "Ring, Field and Finite Field":"https://www.youtube.com/watch?v=oBL-Cb5GxA0&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=56&pp=iAQB",
    "Stream Cipher and Block Cipher":"https://www.youtube.com/watch?v=3adBPqIB4Tw&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=57&pp=iAQB",
    "Feistal Cipher":"https://www.youtube.com/watch?v=8l9xAvuGJFo&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=58&pp=iAQB",
    "DES":"https://www.youtube.com/watch?v=j53iXhTSi_s&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=59&pp=iAQB",
    "Single Round DES Algorithm":"https://www.youtube.com/watch?v=nynAQ593HdU&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=60&pp=iAQB",
    "The F Function of DES":"https://www.youtube.com/watch?v=OePPcJR--F4&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=61&pp=iAQB",
    "Key Scheduling and Decryption in DES":"https://www.youtube.com/watch?v=S-vLA7d1ORI&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=62&pp=iAQB",
    "Alavanche Effect and Strength of DES":"https://www.youtube.com/watch?v=kF_h9gl-vyw&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=63&pp=iAQB",
    "DES (Solved Question)":"https://www.youtube.com/watch?v=WQf43AKWBbY&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=64&pp=iAQB",
    "AES":"https://www.youtube.com/watch?v=3MPkc-PFSRI&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=65&pp=iAQB",
    "AES Encryption and Decryption":"https://www.youtube.com/watch?v=4KiwoeDJFiA&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=66&pp=iAQB",
    "AES Round Transformation":"https://www.youtube.com/watch?v=IpuvKyeCrvU&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=67&pp=iAQB",
    "AES Key Expansion":"https://www.youtube.com/watch?v=0RxLUf4fxs8&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=68&pp=iAQB",
    "Multiple Encription and Triple DES":"https://www.youtube.com/watch?v=4R_kocR1roM&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=70&pp=iAQB",
    "Block Cipher Code of Operation":"https://www.youtube.com/watch?v=VmNk-6GTqRE&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=71&pp=iAQB",
    "Electronic Code Block":"https://www.youtube.com/watch?v=jDnenb9EHQk&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=72&pp=iAQB",
    "Cipher Block Chaining":"https://www.youtube.com/watch?v=nnQONZ_DRyk&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=73&pp=iAQB",
    "Cipher Feedback":"https://www.youtube.com/watch?v=c_9MABuOVJI&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=74&pp=iAQB",
    "Output Feedback":"https://www.youtube.com/watch?v=OGdBTfouuao&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=75&pp=iAQB",
    "Counter Mode":"https://www.youtube.com/watch?v=zX0PZtqerCI&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=76&pp=iAQB",
    "Block Cipher Mode of Operation (Solved Problem)":"https://www.youtube.com/watch?v=tVmEFI_R4bA&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=77&pp=iAQB",
    "Pesudorandom Number Generator":"https://www.youtube.com/watch?v=q2XVhTWJ-Oo&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=78&pp=iAQB",
    "Golomb’s Randomness Postulates":"https://www.youtube.com/watch?v=6agTBs3c89o&list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&index=79&pp=iAQB",
    
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
