# Book Review API

This is a backend API project developed using FastAPI. It allows users to manage books and their reviews through RESTful endpoints. The application uses in-memory data storage and provides interactive documentation using Swagger UI.

## Features

- Add new books
- View all books
- Add reviews to books
- View all reviews
- Built-in Swagger documentation for testing

## Tech Stack

- Python 3
- FastAPI
- Uvicorn (ASGI server)
- Pydantic for data validation
- Swagger UI (auto-generated)

## Project Structure

book_review_api/
│
├── main.py          -> Main application file  
├── models/          -> Contains data models (schemas)  
├── routers/         -> Contains route handlers  
└── database/        -> In-memory data and logic

## How to Run

1. Open terminal and activate virtual environment
2. Install dependencies:

```bash
pip install fastapi uvicorn

Start the server:   uvicorn main:app --reload
Open the browser:

Home: http://127.0.0.1:8000

API Docs: http://127.0.0.1:8000/docs

| Method | Endpoint   | Description      |
| ------ | ---------- | ---------------- |
| GET    | `/`        | Home page        |
| GET    | `/books`   | List all books   |
| POST   | `/books`   | Add a new book   |
| GET    | `/reviews` | List all reviews |
| POST   | `/reviews` | Add a new review |

Author
Mirza Talib
B.Tech in Electronics and Communication Engineering
Jaipur Engineering College and Research Centre (JECRC)
Email: talibmirza5267@gmail.com
GitHub: https://github.com/engrmirzatalib/book-review-api

Status
This project is a basic implementation of a book and review management backend using FastAPI. Further enhancements may include database integration, user authentication, and deployment.
