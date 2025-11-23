from fastapi                  import APIRouter, Depends, HTTPException, Query
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


@router.get("/{hylak_id}", response_model=LakePointOut)
def read_lakes_point(
    session: Annotated[Session, Depends(get_session)],
    hylak_id: int
):
    lakes_point = session.exec(select(
        LakePoint.hylak_id,
        func.ST_AsGeoJSON(LakePoint.geometry).label("geometry")
    ).where(LakePoint.hylak_id == hylak_id)).mappings().one_or_none()
    if not lakes_point:
        raise HTTPException(status_code=404, detail="Object not found")
    return lakes_point