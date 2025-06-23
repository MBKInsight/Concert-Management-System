from contextlib import asynccontextmanager
from fastapi import FastAPI

from database.database import engine
from models.models import Base
from routers import actors, directors, customers, plays, tickets, showtimes
from auth.auth import router as auth_router


# Lifespan context for startup and shutdown tasks
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create database tables
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown: Add any cleanup logic here if needed


# Initialize FastAPI app with lifespan
app = FastAPI(
    title="Sierra Leone Concert API",
    lifespan=lifespan
)

# Include routers
app.include_router(actors.router)
app.include_router(directors.router)
app.include_router(customers.router)
app.include_router(plays.router)
app.include_router(tickets.router)
app.include_router(showtimes.router)
app.include_router(auth_router)


# Root endpoint
@app.get("/")
def root():
    return {"message": "🎭 Welcome to Sierra Leone Concert Management API"}
