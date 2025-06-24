from sqlalchemy.orm import Session
import crud
from models import models
from schemas import schemas


class TicketService:

    @staticmethod
    def create_ticket(db: Session, ticket: schemas.TicketCreate):
        return crud.create_entity(db, models.Ticket, ticket)

    @staticmethod
    def get_ticket(db: Session, ticket_id: int):
        return crud.get_entity(db, models.Ticket, ticket_id)

    @staticmethod
    def get_all_tickets(db: Session):
        return crud.get_all_entities(db, models.Ticket)

    @staticmethod
    def update_ticket(db: Session, ticket_id: int, updated_ticket: schemas.TicketCreate):
        return crud.update_entity(db, models.Ticket, ticket_id, updated_ticket)

    @staticmethod
    def delete_ticket(db: Session, ticket_id: int):
        return crud.delete_entity(db, models.Ticket, ticket_id)
