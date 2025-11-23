from fastapi                import APIRouter, Depends,HTTPException, Query
from sqlmodel               import Session, func, select
from server.db.session      import get_session
from server.models.hms_fire import HMSFire, HMSFireOut
from typing                 import Annotated


router = APIRouter(prefix="/hms_fires", tags=["hms_fires"])


@router.get("/", response_model=list[HMSFireOut])
def read_hms_fires(
    session: Annotated[Session, Depends(get_session)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    hms_fires = session.exec(select(
        HMSFire.lon,
        HMSFire.lat,
        HMSFire.year_day,
        HMSFire.time,
        func.ST_AsGeoJSON(HMSFire.geometry).label("geometry"),
        HMSFire.year,
        HMSFire.id
    ).order_by(HMSFire.year, HMSFire.id).offset(offset).limit(limit)).mappings().all()
    return hms_fires


@router.get("/{id}", response_model=HMSFireOut)
def read_hms_fire(
    session: Annotated[Session, Depends(get_session)],
    year: int,
    id: int
):
    hms_fire = session.exec(select(
        HMSFire.lon,
        HMSFire.lat,
        HMSFire.year_day,
        HMSFire.time,
        func.ST_AsGeoJSON(HMSFire.geometry).label("geometry"),
        HMSFire.year,
        HMSFire.id
    ).where(HMSFire.year == year, HMSFire.id == id)).mappings().one_or_none()
    if not hms_fire:
        raise HTTPException(status_code=404, detail="Object not found")
    return hms_fire