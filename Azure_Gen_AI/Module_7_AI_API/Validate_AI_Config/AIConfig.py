from pydantic import BaseModel, validator

class AIConfig(BaseModel):
    api_key: str     
    region: str     
    model_name: str

    @validator('api_key', 'region', 'model_name')
    def not_empty(cls, value):
        if not value or not value.strip():
            raise ValueError('field cannot be empty')
        return value
    
