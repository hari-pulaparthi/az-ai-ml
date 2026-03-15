from fastapi import FastAPI
from models import TransulationRequest

app = FastAPI(
    title="AI Translation API",
    description="Translates text using Azure AI",
    version="1.0.0",
    docs_url="/swagger",
)

@app.post("/translate")
def transulate_text(request: TransulationRequest):
    """Translate input text to the specified target language."""
    input_text = request.text
    target_language = request.target_language
    transulate_text = f"[Translated to {target_language}]: {input_text[::-1]}"
    return {         
        "original": input_text,         
        "translated": transulate_text,         
        "target_language": target_language     
    } 


