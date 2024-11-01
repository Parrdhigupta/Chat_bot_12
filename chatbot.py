# -*- coding: utf-8 -*-
"""Chatbot.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rSvX-AQX5GloxDkjYYGC883QQbRlCOPV
"""

import os
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi", "Hello", "How are you", "What's up"],
        "responses": ["Hello!", "Hi there!", "How can I help you today?"]
    },
    {
        "tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye", "Take care"],
        "responses": ["Goodbye!", "See you later!", "Have a great day!"]
    },
    {
        "tag": "thanks",
        "patterns": ["Thank you", "Thanks a lot", "I appreciate it"],
        "responses": ["You're welcome!", "No problem!", "Glad I could help!"]
    },
    {
        "tag": "about",
        "patterns": ["Who are you", "What can you do", "Who created you"],
        "responses": ["I'm a chatbot.", "I can answer questions and have conversations.", "I was created to assist you."]
    },
    {
        "tag": "help",
        "patterns": ["Help me", "I need help", "Can you help me?", "I'm having trouble"],
        "responses": ["Sure, what do you need help with?", "I'm here to help. What's the problem?"]
    },
    {
        "tag": "age",
        "patterns": ["How old are you", "What's your age", "When were you born"],
        "responses": ["I don't have an age. I'm just a computer program.", "I'm a chatbot, so I don't have an age."]
    },
    {
        "tag": "weather",
        "patterns": ["What's the weather like", "How's the weather", "Is it raining"],
        "responses": ["I'm sorry, I can't provide real-time weather information.", "I'm just a computer program, so I don't have access to real-time data."]
    },
    {
        "tag": "budget",
        "patterns": ["What's your budget", "How much can I spend", "Can you help me with a budget"],
        "responses": ["I'm here to help you with budgeting. What's your budget?", "I'm just a chatbot, so I don't have a budget."]
    },
    {
        "tag": "credit_score",
        "patterns": ["What's your credit score", "How good is your credit history", "Can you help me with a credit score"],
        "responses": ["I'm sorry, I can't provide real-time credit information.", "I'm just a chatbot, so I don't have access to real-time data."]
    }
]

vectorizer = TfidfVectorizer()
clf = LogisticRegression()

tags = []
patterns = []
for intent in intents:
    for pattern in intent["patterns"]:
        tags.append(intent["tag"])
        patterns.append(pattern)

x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent["tag"] == tag:
            response = random.choice(intent["responses"])
            return response

counter = 0

def main():
  global counter
  st.title("Chatbot")
  st.write("Welcome to the chatbot. Please type a message and press Enter to start the conversation.")

  counter += 1
  user_input = st.text_input("You:", key = f"user_input_ {counter}")

  if user_input:
    response = chatbot(user_input)
    st.text_area("Chatbot:", value=response, height=100, max_chars=None, key=f"chatbot_response_{counter}")

    if response.lower() in ["goodbye", "bye"]:
      st.write("Thank you for using the chatbot. Have a great day!")
      st.stop()

if __name__ == "__main__":
  main()

