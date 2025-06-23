from database.database import engine
from models.models import Base

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)