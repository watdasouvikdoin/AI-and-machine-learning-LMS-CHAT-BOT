# LMS AI Chatbot

An AI-powered chatbot built to help students navigate their college Learning Management System (LMS) more easily.

What started as a simple Jupyter Notebook project evolved into a full RAG-based AI web application with semantic search, conversational responses, and a modern UI inspired by tools like ChatGPT and Perplexity.

The chatbot can answer common LMS-related questions, understand different ways students phrase queries, and generate natural responses using Google Gemini and vector-based retrieval.

---

## Features

- Conversational AI chatbot interface
- RAG (Retrieval-Augmented Generation) architecture
- Semantic search using Sentence Transformers
- ChromaDB vector database for fast retrieval
- Google Gemini 2.5 Flash integration
- Modern dark-themed UI with animations
- Suggested prompts for quick interaction
- Context-aware responses instead of hardcoded replies
- Secure API key handling using `.env`

---

## Tech Stack

### Frontend
- Streamlit
- Custom CSS

### AI / Backend
- Google Gemini 2.5 Flash
- Sentence Transformers (`all-MiniLM-L6-v2`)
- ChromaDB
- Python

### Libraries
- pandas
- numpy
- chromadb
- google-genai
- sentence-transformers

---

## How It Works

1. User asks a question
2. The chatbot converts the query into embeddings
3. ChromaDB retrieves the most relevant LMS context
4. That context is sent to Gemini
5. Gemini generates a conversational response

This allows the chatbot to understand meaning and intent instead of relying only on keyword matching.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/watdasouvikdoin/AI-and-machine-learning-LMS-CHAT-BOT.git
cd AI-and-machine-learning-LMS-CHAT-BOT
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the app:

```bash
streamlit run app.py
```

---

## Project Structure

```bash
├── app.py              # Streamlit frontend
├── chatbot.py          # Core RAG pipeline
├── faqs.csv            # LMS knowledge base
├── requirements.txt
├── .env
└── .chroma/            # Local vector database
```

---

## Screenshots

Add your UI screenshots here once deployed.

Suggested screenshots:
- Homepage
- Chat interface
- Suggested prompts
- Semantic query responses

---

## Future Improvements

- PDF upload + document Q&A
- Multi-chat sessions
- Voice assistant support
- Authentication system
- Deployment on Streamlit Cloud / Render
- Admin dashboard for managing FAQs

---

## Contributing

Contributions, suggestions, and improvements are welcome.

If you'd like to improve the chatbot or experiment with the UI/AI pipeline, feel free to fork the project and open a pull request.

---

Built by Souvik Ghosh
