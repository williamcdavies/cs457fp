from sqlalchemy import Column, Integer, String
from sqlmodel    import Field, SQLModel


class Log(SQLModel, table=True):
    __tablename__ = "logs"
    __table_args__ = {"schema": "public"}

    id: int = Field(
        sa_column=Column("id", Integer, primary_key=True)
    )

    time: str = Field(
        default=None,
        sa_column=Column("time", String)
    )

    type: str = Field(
        default=None,
        sa_column=Column("type", String)
    )