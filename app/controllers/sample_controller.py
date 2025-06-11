from fastapi import APIRouter
from app.models.sample_model import Context, MessageResponse

router = APIRouter(prefix="/sample", tags=["Sample"])

@router.get("/getHello", response_model=MessageResponse)
def get_hello() -> MessageResponse:
    """Return a greeting message."""
    return MessageResponse(message="Hello, world!")

@router.post("/postContext", response_model=MessageResponse)
def post_context(context: Context) -> MessageResponse:
    """Echo the received context."""
    safe_text = context.text.replace("<", "&lt;").replace(">", "&gt;")
    return MessageResponse(message=f"Received: {safe_text}")
