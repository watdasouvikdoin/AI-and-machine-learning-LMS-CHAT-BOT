import streamlit as st
from chatbot import load_data, load_model, compute_embeddings, get_response

# Streamlit App Configuration
st.set_page_config(page_title="LMS Help Chatbot", page_icon="🎓", layout="centered")

st.title("🎓 LMS Help Chatbot")
st.markdown("Welcome to the LMS Help Chatbot! Ask me anything about the Learning Management System.")

# Cache the expensive resources (Model loading and Embeddings computation)
@st.cache_resource(show_spinner="Loading NLP model and data... This happens once per session.")
def initialize_chatbot():
    tokenizer, model = load_model()
    questions, answers = load_data('faqs.csv')
    embeddings = compute_embeddings(questions, tokenizer, model)
    return tokenizer, model, questions, answers, embeddings

try:
    tokenizer, model, questions, answers, embeddings = initialize_chatbot()
except Exception as e:
    st.error(f"Error loading the chatbot components: {e}")
    st.stop()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add an initial greeting message
    st.session_state.messages.append({"role": "assistant", "content": "Hello! I am the LMS AI assistant. How can I help you today?"})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I assist you today?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get bot response
    response = get_response(prompt, tokenizer, model, embeddings, answers)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
