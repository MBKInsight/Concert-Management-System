from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from services.customer_service import CustomerService
from schemas import schemas

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return CustomerService.create_customer(db, customer)


@router.get("/", response_model=list[schemas.Customer])
def get_all_customers(db: Session = Depends(get_db)):
    return CustomerService.get_all_customers(db)


@router.get("/{customer_id}", response_model=schemas.Customer)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = CustomerService.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.put("/{customer_id}", response_model=schemas.Customer)
def update_customer(customer_id: int, customer_update: schemas.CustomerCreate, db: Session = Depends(get_db)):
    updated_customer = CustomerService.update_customer(db, customer_id, customer_update)
    if not updated_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer


@router.delete("/{customer_id}", response_model=schemas.Customer)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    deleted_customer = CustomerService.delete_customer(db, customer_id)
    if not deleted_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return deleted_customer
