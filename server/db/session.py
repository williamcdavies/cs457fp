from sqlmodel import create_engine, Session


engine = create_engine("postgresql://williamchuter-davies@localhost:5432/spatial")


def get_session():
    with Session(engine) as session:
        yield session