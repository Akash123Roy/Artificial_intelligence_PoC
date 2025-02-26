import streamlit as st
import google.generativeai as genai
import streamlit as st
from io import BytesIO
from docx import Document
from docx.shared import Pt

# Configure the API key
genai.configure(api_key="AIzaSyBjKe4Wk6CUtT0oSG1pUaq4Sn0ER90JpGY")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_summary(row):
    input_text = f"CR_NO: {row['CR_NO']}\n:Change Description {row['Change Description']}\nJustification: {row['Justification']}\nGenerate summary in 100 words."
    response = model.generate_content([input_text])
    return response.text

def generate_summary_from_text(text_file):
    prompt = f"Generate summary in 100 words{text_file}"
    response = model.generate_content(prompt)
    return response.text


# Initialize session state for login status
if "login_status" not in st.session_state:
    st.session_state.login_status = False

# Sidebar header for login form
st.sidebar.header("Admin Login")

# If not logged in, show login form
if not st.session_state.login_status:
    # Username and password input fields
    username = st.sidebar.text_input("Username", placeholder="Enter your username")
    password = st.sidebar.text_input("Password", placeholder="Enter your password", type="password")

    # Login button
    if st.sidebar.button("Login"):
        # Check credentials (you can replace with your own validation logic)
        if username == "admin" and password == "password123":  # Replace with actual credentials
            st.sidebar.success("Login successful!")
            st.session_state.login_status = True
        else:
            st.sidebar.error("Invalid username or password.")
else:
    # Once logged in, display the admin features
    st.sidebar.success("Logged in as admin.")

# Streamlit UI
    st.title("Summary Generator")

        # Input option selection
    option = st.selectbox(
        "Choose input type",
        ("Text", "Excel", "CSV")
    )