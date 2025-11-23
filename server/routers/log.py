from fastapi           import APIRouter, Depends, HTTPException, Query
from sqlmodel          import Session, select
from server.db.session import get_session
from server.models.log import Log
from typing            import Annotated


router = APIRouter(prefix="/logs", tags=["logs"])


@router.get("/", response_model=list[Log])
def read_logs(
    session: Annotated[Session, Depends(get_session)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    logs = session.exec(select(Log).order_by(Log.id).offset(offset).limit(limit)).all()
    return logs


@router.get("/{id}", response_model=Log)
def read_log(
    session: Annotated[Session, Depends(get_session)],
    id: int
):
    log = session.get(Log, id)
    if not log:
        raise HTTPException(status_code=404, detail="Object not found")
    return log


@router.post("/", response_model=Log)
def write_log(
    session: Annotated[Session, Depends(get_session)],
    time: str,
    type: str
):
    log = Log(time=time, type=type)
    session.add(log)
    session.commit()
    session.refresh(log)
    return log