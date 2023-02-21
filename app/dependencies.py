from crud.db_setup import SessionLocal


# db
def get_db():
    with SessionLocal() as db:
        yield db

