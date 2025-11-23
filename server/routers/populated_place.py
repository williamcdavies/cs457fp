from fastapi                       import APIRouter, Depends, HTTPException, Query
from sqlmodel                      import Session, func, select
from server.db.session             import get_session
from server.models.populated_place import PopulatedPlace, PopulatedPlaceOut
from typing                        import Annotated


router = APIRouter(prefix="/populated_places", tags=["populated_places"])


@router.get("/", response_model=list[PopulatedPlaceOut])
def read_populated_places(
    session: Annotated[Session, Depends(get_session)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    populated_places = session.exec(select(
        PopulatedPlace.name,
        PopulatedPlace.name_ascii,
        PopulatedPlace.latitude,
        PopulatedPlace.longitude,
        func.ST_AsGeoJSON(PopulatedPlace.geometry).label("geometry"),
        PopulatedPlace.id
    ).order_by(PopulatedPlace.id).offset(offset).limit(limit)).mappings().all()
    return populated_places

@router.get("/{id}", response_model=PopulatedPlaceOut)
def read_populated_place(
    session: Annotated[Session, Depends(get_session)],
    id: int
):
    populated_place = session.exec(select(
        PopulatedPlace.name,
        PopulatedPlace.name_ascii,
        PopulatedPlace.latitude,
        PopulatedPlace.longitude,
        func.ST_AsGeoJSON(PopulatedPlace.geometry).label("geometry"),
        PopulatedPlace.id
    ).where(PopulatedPlace.id == id)).mappings().one_or_none()
    if not populated_place:
        raise HTTPException(status_code=404, detail="Object not found")
    return populated_place