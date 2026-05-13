import pandas as pd
import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def load_data(filepath='faqs.csv'):
    """Load the CSV file into a DataFrame and extract questions and answers."""
    df = pd.read_csv(filepath)
    questions = df['Question'].tolist()
    answers = df['Answer'].tolist()
    return questions, answers

def load_model():
    """Initialize BERT tokenizer and model."""
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    model.eval()  # Set the model to evaluation mode
    return tokenizer, model

def compute_embeddings(questions, tokenizer, model):
    """Tokenize Questions and compute embeddings."""
    encodings = tokenizer(questions, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        embeddings = model(encodings['input_ids'], attention_mask=encodings['attention_mask'])[0][:, 0, :].numpy()
    return embeddings

def get_response(user_input, tokenizer, model, question_embeddings, answers):
    """Get the most appropriate answer for the user input."""
    # Tokenize user input
    user_input_encoded = tokenizer(user_input, padding=True, truncation=True, return_tensors='pt', max_length=512)
    
    with torch.no_grad():
        user_input_embedding = model(user_input_encoded['input_ids'], attention_mask=user_input_encoded['attention_mask'])[0][:, 0, :].numpy()
    
    # Calculate similarities
    similarities = []
    for question_embedding in question_embeddings:
        similarity = cosine_similarity(user_input_embedding, question_embedding.reshape(1, -1))[0][0]
        similarities.append(similarity)

    # Select the best match
    best_match_index = np.argmax(similarities)
    best_similarity = similarities[best_match_index]
    
    # Return corresponding answer (threshold from original notebook was 0.5)
    if best_similarity < 0.5:
        return "I'm sorry, I didn't understand that. Could you please rephrase your question?"
    
    return answers[best_match_index]
