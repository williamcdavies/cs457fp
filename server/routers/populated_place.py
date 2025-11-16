from fastapi                       import APIRouter, Depends, Query
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