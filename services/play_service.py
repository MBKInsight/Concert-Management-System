from sqlalchemy.orm import Session
import crud
from models import models
from schemas import schemas


class PlayService:

    @staticmethod
    def create_play(db: Session, play: schemas.PlayCreate):
        return crud.create_entity(db, models.Play, play)

    @staticmethod
    def get_play(db: Session, play_id: int):
        return crud.get_entity(db, models.Play, play_id)

    @staticmethod
    def get_all_plays(db: Session):
        return crud.get_all_entities(db, models.Play)

    @staticmethod
    def update_play(db: Session, play_id: int, updated_play: schemas.PlayCreate):
        return crud.update_entity(db, models.Play, play_id, updated_play)

    @staticmethod
    def delete_play(db: Session, play_id: int):
        return crud.delete_entity(db, models.Play, play_id)
