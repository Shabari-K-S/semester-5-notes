import streamlit as st 

st.title("Semester 5 Notes")
st.write("This is a collection of notes for semester 5")

table = st.table(
    {
        "Computer Networks": "30-11-2023",
        "Compiler Design": "06-12-2023",
        "Cryptography and Cyber Security": "08-12-2023",
        "Distributed Computing": "12-12-2023",
        "UI and UX Design": "14-12-2023",
        "Web Technologiers": "18-12-2023"
    }
)