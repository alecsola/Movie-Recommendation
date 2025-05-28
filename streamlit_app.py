import streamlit as st
from langchain_community.llms import OpenAI  # ✅ updated import

st.title('🎬 Movie Recommender App')

# Sidebar input for API key
openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key', type='password')

# Movie recommendation function
def generate_recommendations(user_prompt):
    if not openai_api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
        return

    # Create LLM instance with LangChain
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

    # Craft the prompt
    prompt = (
        "You are a movie expert. Based on the user's preferences, recommend 5 great movies "
        "with a short explanation for each. Format each recommendation with an emoji and one sentence.\n\n"
        f"User Preferences: {user_prompt}\n\n"
        "Recommendations:"
    )

    # Generate response
    response = llm(prompt)
    st.markdown(response)

# User form
with st.form('recommendation_form'):
    user_input = st.text_area('Describe what kind of movies you want:', 
                              'I like sci-fi movies with strong female leads and mystery.')
    submitted = st.form_submit_button('Get Recommendations')

    if submitted:
        generate_recommendations(user_input)
