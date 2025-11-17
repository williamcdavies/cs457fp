from fastapi                 import APIRouter, Depends, HTTPException, Query
from sqlmodel                import Session, func, select
from server.db.session       import get_session
from server.models.lake_poly import LakePoly, LakePolyOut
from typing                  import Annotated


router = APIRouter(prefix="/lakes_polys", tags=["lakes_polys"])


@router.get("/", response_model=list[LakePolyOut])
def read_lakes_polys(
    session: Annotated[Session, Depends(get_session)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    lakes_polys = session.exec(select(
        LakePoly.hylak_id,
        func.ST_AsGeoJSON(LakePoly.geometry_4326).label("geometry_4326"),
        func.ST_AsGeoJSON(LakePoly.geometry_3978).label("geometry_3978")
    ).order_by(LakePoly.hylak_id).offset(offset).limit(limit)).mappings().all()
    return lakes_polys


@router.get("/{hylak_id}", response_model=LakePolyOut)
def read_lakes_poly(
    hylak_id: int,
    session: Annotated[Session, Depends(get_session)]
):
    lakes_poly = session.exec(select(
        LakePoly.hylak_id,
        func.ST_AsGeoJSON(LakePoly.geometry_4326).label("geometry_4326"),
        func.ST_AsGeoJSON(LakePoly.geometry_3978).label("geometry_3978")
    ).where(LakePoly.hylak_id == hylak_id)).mappings().one_or_none()
    if not lakes_poly:
        raise HTTPException(status_code=404, detail="Object not found")
    return lakes_poly