from geoalchemy2 import Geometry
from pydantic    import BaseModel
from sqlmodel    import SQLModel, Field
from sqlalchemy  import Column, Integer
from typing      import ClassVar


class LakeBuffer(SQLModel, table=True):
    __tablename__ = "lakes_buffers"
    __table_args__ = {"schema": "public"}

    hylak_id: int = Field(
        sa_column=Column("Hylak_id", Integer, primary_key=True)
    )

    geometry: ClassVar = Column(
        "geometry",
        Geometry(geometry_type="POLYGON", srid=3978)
    )


class LakeBufferOut(BaseModel):
    hylak_id: int
    geometry: str | None = None