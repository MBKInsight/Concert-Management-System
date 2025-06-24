from sqlalchemy.orm import Session
import crud
from models import models
from schemas import schemas


class ShowTimeService:

    @staticmethod
    def create_showtime(db: Session, showtime: schemas.ShowTimeCreate):
        return crud.create_entity(db, models.ShowTime, showtime)

    @staticmethod
    def get_showtime(db: Session, showtime_id: int):
        return crud.get_entity(db, models.ShowTime, showtime_id)

    @staticmethod
    def get_all_showtimes(db: Session):
        return crud.get_all_entities(db, models.ShowTime)

    @staticmethod
    def update_showtime(db: Session, showtime_id: int, updated_showtime: schemas.ShowTimeCreate):
        return crud.update_entity(db, models.ShowTime, showtime_id, updated_showtime)

    @staticmethod
    def delete_showtime(db: Session, showtime_id: int):
        return crud.delete_entity(db, models.ShowTime, showtime_id)
