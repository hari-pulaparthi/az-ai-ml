from pydantic import BaseModel

class TransulationRequest(BaseModel):
    text: str
    target_language: str