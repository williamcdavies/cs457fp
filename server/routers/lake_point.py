from fastapi                  import APIRouter, Depends, Query
from sqlmodel                 import Session, func, select
from server.db.session        import get_session
from server.models.lake_point import LakePoint, LakePointOut
from typing                   import Annotated


router = APIRouter(prefix="/lakes_points", tags=["lakes_points"])


@router.get("/", response_model=list[LakePointOut])
def read_lakes_points(
    session: Annotated[Session, Depends(get_session)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    lakes_points = session.exec(select(
        LakePoint.hylak_id,
        func.ST_AsGeoJSON(LakePoint.geometry).label("geometry")
    ).order_by(LakePoint.hylak_id).offset(offset).limit(limit)).mappings().all()
    return lakes_points