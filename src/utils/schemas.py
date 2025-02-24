from pydantic import BaseModel
from pydantic import Field


class ResponseOutput(BaseModel):
    Name: str = Field(..., description="Full Name of the candiate present in the CV")
    Score: int = Field(..., description="Evaluation score for assigned for the given CV compared to the job description")
    Reason: str = Field(..., description="Reasoning behind the given score which includes comparison details and highlights of the CV")