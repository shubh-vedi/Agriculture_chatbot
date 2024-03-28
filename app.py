# Imports
import streamlit as st
from helper import get_response

# Configure the page
st.set_page_config(
    page_title="AgroGPt🌾",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Title of the page
st.markdown("# AgroGPt 🌾")
st.markdown("#### **Welcome to the AgroGPt! 🚜🌾**")
st.markdown("#### **Your AI-powered farming assistant. Implies a helpful companion for agricultural tasks🌾**")

st.markdown("<br>", unsafe_allow_html=True)

# Initialize a list to store conversation history
conversation_history = []

# Function to display conversation history
def display_history(history):
    st.markdown("### **Conversation History:**")
    for item in history:
        st.markdown(f"**User:** {item['user_input']}")
        st.markdown(f"**Bot:** {item['bot_response']}")
        st.markdown("---")

# Field to take user input for Issue Description
issue_description = st.text_area("Issue Description", placeholder="Describe the issue you are facing...")

# Dropdown for language selection
selected_language = st.selectbox("Select Language", ["English", "Hindi", "Bengali", "Telugu", "Marathi", "Tamil"])

# Button to submit the user inputs
if st.button("Submit"):
    # Check for empty fields
    if issue_description == "":
        st.error("Please fill the Issue Description field!")
    else:
        # Add current user input to conversation history
        conversation_history.append({"user_input": issue_description, "bot_response": ""})
        
        # Get the response from the chatbot
        bot_response = get_response({"Issue Description": issue_description, "Selected Language": selected_language})
        
        # Add bot response to conversation history
        conversation_history[-1]["bot_response"] = bot_response
        
        # Display entire conversation history
        display_history(conversation_history)
