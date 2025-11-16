from geoalchemy2 import Geometry
from pydantic    import BaseModel
from sqlmodel    import SQLModel, Field
from sqlalchemy  import Column, Integer, String
from typing      import ClassVar


class HMSSmoke(SQLModel, table=True):
    __tablename__ = "hms_smokes"
    __table_args__ = {"schema": "public"}

    start: str = Field(
        default=None,
        sa_column=Column("Start", String)
    )

    end: str = Field(
        default=None,
        sa_column=Column("End", String)
    )

    density: str = Field(
        default=None,
        sa_column=Column("Density", String)
    )

    geometry: ClassVar = Column(
        "geometry",
        Geometry(geometry_type="POLYGON", srid=4326)
    )

    year: int = Field(
        sa_column=Column("Year", Integer, primary_key=True)
    )

    id: int = Field(
        sa_column=Column("id", Integer, primary_key=True)
    )


class HMSSmokeOut(BaseModel):
    start: str | None = None
    end: str | None = None
    density: str | None = None
    geometry: str | None = None
    year: int
    id: int