# AI-and-machine-learning-LMS-CHAT-BOT
A chat bot for helping students who are new to out college's website i.e. LMS

# LMS Help Chatbot

This repository contains the implementation of a chatbot designed to assist students with their queries related to the Learning Management System (LMS). The project utilizes natural language processing (NLP) techniques, including the BERT model, to provide accurate and context-aware responses to frequently asked questions.

## Project Overview

The LMS Help Chatbot aims to improve the user experience by offering instant assistance to students navigating the LMS. By leveraging machine learning, this chatbot can understand student inquiries and provide relevant answers, facilitating a smoother learning process.

## Key Features

- **Natural Language Understanding**: Utilizes BERT for effective understanding of user queries.
- **Contextual Responses**: Provides accurate answers based on a pre-defined dataset of frequently asked questions.
- **User-Friendly Interface**: Simple interaction model allowing students to ask questions easily.
- **Scalability**: Easily extendable with new questions and answers to improve accuracy and coverage.

## Dataset

The dataset used for training the model consists of a collection of questions and their corresponding answers related to the LMS. The dataset is organized in a CSV file with the following structure:

Question,Answer 
"How do I submit an assignment?","To submit an assignment, go to the 'Assignments' section, select the assignment, and click 'Submit'." 



Ensure that the dataset follows this structure to maintain compatibility with the chatbot's training process.

## Installation and Dependencies

To run this project, install the following dependencies:

- Python 3.x
- PyTorch
- Transformers
- Pandas


Project Structure
chatbot.py: Main script to run the chatbot and handle user interactions.
data_processing.py: Script for loading and preprocessing the dataset.
model.py: Contains the model definition and training logic using BERT.
requirements.txt: List of dependencies required to run the project.
faqs.csv: CSV file containing the questions and answers for training the chatbot.


Model Details
This project uses the following model:

BERT Model: A transformer-based model fine-tuned for question-answering tasks, allowing the chatbot to understand and respond to user queries effectively.



Training the Model
To train the model, use the following command:
python model.py


This script will load the dataset, preprocess the questions and answers, and train the model. Evaluation results, including accuracy, will be printed at the end of the training.


Results and Analysis
Test Accuracy: Displayed after model evaluation.
Performance metrics: Generated for analyzing the model's effectiveness in understanding and responding to questions.
