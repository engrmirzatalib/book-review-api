from fastapi import APIRouter
from models.review import Review
from database.database import reviews

router = APIRouter()

@router.get("/reviews")
def get_reviews():
    return reviews

@router.post("/reviews")
def create_review(review: Review):
    reviews.append(review)
    return {"message": "Review added successfully"}
