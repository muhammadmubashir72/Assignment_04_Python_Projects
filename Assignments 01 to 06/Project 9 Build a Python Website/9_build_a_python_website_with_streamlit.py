import streamlit as st

# Website Title
st.title("👨‍💻 My Portfolio")

# Sidebar Navigation
menu = st.sidebar.radio("📌 Navigate", ["Home", "Projects", "Contact"])

if menu == "Home":
    st.header("Welcome to My Portfolio!")
    st.write("Hello! I'm a passionate developer skilled in Python, Streamlit, and more. 🚀")

elif menu == "Projects":
    st.header("🛠️ My Projects")
    st.write("- **Project 1:** AI-based Chatbot 🤖")
    st.write("- **Project 2:** E-commerce Website 🛒")
    st.write("- **Project 3:** Data Visualization Dashboard 📊")

elif menu == "Contact":
    st.header("📬 Get in Touch")
    st.write("📧 Email: example@email.com")
    st.write("📱 LinkedIn: [My Profile](https://linkedin.com)")

