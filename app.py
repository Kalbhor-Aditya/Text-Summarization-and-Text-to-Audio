import streamlit as st
from transformers import pipeline


# Load the summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    summarized = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summarized[0]['summary_text']

# Streamlit app
st.title("Article Summarizer")

# Text input box
article = st.text_area("Paste your article here:")

if st.button("Summarize"):
    summarized_text = summarize_text(article)
    st.write("**Summarized Text:**")
    st.write(summarized_text)

   