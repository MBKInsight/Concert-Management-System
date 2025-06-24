from sqlalchemy.orm import Session
import crud
from models import models
from schemas import schemas


class ActorService:

    @staticmethod
    def create_actor(db: Session, actor: schemas.ActorCreate):
        return crud.create_entity(db, models.Actor, actor)

    @staticmethod
    def get_actor(db: Session, actor_id: int):
        return crud.get_entity(db, models.Actor, actor_id)

    @staticmethod
    def get_all_actors(db: Session):
        return crud.get_all_entities(db, models.Actor)

    @staticmethod
    def update_actor(db: Session, actor_id: int, updated_actor: schemas.ActorCreate):
        return crud.update_entity(db, models.Actor, actor_id, updated_actor)

    @staticmethod
    def delete_actor(db: Session, actor_id: int):
        return crud.delete_entity(db, models.Actor, actor_id)
