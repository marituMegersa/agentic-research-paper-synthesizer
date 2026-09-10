from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.research_paper_synthesizer.models import AgenticResearchPaperSynthesizerSession, AgenticResearchPaperSynthesizerItem
from app.domain.research_paper_synthesizer.schemas import AgenticResearchPaperSynthesizerSessionCreate, AgenticResearchPaperSynthesizerItemCreate

class AgenticResearchPaperSynthesizerService:
    @staticmethod
    def create_session(db: Session, data: AgenticResearchPaperSynthesizerSessionCreate) -> AgenticResearchPaperSynthesizerSession:
        db_obj = AgenticResearchPaperSynthesizerSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticResearchPaperSynthesizerSession:
        return db.query(AgenticResearchPaperSynthesizerSession).filter(AgenticResearchPaperSynthesizerSession.id == session_id).first()
