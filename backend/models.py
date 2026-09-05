import datetime
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    role = Column(String(30), nullable=False, default="examiner") # admin, examiner, moderator

class Rubric(Base):
    __tablename__ = "rubrics"
    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(100), default="Physics")
    question_text = Column(Text, nullable=False)
    criteria = Column(JSON, nullable=False) # JSON structure of marking steps & deductions
    max_marks = Column(Float, nullable=False, default=10.0)

class Script(Base):
    __tablename__ = "scripts"
    id = Column(Integer, primary_key=True, index=True)
    student_identifier = Column(String(100), nullable=False, index=True) # Roll number / Barcode
    image_url = Column(String(500), nullable=False)
    rubric_id = Column(Integer, ForeignKey("rubrics.id"), nullable=True)
    status = Column(String(30), default="pending") # pending, graded, flagged, overridden
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    rubric = relationship("Rubric")
    evaluations = relationship("Evaluation", back_populates="script")

class Evaluation(Base):
    __tablename__ = "evaluations"
    id = Column(Integer, primary_key=True, index=True)
    script_id = Column(Integer, ForeignKey("scripts.id"), nullable=False)
    ai_score = Column(Float, nullable=False)
    ai_reasoning = Column(Text, nullable=False)
    ai_confidence = Column(String(20), nullable=False) # high, medium, low
    examiner_score = Column(Float, nullable=True)
    examiner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    override_reason = Column(Text, nullable=True) # Mandatory if examiner_score != ai_score
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    script = relationship("Script", back_populates="evaluations")
    audit_logs = relationship("AuditLog", back_populates="evaluation")

class AuditLog(Base):
    __tablename__ = "audit_log"
    id = Column(Integer, primary_key=True, index=True)
    evaluation_id = Column(Integer, ForeignKey("evaluations.id"), nullable=False)
    action_type = Column(String(50), nullable=False) # AI_EVALUATED, EXAMINER_APPROVED, EXAMINER_OVERRIDDEN, EXAMINER_FLAGGED
    actor_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    actor_name = Column(String(100), default="System")
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    details = Column(JSON, nullable=False) # Snapshot of score, reason, diff, client info

    evaluation = relationship("Evaluation", back_populates="audit_logs")
