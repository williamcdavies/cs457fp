from sqlmodel import Session, SQLModel, create_engine


engine = create_engine("postgresql://williamchuter-davies@localhost:5432/spatial")


def get_session():
    with Session(engine) as session:
        yield session