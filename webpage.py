# This file is the frontend of the chatbot. It is used to display the chatbot on a webpage.

#-------------------------Imports-------------------------#

import streamlit as st
from streamlit_chat import message
from main import get_ans

#-------------------------Main Code-------------------------#

# Set page config
st.set_page_config(page_title="Unicamp Vestibular 2024 Bot")

st.header("Unicamp Vestibular 2024")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display initial message in chat message container
with st.chat_message("assistant", avatar='logo.png'):
    st.markdown("Oi, estou aqui para ajudar com qualquer duvida em relacao ao vestibular da Unicamp 2024, em que posso ajudar?")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Escreva sua pergunta aqui..."):

    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response, source_documents = get_ans(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar='logo.png'):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})