from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from services.ticket_service import TicketService
from schemas import schemas

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post("/", response_model=schemas.Ticket)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    return TicketService.create_ticket(db, ticket)


@router.get("/", response_model=list[schemas.Ticket])
def get_all_tickets(db: Session = Depends(get_db)):
    return TicketService.get_all_tickets(db)


@router.get("/{ticket_id}", response_model=schemas.Ticket)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = TicketService.get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.put("/{ticket_id}", response_model=schemas.Ticket)
def update_ticket(ticket_id: int, ticket_update: schemas.TicketCreate, db: Session = Depends(get_db)):
    updated_ticket = TicketService.update_ticket(db, ticket_id, ticket_update)
    if not updated_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return updated_ticket


@router.delete("/{ticket_id}", response_model=schemas.Ticket)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    deleted_ticket = TicketService.delete_ticket(db, ticket_id)
    if not deleted_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return deleted_ticket
