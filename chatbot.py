import os
import google.generativeai as genai
import dotenv
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-1.5-flash')

st.markdown("<h1 style='text-align: center; color: white;'> Tuorist Guide ChatBot</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: white;'>Built By ztech.studio.</h1>", unsafe_allow_html=True)

chat = model.start_chat(history=[])

def answer(user_question):
    response = chat.send_message(user_question)
    return response

quest = st.text_input("Ask a question:")
btn = st.button("Ask", type="primary")

if btn and quest:
    result = answer(quest)
    st.subheader("Response : ")
    for word in result:
        st.text(word.text)
        


