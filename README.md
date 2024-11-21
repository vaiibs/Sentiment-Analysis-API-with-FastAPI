# Sentiment-Analysis-API-with-FastAPI

This project creates a simple FastAPI web application that uses a pre-trained model from Hugging Face's Transformers library to perform sentiment analysis on text input. It analyzes whether the input text is positive or negative and returns the sentiment along with a confidence score.

Process:

Load Pre-trained Model: Use Hugging Face's transformers library to load a pre-trained sentiment analysis model.
Set Up FastAPI App: Create a FastAPI application that accepts text input through a POST request.
Perform Sentiment Analysis: The API processes the input text and returns a sentiment label (e.g., "POSITIVE", "NEGATIVE") and a confidence score.
Deploy and Test: The FastAPI app can be tested locally via Swagger UI or with tools like Postman or cURL.

Steps to Run:

    pip install -r requirements.txt
   
    uvicorn api:app --reload
    
    Test API with Postman:
      Create a POST request to the following URL: http://127.0.0.1:8000/analyze_sentiment/
     
      INPUT:
      {
      "text": "I love the new design of this app! It's so intuitive."
      }
      
      OUTPUT
      {
      "sentiment": "POSITIVE",
      "confidence": 0.9998795986175537
      }
