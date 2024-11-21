from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize the FastAPI app
app = FastAPI()

# Load pre-trained sentiment-analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis")

# Define a Pydantic model to accept text input
class TextInput(BaseModel):
    text: str

# Define the API endpoint for sentiment analysis
@app.post("/analyze_sentiment/")
def analyze_sentiment(input_text: TextInput):
    # Perform sentiment analysis
    result = sentiment_analysis(input_text.text)
    
    # Return the sentiment label and confidence score
    return {"sentiment": result[0]['label'], "confidence": result[0]['score']}

# To run the app, use: uvicorn <filename>:app --reload
