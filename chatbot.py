import os
import pandas as pd
import chromadb
from google import genai

def init_db(data_filepath="faqs.csv", db_path=".chroma"):
    """Initialize ChromaDB and populate it with FAQs if empty."""
    client = chromadb.PersistentClient(path=db_path)
    collection = client.get_or_create_collection(name="lms_faqs")
    
    # Check if we need to load data
    if collection.count() == 0:
        try:
            df = pd.read_csv(data_filepath)
            documents = df['Question'] + " -> " + df['Answer']
            
            # Add to ChromaDB. ChromaDB automatically uses all-MiniLM-L6-v2 to embed these!
            collection.add(
                documents=documents.tolist(),
                metadatas=[{"question": q, "answer": a} for q, a in zip(df['Question'], df['Answer'])],
                ids=[str(i) for i in range(len(df))]
            )
        except Exception as e:
            print(f"Warning: Could not load {data_filepath}: {e}")
            
    return collection

def get_response(user_input: str, collection) -> str:
    """Retrieve context from ChromaDB and generate a response using Gemini."""
    
    # 1. Retrieve the top 2 most relevant FAQs from ChromaDB
    results = collection.query(
        query_texts=[user_input],
        n_results=2
    )
    
    if not results['documents'] or len(results['documents'][0]) == 0:
        return "I'm having trouble searching my knowledge base right now."
        
    context_docs = results['documents'][0]
    context_text = "\n\n".join(context_docs)
    
    # 2. Build the prompt for the LLM
    prompt = f"""You are a helpful, friendly, and professional AI assistant for a college Learning Management System (LMS).
Use the following official FAQ context to answer the student's question. 
If the provided FAQs do not contain the answer, politely say that you don't have that information and advise them to contact IT support (support@college.edu). 
Do NOT invent or hallucinate answers outside of the provided context.
Keep your answer concise and easy to read.

Context Information:
{context_text}

Student Question:
{user_input}
"""

    # 3. Call Google Gemini to generate the response
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        return "I'm sorry, my AI backend is not configured yet. Please add your GEMINI_API_KEY to the .env file."
        
    client = genai.Client(api_key=api_key)
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Sorry, I encountered an error while thinking: {str(e)}"
