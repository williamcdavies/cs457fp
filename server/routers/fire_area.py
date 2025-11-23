from fastapi                 import APIRouter, Depends, HTTPException, Query
from sqlmodel                import Session, func, select
from server.db.session       import get_session
from server.models.fire_area import FireArea, FireAreaOut
from typing                  import Annotated


router = APIRouter(prefix="/fire_areas", tags=["fire_areas"])


@router.get("/", response_model=list[FireAreaOut])
def read_fire_areas(
    session: Annotated[Session, Depends(get_session)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    fire_areas = session.exec(select(
        FireArea.year,
        func.ST_AsGeoJSON(FireArea.geometry).label("geometry"),
        FireArea.id
    ).order_by(FireArea.year, FireArea.id).offset(offset).limit(limit)).mappings().all()
    return fire_areas


@router.get("/{id}", response_model=FireAreaOut)
def read_fire_area(
    session: Annotated[Session, Depends(get_session)],
    year: int,
    id: int
):
    fire_area = session.exec(select(
        FireArea.year,
        func.ST_AsGeoJSON(FireArea.geometry).label("geometry"),
        FireArea.id
    ).where(FireArea.year == year, FireArea.id == id)).mappings().one_or_none()
    if not fire_area:
        raise HTTPException(status_code=404, detail="Object not found")
    return fire_area