# 🎓 Advanced LMS AI Chatbot A state-of-the-art, Retrieval-Augmented Generation (RAG) chatbot designed to provide instant, conversational support for students navigating a college Learning Management System (LMS). This project transforms static FAQ data into a dynamic, intelligent AI assistant with a premium user interface. ## 🚀 Key Features * **RAG Architecture (Retrieval-Augmented Generation):** Beyond simple keyword matching. The bot retrieves relevant official context and uses a Large Language Model (LLM) to generate natural, helpful responses. * **Vector Database (ChromaDB):** High-performance semantic search powered by chromadb. All FAQ data is stored as vectors locally for lightning-fast, persistent retrieval. * **Deep Semantic Understanding:** Powered by sentence-transformers, the bot understands the intent behind questions (e.g., mapping "I can't log in" to "Password Reset" answers). * **Premium "AI-First" UI:** * **Modern Aesthetic:** Sleek dark-themed interface with custom purple/blue gradients. * **Suggested Prompts:** Interactive pill-style buttons for common queries. * **Real-time Animations:** Modern "Thinking..." states and typewriter-style response reveals. * **Secure & Scalable:** Built-in .env support for API keys and optimized local database storage. ## 🛠️ Technical Stack - **Frontend:** [Streamlit](https://streamlit.io/) (Custom CSS) - **Brain:** [Google Gemini 2.5 Flash](https://aistudio.google.com/) (via google-genai SDK) - **Vector Engine:** [ChromaDB](https://www.trychroma.com/) - **Embeddings:** all-MiniLM-L6-v2 (Sentence Transformers) - **Logic:** Python, Pandas, NumPy ## ⚙️ Installation & Setup 1. **Clone the repository:**
bash
   git clone https://github.com/watdasouvikdoin/AI-and-machine-learning-LMS-CHAT-BOT.git
   cd AI-and-machine-learning-LMS-CHAT-BOT
2. **Install dependencies:**
bash
   pip install -r requirements.txt
3. **Configure Environment:** Create a .env file in the root directory and add your Google API Key:
env
   GEMINI_API_KEY=your_google_gemini_api_key
4. **Launch the App:**
bash
   streamlit run app.py
## 📂 File Structure - app.py: The main Streamlit web interface and UI logic. - chatbot.py: Core RAG logic, ChromaDB initialization, and LLM integration. - faqs.csv: The knowledge base containing LMS frequently asked questions. - .chroma/: Local directory where the vector database is persisted. - requirements.txt: List of necessary Python libraries. ## 🤝 Contributing Feel free to fork this project, open issues, or submit pull requests to improve the chatbot's capabilities or UI! --- *Developed with ❤️ to improve the student digital experience.*
