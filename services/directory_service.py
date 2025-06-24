from sqlalchemy.orm import Session
import crud
from models import models
from schemas import schemas


class DirectorService:

    @staticmethod
    def create_director(db: Session, director: schemas.DirectorCreate):
        return crud.create_entity(db, models.Director, director)

    @staticmethod
    def get_director(db: Session, director_id: int):
        return crud.get_entity(db, models.Director, director_id)

    @staticmethod
    def get_all_directors(db: Session):
        return crud.get_all_entities(db, models.Director)

    @staticmethod
    def update_director(db: Session, director_id: int, updated_director: schemas.DirectorCreate):
        return crud.update_entity(db, models.Director, director_id, updated_director)

    @staticmethod
    def delete_director(db: Session, director_id: int):
        return crud.delete_entity(db, models.Director, director_id)


def get_all_directors(db):
    return None


def get_director(db, director_id):
    return None


def create_director(db, director):
    return None


def update_director(db, director_id, director_update):
    return None


def delete_director(db, director_id):
    return None
