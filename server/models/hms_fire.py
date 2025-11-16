from geoalchemy2 import Geometry
from pydantic    import BaseModel
from sqlmodel    import SQLModel, Field
from sqlalchemy  import Column, Float, Integer, String
from typing      import ClassVar


class HMSFire(SQLModel, table=True):
    __tablename__ = "hms_fires"
    __table_args__ = {"schema": "public"}

    lon: float = Field(
        default=None,
        sa_column=Column("Lon", Float)
    )

    lat: float = Field(
        default=None,
        sa_column=Column("Lat", Float)
    )

    year_day: int = Field(
        default=None,
        sa_column=Column("YearDay", Integer)
    )

    time: str = Field(
        default=None,
        sa_column=Column("Time", String)
    )

    geometry: ClassVar = Column(
        "geometry",
        Geometry(geometry_type="POINT", srid=4326)
    )

    year: int = Field(
        sa_column=Column("Year", Integer, primary_key=True)
    )

    id: int = Field(
        sa_column=Column("id", Integer, primary_key=True)
    )


class HMSFireOut(BaseModel):
    lon: float | None = None
    lat: float | None = None
    year_day: int | None
    time: str | None
    geometry: str | None = None
    year: int
    id: int