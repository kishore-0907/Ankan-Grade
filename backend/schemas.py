from pydantic import BaseModel, Field, field_validator
from typing import Optional, Any, Dict, List
import datetime

class RubricCreate(BaseModel):
    subject: str = "Physics"
    question_text: str
    criteria: Dict[str, Any]
    max_marks: float

class ScriptResponse(BaseModel):
    id: int
    student_identifier: str
    image_url: str
    rubric_id: Optional[int]
    status: str
    created_at: datetime.datetime

    class Config:
        from_attributes = True

class ApproveScoreRequest(BaseModel):
    examiner_id: int
    examiner_name: str = "Examiner"

class OverrideScoreRequest(BaseModel):
    examiner_id: int
    examiner_name: str = "Examiner"
    examiner_score: float
    override_reason: str = Field(..., min_length=5, description="Mandatory typed explanation for overriding the AI score")

    @field_validator("override_reason")
    @classmethod
    def check_override_reason(cls, v):
        if not v or len(v.strip()) < 5:
            raise ValueError("An explicit, typed reason of at least 5 characters is mandatory when overriding AI score.")
        return v.strip()

class FlagScoreRequest(BaseModel):
    examiner_id: int
    examiner_name: str = "Examiner"
    flag_reason: str
