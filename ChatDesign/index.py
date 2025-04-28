import streamlit as st
import datetime
import time
from MyModel import MyModel
from IntentModel import IntentModel
import os 
from datetime import datetime

current_datetime = datetime.now()
# Load the models
model = MyModel()
intent = IntentModel()

try:

    st.set_page_config(page_title="ChatNova")

    # Check if 'chat_history' exists in session state, if not, initialize it
    if 'chat_history' not in st.session_state:
        st.balloons()
        st.session_state['chat_history'] = []


    def save_conversation_to_file(filename="history/chat_history.txt"):
        with open(filename, "a") as f:  # Open the file in append mode
            for msg in st.session_state['chat_history']:
                if msg['is_user']:
                    f.write(f"You: {msg['message']}\n")
                else:
                    f.write(f"Nova: {msg['message']}  time {current_datetime}\n" )

            f.write("\n")  # Add a newline after each session

    # Define a simple bot response function
    def get_bot_response(user_message):
        if "hello" in user_message:
            return "Hello! How can I help you today?"
        elif "what is the time" in user_message: 
            return f" The current time is {current_datetime}"
        elif "my name is" in user_message:
            return "Great! Hello, my name is Nova."
        elif "hi" in user_message:
            return "Hi! How can I help you today?"
        elif "how are you" in user_message:
            return "I'm just a bot, but I'm doing great! Thanks for asking."
        elif "bye" in user_message:
            return "Goodbye! Have a great day!"
        else:
            user_message = user_message.lower()
            res = model.predict(user_message)
            res = intent.get_response(res)
            return res

    # Function to simulate typing animation for the bot's response
    def animated_typing(text, speed=0.03):
        full_text = ""
        placeholder = st.empty()  # Create a placeholder to dynamically update text
        for char in text:
            full_text += char
            placeholder.markdown(f"**Nova**: {full_text}")
            time.sleep(speed)



    # Title for the app

    st.title("ChatNova")
    st.caption("""
    Hello! I'm Nova, your virtual assistant.
    I’m a chatbot designed to help you with any questions or tasks you may have. Whether you need information, assistance with technology, or just want to have a friendly conversation, I’m here for you 24/7!

    I learn from every interaction and constantly improve to serve you better. My goal is to make your life easier and more efficient. Ask me anything, and let's explore the possibilities together!
    """)

    # Create a text input for user messages
    user_input = st.chat_input("ChatNova")

    # When the user enters a message
    if user_input:
        # Append the user's message to chat history in session state
        st.session_state['chat_history'].append({"message": user_input, "is_user": True})

        # Display past chat history
        for msg in st.session_state['chat_history'][:-1]:  # Skip the current input
            if msg['is_user']:
                st.markdown(f"**You**: {msg['message']}")
            else:
                st.markdown(f"**Nova**: {msg['message']}")

        # Display the user's new message
        st.markdown(f"**You**: {user_input}")

        # Simulate bot typing delay
        time.sleep(1)

        # Get the bot's reply and append it to the chat history
        bot_reply = get_bot_response(user_input)
        st.session_state['chat_history'].append({"message": bot_reply, "is_user": False})

        # Display the bot's message with typing animation
        animated_typing(bot_reply)
        
        save_conversation_to_file()

except (Exception):
    st.code(f"""print(Error :  + {str(e)})""")