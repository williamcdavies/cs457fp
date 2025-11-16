from geoalchemy2 import Geometry
from pydantic    import BaseModel
from sqlmodel    import SQLModel, Field
from sqlalchemy  import Column, Integer
from typing      import ClassVar


class LakePoint(SQLModel, table=True):
    __tablename__ = "lakes_points"
    __table_args__ = {"schema": "public"}

    hylak_id: int = Field(
        sa_column=Column("Hylak_id", Integer, primary_key=True)
    )

    geometry: ClassVar = Column(
        "geometry",
        Geometry(geometry_type="POINT", srid=4326)
    )


class LakePointOut(BaseModel):
    hylak_id: int
    geometry: str | None = None