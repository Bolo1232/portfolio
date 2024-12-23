import streamlit as st
import time
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Xevery Jan C. Bolo - Portfolio",
    page_icon="🌐",
    layout="wide"
)

# Add a custom header image
st.image("XEV2.jpg", width=800)  # Adjust the width as needed

# Title and Subtitle
st.title("My Autobiography & Portfolio")
st.subheader("Welcome to my personal page!")

# Autobiography Section
st.header("🖋️ About Me")
st.write("""
Hi, I'm **Xevery Jan C. Bolo**, a passionate web developer with a love for creating intuitive and impactful web applications.
Born and raised in **Sangat, San Fernando, Cebu**, I discovered my passion for technology at a young age. I am currently a **BSIT 4th year student**
at **Cebu Institute of Technology - University**, where I have honed my skills and built impactful projects.
""")

# Adding a Divider
st.markdown("---")

# Portfolio Section
st.header("🌐 Portfolio")

# Project 1
st.subheader("1. Library Management System")
st.write("""
Developed a **full-stack Library Management System** using **Spring Boot** and **React**. The system includes features like 
user authentication, book reservations, and administrative controls. Integrated **MySQL** for database management and 
used **Docker** for containerization.
""")
st.markdown("[View Project Design](https://www.figma.com/design/SZTIl3pVvPKt9ZOQnCCUwS/APP-DEV?node-id=0-1&p=f&t=RmXIrehwoiKRCBwX-0)")

# Project 2
st.subheader("2. CIT-University Library Access Monitoring and Time Management System")
st.write("""
The **CIT-University Library Access Monitoring and Time Management System** is a web-based application that automates the tracking of students' library hours and book logs. 
It integrates with the school's ID scanner system to record time in/out and automatically calculate total hours spent. 
The system enables manual book logging and provides tools for teachers and librarians to set required hours, approve logs, and generate reports. 
Its primary goals are to improve the efficiency of tracking library hours, ensure data accuracy, and simplify reporting for both students and faculty.
""")
st.markdown("[View Project Design](https://www.figma.com/design/jd8LrWFR43MV6DGTyuZdiH/UI?node-id=0-1&p=f&t=3CpwYpenacdSloin-0)")

# Project 3
st.subheader("3. FilipiKnow")
st.write("""
Online Learning Platform Provides a variety of resources including audio and video lessons, vocabulary lists, grammar explanations, and cultural insights to help learners of all levels improve their Filipino language skills. .
""")
st.markdown("[View Project Design](https://www.figma.com/design/0rVSEq3juKxm93aMEBhK1u/HCI?node-id=0-1&p=f&t=jNAbmQqqfF7zSbM3-0)")

# Adding a Divider
st.markdown("---")

# Contact Me Section
st.header("📧 Contact Me")
st.write("Feel free to reach out to me through the information below:")

# Displaying contact information
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Name:**")
    st.write("**Email:**")
    st.write("**Contact no:**")
with col2:
    st.write("Xevery Jan C. Bolo")
    st.write("[xeverybolo126@gmail.com](mailto:xeverybolo126@gmail.com)")
    st.write("09942854992")

# Adding Social Media Links
st.header("🔍 Find Me on Social Media")
st.write("""
- [👤 Facebook](https://www.facebook.com/profile.php?id=100008734368411)  
- [💻 GitHub](https://github.com/Bolo1232)  
""")

# Adding a Divider
st.markdown("---")

# Skills Section
st.header("🌟 Skills")
with st.expander("Programming Languages"):
    st.write("""
    - **Python** 
    - **Java** 
    - **JavaScript** 
    """)

with st.expander("Frameworks & Libraries"):
    st.write("""
    - **Spring Boot** 
    - **React** 
    - **Streamlit** 
    - **TensorFlow** 
    """)

with st.expander("Tools & Platforms"):
    st.write("""
    - **Docker** 
    - **MySQL** 
    - **Figma** 
    - **WordPress** 
    """)

# Adding a Divider
st.markdown("---")

# Location Section
st.header("🌎 Location")

# Coordinates for Sangat, San Fernando, Cebu
location_data = pd.DataFrame({
    'lat': [10.194],
    'lon': [123.7208]
})

st.map(location_data)

# Thank You Message
st.write(""" 
**🙏 Thank you for visiting my page!** 
""")
