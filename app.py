import streamlit as st
from chatbot import load_data, load_model, compute_embeddings, get_response

# Streamlit App Configuration
st.set_page_config(page_title="LMS Help Chatbot", page_icon="🎓", layout="centered")

# Custom CSS for styling
st.markdown("""
<style>
    /* Dark AI-themed background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #e0e0e0;
    }

    /* Title styling */
    h1 {
        background: linear-gradient(90deg, #a78bfa, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    /* Subtitle text */
    .subtitle {
        color: #94a3b8;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
    }

    /* Suggested prompts section header */
    .prompts-header {
        color: #a78bfa;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 0.75rem;
        margin-top: 0.5rem;
    }

    /* Suggested prompt buttons */
    div[data-testid="stHorizontalBlock"] .stButton > button {
        background: rgba(167, 139, 250, 0.08);
        border: 1px solid rgba(167, 139, 250, 0.35);
        color: #c4b5fd;
        border-radius: 20px;
        padding: 0.4rem 0.9rem;
        font-size: 0.82rem;
        font-weight: 500;
        width: 100%;
        transition: all 0.2s ease;
        white-space: normal;
        text-align: left;
        line-height: 1.4;
        min-height: 52px;
    }
    div[data-testid="stHorizontalBlock"] .stButton > button:hover {
        background: rgba(167, 139, 250, 0.22);
        border-color: rgba(167, 139, 250, 0.75);
        color: #ede9fe;
        transform: translateY(-1px);
        box-shadow: 0 4px 15px rgba(167, 139, 250, 0.2);
    }
    div[data-testid="stHorizontalBlock"] .stButton > button:active {
        transform: translateY(0px);
    }

    /* Divider */
    hr {
        border-color: rgba(167, 139, 250, 0.2);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title and welcome message
st.title("🎓 LMS Help Chatbot")
st.markdown('<p class="subtitle">Welcome! Ask me anything about the Learning Management System.</p>', unsafe_allow_html=True)

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

# Initialize session state for chat history and prompt trigger
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "Hello! I am the LMS AI assistant. How can I help you today?"})

if "triggered_prompt" not in st.session_state:
    st.session_state.triggered_prompt = None

# ── Suggested Prompts Section ──────────────────────────────────────────────────
SUGGESTED_PROMPTS = [
    "How do I reset my password?",
    "Where can I view my grades?",
    "How do I submit assignments?",
    "How do I contact faculty?",
]

st.markdown('<p class="prompts-header">✦ Try asking</p>', unsafe_allow_html=True)

cols = st.columns(2)
for i, prompt_text in enumerate(SUGGESTED_PROMPTS):
    with cols[i % 2]:
        if st.button(prompt_text, key=f"suggested_prompt_{i}"):
            st.session_state.triggered_prompt = prompt_text

st.markdown("---")

# ── Chat History ───────────────────────────────────────────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── Process triggered prompt from suggestion buttons ──────────────────────────
if st.session_state.triggered_prompt:
    prompt = st.session_state.triggered_prompt
    st.session_state.triggered_prompt = None  # Reset

    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_response(prompt, tokenizer, model, embeddings, answers)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()

# ── React to typed user input ──────────────────────────────────────────────────
if prompt := st.chat_input("Type your question here..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_response(prompt, tokenizer, model, embeddings, answers)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
