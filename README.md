# 🎵 Concert Management System API

This is a backend system built with FastAPI that helps manage concert events. It lets users manage actors, directors, plays, showtimes, customers, and ticket bookings. The system is well-organized, uses JWT for security, and follows good coding practices.



## 📌 Overview

This system helps manage:
- 🎭 Actors and 🎬 Directors
- 📅 Plays and Showtimes
- 👥 Customers
- 🎫 Ticket Bookings

It’s built with:
- *FastAPI* for the API
- *PostgreSQL* as the database
- *SQLAlchemy* for database operations
- *JWT* for secure login



## 📁 Project Folder Structure

Concert-Management-System/

├── auth/ # Handles login and JWT

├── concert_api/ # Holds requirements.txt file

├── database/ # Database settings and environment file

├── models/ # Database tables using SQLAlchemy

├── routers/ # Defines API endpoints

├── schemas/ # Validates data using Pydantic

├── services/ # Business logic

├── create_tables.py # Creates tables in the database

├── crud.py # Performs DB actions

├── main.py # Starts the FastAPI app





## 🗃 Database

We use *PostgreSQL* with *SQLAlchemy*.

### Main Tables:
- Actors: id, name, age, experience  
- Customers: id, name, email, phone  
- Directors: id, name, awards  
- Plays: id, title, genre, director_id  
- Showtimes: id, play_id, time, venue  
- Tickets: id, customer_id, showtime_id, seat_number  

### Relationships:
- One Director can direct many Plays  
- One Play can have many Showtimes  
- One Customer can book many Tickets  



## ⚙ API Technology

- *FastAPI* – Builds the API
- *SQLAlchemy* – Handles the database
- *Pydantic* – Validates input/output
- *Uvicorn* – Runs the server
- *JWT* – Secures routes with tokens



## 📂 Example Endpoints

| Method | Route            | What It Does              |
|--------|------------------|---------------------------|
| GET    | /actors/         | Shows all actors          |
| POST   | /tickets/        | Books a ticket            |
| POST   | /customers/      | Registers a customer      |
| POST   | /plays/          | Adds a new play           |



## 🧪 API Testing

You can test the API with:
- *Swagger UI* at http://localhost:8000/docs
- *ReDoc* at http://localhost:8000/redoc

### To Use:
1. Get a token from /token
2. Click "Authorize" and paste the token
3. Try out the routes directly

You can also use *Postman*:
- Add the token in the header as Authorization: Bearer <token>



## 🛠 How to Set Up the Project

### Requirements:
- Python 3.11 or newer
- PostgreSQL

### Steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/concert-management-system.git
cd concert-management-system
Set up and activate a virtual environment:

bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
Install required libraries:

bash
pip install -r concert_api/requirements.txt
Create a .env file inside the database/ folder:

env
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
Create the database tables:

bash
python create_tables.py
Run the FastAPI server:

bash
uvicorn main:app --reload
🔮 Future Improvements
Add tests using pytest

Add CORS for frontend integration

Add user roles (admin/user)

Support for API versioning and rate limiting

📚 Useful Links
FastAPI Docs

SQLAlchemy Docs

Pydantic Docs

JWT.io

Uvicorn

👥 Authors
Mohamed Bockarie Koroma GitHub: @MBKInsight
Promise G Sandy GitHub: @Promisegsandy
Da-Moi GitHub: @Da-moi

📄 License
This project is under the MIT License.

