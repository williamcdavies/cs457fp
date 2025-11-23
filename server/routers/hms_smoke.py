from fastapi                 import APIRouter, Depends, HTTPException, Query
from sqlmodel                import Session, func, select
from server.db.session       import get_session
from server.models.hms_smoke import HMSSmoke, HMSSmokeOut
from typing                  import Annotated


router = APIRouter(prefix="/hms_smokes", tags=["hms_smokes"])


@router.get("/", response_model=list[HMSSmokeOut])
def read_hms_smokes(
    session: Annotated[Session, Depends(get_session)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    hms_smokes = session.exec(select(
        HMSSmoke.start,
        HMSSmoke.end,
        HMSSmoke.density,
        func.ST_AsGeoJSON(HMSSmoke.geometry).label("geometry"),
        HMSSmoke.year,
        HMSSmoke.id
    ).order_by(HMSSmoke.year, HMSSmoke.id).offset(offset).limit(limit)).mappings().all()
    return hms_smokes


@router.get("/{id}", response_model=HMSSmokeOut)
def read_hms_smoke(
    session: Annotated[Session, Depends(get_session)],
    year: int,
    id: int
):
    hms_smoke = session.exec(select(
        HMSSmoke.start,
        HMSSmoke.end,
        HMSSmoke.density,
        func.ST_AsGeoJSON(HMSSmoke.geometry).label("geometry"),
        HMSSmoke.year,
        HMSSmoke.id
    ).where(HMSSmoke.year == year, HMSSmoke.id == id)).mappings().one_or_none()
    if not hms_smoke:
        raise HTTPException(status_code=404, detail="Object not found")
    return hms_smoke