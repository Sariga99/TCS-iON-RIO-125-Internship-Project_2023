# TCS-iON-RIO-125-Internship-Project_2023
Project - Automated Sentiment Analysis of Textual Comments and Feedback


Welcome to the Automated Sentiment Analysis project! This project addresses the need for automated sentiment analysis, a crucial task in today's data-driven world. With the exponential growth of online content and user-generated comments, there is an increasing demand for efficient sentiment analysis tools. The primary goal of this project is to develop a robust sentiment analysis solution capable of categorizing text-based inputs into predefined sentiment classes, such as positive or negative.



Solution Approach: 

1. Data Collection and Preprocessing: Gather a sizable dataset containing user comments and associated sentiments. I chose IMDB movie review dataset. Perform essential preprocessing, including text cleaning, tokenization, and removal of stop words.

2.Model Building: The chosen solution approach involved implementing and evaluating multiple deep learning models, including BERT, CNN, RNN, and LSTM. The order of implementation was RNN, LSTM, CNN and BERT. 

3. Model Evaluation: Train, validate, and fine-tune each model using appropriate evaluation metrics. The model that performs best on validation data will be selected.

4. Streamlit Application: Develop a Streamlit web application to provide an interactive platform for users to input text and receive sentiment analysis results. This application will serve as a practical and user-friendly interface for your sentiment analysis model.


Outcome:

The CNN model demonstrated remarkable performance with a training accuracy of 99.99% and a validation accuracy of 85.39%. However, it is essential to be cautious about potential overfitting when deploying this model in practice.

The LSTM model yielded a training accuracy of 94.93% and a validation accuracy of 83.56%, making it a competitive choice for sentiment analysis.

The RNN model, while still providing valuable insights, achieved lower accuracy on both training (57.69%) and validation (51.15%) data.


BERT is a state-of-the-art model, but due to resource constraints, it was unable to run successfully. 

LSTM model is deployed using a streamlit app that can accurately and efficiently automate sentiment analysis of textual comments and feedback. The model can be used in a variety of applications, such as customer service, product development, and social media monitoring.
