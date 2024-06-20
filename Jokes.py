import streamlit as st
import requests

st.title("Joke Fetcher")

# Description
st.write("This app allows you to fetch a joke from the Appstop Jokes API.")

# Initialize a session state variable to store the raw joke JSON
if 'joke' not in st.session_state:
    st.session_state.joke = None

# st.echo allows you to display the code being executed
with st.echo():
    # Function to fetch joke from Appstop Jokes API
    def fetch_joke():
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        joke = response.json()
        return joke
    
    joke = fetch_joke()
    print(joke)

# Create two columns
col1, col2 = st.columns(2)

# Place the Fetch a Joke button in the first column
with col1:
    if st.button('Fetch a Joke'):
        st.session_state.joke = fetch_joke()
        st.write("Here's your joke in JSON format:")
        st.json(st.session_state.joke)

# Place the Beautify button in the second column
with col2:
    if st.session_state.joke:
        if st.button('Beautify'):
            setup = st.session_state.joke.get('setup')
            punchline = st.session_state.joke.get('punchline')
            if setup and punchline:
                st.write(setup)
                st.write(" ")
                st.write(punchline)
            else:
                st.write("Could not find 'setup' and 'punchline' in the response.")
