from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from services import directory_service
from schemas import schemas

router = APIRouter(prefix="/directors", tags=["Directors"])


@router.post("/", response_model=schemas.Director)
def create_director(director: schemas.DirectorCreate, db: Session = Depends(get_db)):
    return directory_service.create_director(db, director)


@router.get("/", response_model=list[schemas.Director])
def get_all_directors(db: Session = Depends(get_db)):
    return directory_service.get_all_directors(db)


@router.get("/{director_id}", response_model=schemas.Director)
def get_director(director_id: int, db: Session = Depends(get_db)):
    director = directory_service.get_director(db, director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return director


@router.put("/{director_id}", response_model=schemas.Director)
def update_director(director_id: int, director_update: schemas.DirectorCreate, db: Session = Depends(get_db)):
    updated_director = directory_service.update_director(db, director_id, director_update)
    if not updated_director:
        raise HTTPException(status_code=404, detail="Director not found")
    return updated_director


@router.delete("/{director_id}", response_model=schemas.Director)
def delete_director(director_id: int, db: Session = Depends(get_db)):
    deleted_director = directory_service.delete_director(db, director_id)
    if not deleted_director:
        raise HTTPException(status_code=404, detail="Director not found")
    return deleted_director
