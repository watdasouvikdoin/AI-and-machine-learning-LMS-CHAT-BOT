import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Confidence threshold — below this, the bot admits uncertainty
SIMILARITY_THRESHOLD = 0.40

def load_model():
    """Load the sentence-transformers model (all-MiniLM-L6-v2).
    Much lighter (~80MB) and faster than bert-base-uncased,
    while producing superior semantic embeddings.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model

def load_data(filepath: str = "faqs.csv"):
    """Load the CSV file and extract questions and answers."""
    df = pd.read_csv(filepath)
    questions = df["Question"].tolist()
    answers = df["Answer"].tolist()
    return questions, answers

def compute_embeddings(questions: list, model: SentenceTransformer) -> np.ndarray:
    """Encode all FAQ questions into dense sentence embeddings.
    convert_to_numpy=True gives a plain ndarray ready for cosine_similarity.
    show_progress_bar=False keeps logs clean inside Streamlit.
    """
    embeddings = model.encode(
        questions,
        convert_to_numpy=True,
        show_progress_bar=False,
        normalize_embeddings=True,   # L2-normalised → dot-product == cosine sim
    )
    return embeddings

def get_response(
    user_input: str,
    model: SentenceTransformer,
    question_embeddings: np.ndarray,
    answers: list,
    threshold: float = SIMILARITY_THRESHOLD,
) -> str:
    """Find the most semantically similar FAQ and return its answer.

    Because embeddings are L2-normalised, cosine similarity reduces to a
    simple dot product — O(n) and very fast even for large FAQ sets.
    """
    user_embedding = model.encode(
        [user_input],
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    # Shape: (1, n_questions)
    scores = cosine_similarity(user_embedding, question_embeddings)[0]

    best_idx = int(np.argmax(scores))
    best_score = float(scores[best_idx])

    if best_score < threshold:
        return (
            "I'm not fully sure about that. "
            "Could you rephrase your question or try one of the suggested prompts?"
        )

    return answers[best_idx]
