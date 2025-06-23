from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from services.showtime_service import ShowTimeService
from schemas import schemas

router = APIRouter(prefix="/showtimes", tags=["Showtimes"])


@router.post("/", response_model=schemas.ShowTime)
def create_showtime(showtime: schemas.ShowTimeCreate, db: Session = Depends(get_db)):
    return ShowTimeService.create_showtime(db, showtime)


@router.get("/", response_model=list[schemas.ShowTime])
def get_all_showtimes(db: Session = Depends(get_db)):
    return ShowTimeService.get_all_showtimes(db)


@router.get("/{showtime_id}", response_model=schemas.ShowTime)
def get_showtime(showtime_id: int, db: Session = Depends(get_db)):
    showtime = ShowTimeService.get_showtime(db, showtime_id)
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return showtime


@router.put("/{showtime_id}", response_model=schemas.ShowTime)
def update_showtime(showtime_id: int, showtime_update: schemas.ShowTimeCreate, db: Session = Depends(get_db)):
    updated_showtime = ShowTimeService.update_showtime(db, showtime_id, showtime_update)
    if not updated_showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return updated_showtime


@router.delete("/{showtime_id}", response_model=schemas.ShowTime)
def delete_showtime(showtime_id: int, db: Session = Depends(get_db)):
    deleted_showtime = ShowTimeService.delete_showtime(db, showtime_id)
    if not deleted_showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return deleted_showtime
