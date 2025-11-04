import requests
import streamlit as st

def get_essay_response(input_text):
    response=requests.post("http://localhost:8000/ollama-essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

def get_poem_response(input_text):
    response=requests.post(
    "http://localhost:8000/ollama-poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

    ## streamlit framework

st.title('Langchain Demo With LLAMA API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

if input_text:
    essay_response= get_essay_response(input_text)
    st.write("Essay:", essay_response)
if input_text1:
    poem_response= get_poem_response(input_text1)
    st.write("Poem:", poem_response)
