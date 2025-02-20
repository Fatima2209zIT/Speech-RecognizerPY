import streamlit as st
import wikipedia
import webbrowser
from gtts import gTTS
import os

def speak(text):
    """Convert text to speech using gTTS"""
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")  # Linux ke liye (Colab ke liye suitable)

def open_app(command):
    """Open apps based on user command"""
    urls = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "gmail": "https://www.gmail.com",
        "instagram": "https://www.instagram.com",
        "wikipedia": "https://www.wikipedia.org"
    }
    for key in urls:
        if key in command:
            webbrowser.open(urls[key])
            speak(f"Opening {key}")
            return f"Opened {key}"
    return "Sorry, I can't open that app yet."

def search_wikipedia(query):
    """Search Wikipedia and return a summary"""
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError:
        return "There are multiple results. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "No results found."

# Streamlit UI
st.title("Voice Assistant")
st.write("Type your command below:")

user_command = st.text_input("Enter your command:")
if user_command:
    st.write(f"**You:** {user_command}")

    if "exit" in user_command or "bye" in user_command:
        st.write("Goodbye! Have a great day!")
        speak("Goodbye! Have a great day!")
    elif "open" in user_command:
        result = open_app(user_command)
        st.write(result)
    else:
        answer = search_wikipedia(user_command)
        st.write(f"**Assistant:** {answer}")
        speak(answer)
