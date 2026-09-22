from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from sentiment import analyze_text

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextRequest(BaseModel):
    text: str = Field(min_length=1, max_length=5000)


@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.post("/analyze")
def analyze_sentiment(request: TextRequest):
    sentiment, score, explanation = analyze_text(request.text)

    return {
        "text": request.text,
        "sentiment": sentiment,
        "score": score,
        "explanation": explanation
    }