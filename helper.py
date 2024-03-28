# Imports
import os
from hugchat import hugchat
from hugchat.login import Login
from dotenv import load_dotenv


# Load the environment variables
load_dotenv()


# Load the email and password from the environment variables
EMAIL = os.getenv("HUGCHAT_EMAIL")
PASSWD = os.getenv("HUGCHAT_PASSWD")


# Sign in to the HugChat
user = Login(email=EMAIL, passwd=PASSWD)


# Function to prepare the query
def prepare_query(user_inputs):
    # Initialize the query
    query = ""
    # query += "**Current Issue:**\n {user_input}\n"

    # Loop through the user inputs
    for key, value in user_inputs.items():
        # Add the key and value to the query
        query += f"{key}: {value}\n"

    # Add a new line at the end of the query
    # query += "Give me a solution for this issue or give me some information about it."
    

# Provide specific instructions tailored to an agriculture chatbot
    query += "Respond with the following, prioritizing in this order:\n* **Direct Solutions:** If you can provide a specific solution to the issue, do so clearly. Explain the steps involved and why this solution is recommended.\n* **Relevant Information:** Offer helpful agricultural information related to the issue. This might include causes, prevention methods, best practices, or further resources the user could explore.\n* **Contextual Understanding:** If the issue is complex or requires more information, acknowledge that and ask clarifying questions to help you provide a better solution. \n"

    # Return the query
    return query


# Function to get the chatbot
def get_chatbot():

    # Set the cookies path
    COOKIES_PATH = "cookies.json"

    # Save the cookies
    cookies = user.login(cookie_dir_path=COOKIES_PATH)

    # Initialize the chatbot
    chatbot = hugchat.ChatBot(
        cookies=cookies.get_dict(), default_llm="openchat/openchat-3.5-0106"
    )

    # Return the chatbot
    return chatbot


# Function to get the response from the chatbot
def get_response(user_inputs):
    # Get the chatbot
    chatbot = get_chatbot()

    # Prepare the query
    query = prepare_query(user_inputs)

    # Get the response from the chatbot
    response = chatbot.chat(query)

    # Return the response
    return response