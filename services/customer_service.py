from sqlalchemy.orm import Session
import crud
from models import models
from schemas import schemas


class CustomerService:

    @staticmethod
    def create_customer(db: Session, customer: schemas.CustomerCreate):
        return crud.create_entity(db, models.Customer, customer)

    @staticmethod
    def get_customer(db: Session, customer_id: int):
        return crud.get_entity(db, models.Customer, customer_id)

    @staticmethod
    def get_all_customers(db: Session):
        return crud.get_all_entities(db, models.Customer)

    @staticmethod
    def update_customer(db: Session, customer_id: int, updated_customer: schemas.CustomerCreate):
        return crud.update_entity(db, models.Customer, customer_id, updated_customer)

    @staticmethod
    def delete_customer(db: Session, customer_id: int):
        return crud.delete_entity(db, models.Customer, customer_id)
