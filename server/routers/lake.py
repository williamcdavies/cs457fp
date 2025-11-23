from fastapi            import APIRouter, Depends, HTTPException, Query
from sqlmodel           import Session, select
from server.db.session  import get_session
from server.models.lake import Lake
from typing             import Annotated


router = APIRouter(prefix="/lakes", tags=["lakes"])


@router.get("/", response_model=list[Lake])
def read_lakes(
    session: Annotated[Session, Depends(get_session)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    lakes = session.exec(select(Lake).order_by(Lake.hylak_id).offset(offset).limit(limit)).all()
    return lakes


@router.get("/{hylak_id}", response_model=Lake)
def read_lake(
    session: Annotated[Session, Depends(get_session)],
    hylak_id: int
):
    lake = session.get(Lake, hylak_id)
    if not lake:
        raise HTTPException(status_code=404, detail="Object not found")
    return lake