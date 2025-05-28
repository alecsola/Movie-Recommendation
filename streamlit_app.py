import streamlit as st
from langchain_community.llms import Ollama

st.title('Offline Movie Recommender (Ollama + LangChain)')


llm = Ollama(model="mistral")  

def generate_recommendations(user_input):
    prompt = (
        "You are a movie expert. Based on the user's preferences, recommend 5 great movies "
        "with a short explanation for each one. Format the response with emojis and line breaks.\n\n"
        f"User Preferences: {user_input}\n\n"
        "Recommendations:"
    )
    response = llm(prompt)
    st.markdown(response)

# Streamlit UI
with st.form("movie_form"):
    user_input = st.text_area("What kind of movies are you into?", "I like thrillers from the 90s.")
    submitted = st.form_submit_button("Get Recommendations")

    if submitted:
        generate_recommendations(user_input)
