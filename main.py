from fastapi import FastAPI
from routers import book_routes, review_routes

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Book Review API!"}

app.include_router(book_routes.router)
app.include_router(review_routes.router)

