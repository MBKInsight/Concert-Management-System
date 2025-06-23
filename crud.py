from sqlalchemy.orm import Session

from models import models


# Generic CRUD Template

def create_entity(db: Session, entity_model, entity_schema):
    db_entity = entity_model(**entity_schema.dict())
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity


def get_entity(db: Session, entity_model, entity_id: int):
    return db.query(entity_model).filter(entity_model.id == entity_id).first()


def get_all_entities(db: Session, entity_model):
    return db.query(entity_model).all()


def update_entity(db: Session, entity_model, entity_id: int, updated_schema):
    db_entity = get_entity(db, entity_model, entity_id)
    if not db_entity:
        return None
    for field, value in updated_schema.dict().items():
        setattr(db_entity, field, value)
    db.commit()
    db.refresh(db_entity)
    return db_entity


def delete_entity(db: Session, entity_model, entity_id: int):
    db_entity = get_entity(db, entity_model, entity_id)
    if db_entity:
        db.delete(db_entity)
        db.commit()
    return db_entity


# Specific shortcuts (optional)
def create_play(db: Session, play):
    return create_entity(db, models.Play, play)


def get_play(db: Session, play_id: int):
    return get_entity(db, models.Play, play_id)


def get_all_plays(db: Session):
    return get_all_entities(db, models.Play)


def update_play(db: Session, play_id: int, updated_play):
    return update_entity(db, models.Play, play_id, updated_play)


def delete_play(db: Session, play_id: int):
    return delete_entity(db, models.Play, play_id)


def create_actor(db: Session, actor):
    return create_entity(db, models.Actor, actor)


def get_actor(db: Session, actor_id: int):
    return get_entity(db, models.Actor, actor_id)


def get_all_actors(db: Session):
    return get_all_entities(db, models.Actor)


def update_actor(db: Session, actor_id: int, updated_actor):
    return update_entity(db, models.Actor, actor_id, updated_actor)


def delete_actor(db: Session, actor_id: int):
    return delete_entity(db, models.Actor, actor_id)


def create_director(db: Session, director):
    return create_entity(db, models.Director, director)


def get_director(db: Session, director_id: int):
    return get_entity(db, models.Director, director_id)


def get_all_directors(db: Session):
    return get_all_entities(db, models.Director)


def update_director(db: Session, director_id: int, updated_director):
    return update_entity(db, models.Director, director_id, updated_director)


def delete_director(db: Session, director_id: int):
    return delete_entity(db, models.Director, director_id)


def create_customer(db: Session, customer):
    return create_entity(db, models.Customer, customer)


def get_customer(db: Session, customer_id: int):
    return get_entity(db, models.Customer, customer_id)


def get_all_customers(db: Session):
    return get_all_entities(db, models.Customer)


def update_customer(db: Session, customer_id: int, updated_customer):
    return update_entity(db, models.Customer, customer_id, updated_customer)


def delete_customer(db: Session, customer_id: int):
    return delete_entity(db, models.Customer, customer_id)


def create_ticket(db: Session, ticket):
    return create_entity(db, models.Ticket, ticket)


def get_ticket(db: Session, ticket_id: int):
    return get_entity(db, models.Ticket, ticket_id)


def get_all_tickets(db: Session):
    return get_all_entities(db, models.Ticket)


def update_ticket(db: Session, ticket_id: int, updated_ticket):
    return update_entity(db, models.Ticket, ticket_id, updated_ticket)


def delete_ticket(db: Session, ticket_id: int):
    return delete_entity(db, models.Ticket, ticket_id)


def create_showtime(db: Session, showtime):
    return create_entity(db, models.ShowTime, showtime)


def get_showtime(db: Session, showtime_id: int):
    return get_entity(db, models.ShowTime, showtime_id)


def get_all_showtimes(db: Session):
    return get_all_entities(db, models.ShowTime)


def update_showtime(db: Session, showtime_id: int, updated_showtime):
    return update_entity(db, models.ShowTime, showtime_id, updated_showtime)


def delete_showtime(db: Session, showtime_id: int):
    return delete_entity(db, models.ShowTime, showtime_id)
