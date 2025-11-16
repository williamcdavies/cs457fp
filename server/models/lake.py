from sqlalchemy import Column, Float, Integer, String
from sqlmodel   import SQLModel, Field


class Lake(SQLModel, table=True):
    __tablename__ = "lakes"
    __table_args__ = {"schema": "public"}

    hylak_id: int = Field(
        sa_column=Column("Hylak_id", Integer, primary_key=True)
    )

    lake_name: str | None = Field(
        default=None,
        sa_column=Column("Lake_name", String)
    )

    country: str | None = Field(
        default=None,
        sa_column=Column("Country", String)
    )

    continent: str | None = Field(
        default=None,
        sa_column=Column("Continent", String)
    )

    pour_long: float | None = Field(
        default=None,
        sa_column=Column("Pour_long", Float)
    )

    pour_lat: float | None = Field(
        default=None,
        sa_column=Column("Pour_lat", Float)
    )