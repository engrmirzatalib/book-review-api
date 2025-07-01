from pydantic import BaseModel
from typing import Optional

class Review(BaseModel):
    id: int
    book_id: int
    reviewer_name: str
    rating: int
    comment: Optional[str] = None
