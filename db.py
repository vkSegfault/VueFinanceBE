from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = 'postgresql+psycopg2://user:pass@localhost:5432/mydb'

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
