from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from schemas import schemas
from services.actor_service import ActorService

router = APIRouter(prefix="/actors", tags=["Actors"])


@router.post("/", response_model=schemas.Actor)
def create_actor(actor: schemas.ActorCreate, db: Session = Depends(get_db)):
    return ActorService.create_actor(db, actor)


@router.get("/", response_model=list[schemas.Actor])
def get_all_actors(db: Session = Depends(get_db)):
    return ActorService.get_all_actors(db)


@router.get("/{actor_id}", response_model=schemas.Actor)
def get_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = ActorService.get_actor(db, actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor


@router.put("/{actor_id}", response_model=schemas.Actor)
def update_actor(actor_id: int, actor_update: schemas.ActorCreate, db: Session = Depends(get_db)):
    updated_actor = ActorService.update_actor(db, actor_id, actor_update)
    if not updated_actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return updated_actor


@router.delete("/{actor_id}", response_model=schemas.Actor)
def delete_actor(actor_id: int, db: Session = Depends(get_db)):
    deleted_actor = ActorService.delete_actor(db, actor_id)
    if not deleted_actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return deleted_actor
