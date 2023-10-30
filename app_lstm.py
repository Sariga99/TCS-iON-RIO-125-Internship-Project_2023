# Import necessary libraries
import streamlit as st
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the LSTM model
# pickle_in = open(r"C:\Users\Dell\Desktop\ICT ML AI\tcsion2023\lstm_model.pkl", "rb")
# model = pickle.load(pickle_in)
lstm_model = tf.keras.models.load_model("lstm_model")


# Load other resources needed for preprocessing, e.g., tokenizer
tokenizer_path = 'tokenizer.pkl'  
with open(tokenizer_path, 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

# Define the maximum sequence length for your model
MAX_SEQUENCE_LENGTH = 200
# Define a function to preprocess text and make predictions
def predict_sentiment(text):
    # Tokenize and pad the input text
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

    # Make predictions
    prediction = lstm_model.predict(padded_sequences)[0][0]
    sentiment = "Positive" if prediction >= 0.5 else "Negative"

    return sentiment, prediction


# Streamlit UI with custom styling
st.set_page_config(page_title="Sentiment Analysis")

# Apply custom CSS styles for the app
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: #173B59;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Sentiment Analysis")

st.write("Welcome to our Sentiment Analysis App! 🚀 Analyze the sentiment of your feedback and comments to discover what people are saying. Simply enter your text, click 'Analyze,' and let the magic happen. We'll reveal whether it's all smiles 😃 or if there's room for improvement 😞.")

user_input = st.text_area("Enter your movie review:")
if st.button("Analyze"):
    if user_input:
        sentiment, confidence = predict_sentiment(user_input)
        emoji = "😃" if sentiment == "Positive" else "😞"
        st.write(f"Sentiment: {sentiment} {emoji}")
        st.write(f"Confidence: {confidence:.2f}")

# # Streamlit UI
# st.set_page_config(page_title="Sentiment Analysis")
# st.title("Sentiment Analysis")
# st.write("Welcome to our Sentiment Analysis App! 🚀 Analyze the sentiment of your feedback and comments to discover what people are saying. Simply enter your text, click 'Analyze,' and let the magic happen. We'll reveal whether it's all smiles 😃 or if there's room for improvement 😞.")


# user_input = st.text_area("Enter your movie review:")
# if st.button("Analyze"):
#     if user_input:
#         sentiment, confidence = predict_sentiment(user_input)
#         st.write(f"Sentiment: {sentiment}")
#         st.write(f"Confidence: {confidence:.2f}")


