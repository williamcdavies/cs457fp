from geoalchemy2 import Geometry
from pydantic    import BaseModel
from sqlmodel    import SQLModel, Field
from sqlalchemy  import Column, Integer
from typing      import ClassVar


class LakePoly(SQLModel, table=True):
    __tablename__ = "lakes_polys"
    __table_args__ = {"schema": "public"}

    hylak_id: int = Field(
        sa_column=Column("Hylak_id", Integer, primary_key=True)
    )

    geometry_4326: ClassVar = Column(
        "4326_geometry",
        Geometry(geometry_type="POLYGON", srid=4326)
    )

    geometry_3978: ClassVar = Column(
        "3978_geometry",
        Geometry(geometry_type="POLYGON", srid=3978)
    )


class LakePolyOut(BaseModel):
    hylak_id: int
    geometry_4326: str | None = None
    geometry_3978: str | None = None