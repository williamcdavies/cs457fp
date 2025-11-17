from fastapi                   import APIRouter, Depends, HTTPException, Query
from sqlmodel                  import Session, func, select
from server.db.session         import get_session
from server.models.lake_buffer import LakeBuffer, LakeBufferOut
from typing                    import Annotated


router = APIRouter(prefix="/lakes_buffers", tags=["lakes_buffers"])


@router.get("/", response_model=list[LakeBufferOut])
def read_lakes_buffers(
    session: Annotated[Session, Depends(get_session)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    lakes_buffers = session.exec(select(
        LakeBuffer.hylak_id,
        func.ST_AsGeoJSON(LakeBuffer.geometry).label("geometry")
    ).order_by(LakeBuffer.hylak_id).offset(offset).limit(limit)).mappings().all()
    return lakes_buffers


@router.get("/{hylak_id}", response_model=LakeBufferOut)
def read_lakes_buffer(
    hylak_id: int,
    session: Annotated[Session, Depends(get_session)]
):
    lakes_buffer = session.exec(select(
        LakeBuffer.hylak_id,
        func.ST_AsGeoJSON(LakeBuffer.geometry).label("geometry")
    ).where(LakeBuffer.hylak_id == hylak_id)).mappings().one_or_none()
    if not lakes_buffer:
        raise HTTPException(status_code=404, detail="Object not found")
    return lakes_buffer