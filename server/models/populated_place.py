from geoalchemy2 import Geometry
from pydantic    import BaseModel
from sqlmodel    import SQLModel, Field
from sqlalchemy  import Column, Float, Integer, String
from typing      import ClassVar


class PopulatedPlace(SQLModel, table=True):
    __tablename__ = "populated_places"
    __table_args__ = {"schema": "public"}

    name: str = Field(
        default=None,
        sa_column=Column("NAME", String)
    )

    name_ascii: str = Field(
        default=None,
        sa_column=Column("NAMEASCII", String)
    )
    
    latitude: float = Field(
        default=None,
        sa_column=Column("LATITUDE", Float)
    )

    longitude: float = Field(
        default=None,
        sa_column=Column("LONGITUDE", Float)
    )

    geometry: ClassVar = Column(
        "geometry",
        Geometry(geometry_type="POINT", srid=4326)
    )

    id: int = Field(
        sa_column=Column("id", Integer, primary_key=True)
    )


class PopulatedPlaceOut(BaseModel):
    name: str | None = None
    name_ascii: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    geometry: str | None = None
    id: int