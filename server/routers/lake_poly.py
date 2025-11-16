from fastapi                 import APIRouter, Depends, Query
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