from geoalchemy2 import Geometry
from pydantic    import BaseModel
from sqlmodel    import SQLModel, Field
from sqlalchemy  import Column, Integer
from typing      import ClassVar


class FireArea(SQLModel, table=True):
    __tablename__ = "fire_area_canada_usa"
    __table_args__ = {"schema": "public"}

    year: int = Field(
        sa_column=Column("YEAR", Integer, primary_key=True)
    )

    geometry: ClassVar = Column(
        "geometry",
        Geometry(geometry_type="POLYGON", srid=3978)
    )

    id: int = Field(
        sa_column=Column("id", Integer, primary_key=True)
    )


class FireAreaOut(BaseModel):
    year: int
    geometry: str | None = None
    id: int