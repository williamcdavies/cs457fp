from fastapi                 import APIRouter, Depends, Query
from sqlmodel                import Session, func, select
from server.db.session       import get_session
from server.models.hms_smoke import HMSSmoke, HMSSmokeOut
from typing                  import Annotated


router = APIRouter(prefix="/hms_smokes", tags=["hms_smokes"])


@router.get("/", response_model=list[HMSSmokeOut])
def read_hms_fires(
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