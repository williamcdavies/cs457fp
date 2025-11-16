from fastapi                            import APIRouter, Depends, Query
from sqlmodel                           import Session, func, select
from server.db.session                  import get_session
from server.models.fire_area_canada_usa import FireAreaCanadaUSA, FireAreaCanadaUSAOut
from typing                             import Annotated


router = APIRouter(prefix="/fire_area_usa_canada", tags=["fire_area_usa_canada"])


@router.get("/", response_model=list[FireAreaCanadaUSAOut])
def read_fire_area_usa_canada(
    session: Annotated[Session, Depends(get_session)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    fire_area_usa_canada = session.exec(select(
        FireAreaCanadaUSA.year,
        func.ST_AsGeoJSON(FireAreaCanadaUSA.geometry).label("geometry"),
        FireAreaCanadaUSA.id
    ).order_by(FireAreaCanadaUSA.year, FireAreaCanadaUSA.id).offset(offset).limit(limit)).mappings().all()
    return fire_area_usa_canada