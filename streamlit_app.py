import streamlit as st
from langchain_community.llms import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('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')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
