from fastapi            import APIRouter, Depends, Query
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