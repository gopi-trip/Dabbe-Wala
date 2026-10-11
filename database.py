from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./dabbe-wala.db"

engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    # Create the database tables based on the models defined in models.py
    SQLModel.metadata.create_all(engine)

def get_session():
    # Provide a database session for interacting with the database
    with Session(engine) as session:
        yield session