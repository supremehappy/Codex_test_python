from pydantic import BaseModel, constr

class Context(BaseModel):
    """Model for the POST request body."""
    text: constr(strip_whitespace=True, min_length=1, max_length=1000)

class MessageResponse(BaseModel):
    """Standard response model."""
    message: str
