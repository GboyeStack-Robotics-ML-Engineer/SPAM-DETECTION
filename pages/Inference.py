import streamlit as st
import random
import time
import os
import google.generativeai as genai


import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os

api_key=os.environ['GEMINI_API_KEY']
# print(api_key)
genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-8b",
  generation_config=generation_config,
  
)


def response_generator(session,prompt):
    response = session.send_message(prompt)
    response=response.text
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
        

def app():
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "model", 'content': 'Hey.... I am Jarvis. How can I be of assitance to you?'}]
        
        

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display assistant response in chat message container
    
        history=[{"role":message['role'],"parts":[message['content'],]} for message in st.session_state.messages]
        
        chat_session = model.start_chat(history=history)
        with st.chat_message("model"):
            response = st.write_stream(response_generator(session=chat_session,prompt=prompt))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "model", 'content': response})

