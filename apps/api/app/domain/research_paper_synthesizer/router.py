from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.research_paper_synthesizer.schemas import AgenticResearchPaperSynthesizerSessionCreate, AgenticResearchPaperSynthesizerSessionResponse
from app.domain.research_paper_synthesizer.service import AgenticResearchPaperSynthesizerService

router = APIRouter(prefix="/api/v1/research_paper_synthesizer", tags=["Agentic Research Paper Synthesizer Domain"])

@router.post("/sessions", response_model=AgenticResearchPaperSynthesizerSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticResearchPaperSynthesizerSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Research Paper Synthesizer.
    """
    return AgenticResearchPaperSynthesizerService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticResearchPaperSynthesizerSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticResearchPaperSynthesizerService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
