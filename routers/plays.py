from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from services.play_service import PlayService
from schemas import schemas

router = APIRouter(prefix="/plays", tags=["Plays"])


@router.post("/", response_model=schemas.Play)
def create_play(play: schemas.PlayCreate, db: Session = Depends(get_db)):
    return PlayService.create_play(db, play)


@router.get("/", response_model=list[schemas.Play])
def get_all_plays(db: Session = Depends(get_db)):
    return PlayService.get_all_plays(db)


@router.get("/{play_id}", response_model=schemas.Play)
def get_play(play_id: int, db: Session = Depends(get_db)):
    play = PlayService.get_play(db, play_id)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")
    return play


@router.put("/{play_id}", response_model=schemas.Play)
def update_play(play_id: int, play_update: schemas.PlayCreate, db: Session = Depends(get_db)):
    updated_play = PlayService.update_play(db, play_id, play_update)
    if not updated_play:
        raise HTTPException(status_code=404, detail="Play not found")
    return updated_play


@router.delete("/{play_id}", response_model=schemas.Play)
def delete_play(play_id: int, db: Session = Depends(get_db)):
    deleted_play = PlayService.delete_play(db, play_id)
    if not deleted_play:
        raise HTTPException(status_code=404, detail="Play not found")
    return deleted_play
