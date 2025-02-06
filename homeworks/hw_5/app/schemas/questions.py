from pydantic import BaseModel, Field

class CreateQuestion(BaseModel):
    text: str = Field(..., min_length=5)
    category: str




class ResponseQuestion(BaseModel):
    # question_id: int
    text: str
    category: str
    model_config = {
        'from_attributes': True
    }

class CategoryBase(BaseModel):
    text: str


class MessageResponse(BaseModel):
    msg: str



