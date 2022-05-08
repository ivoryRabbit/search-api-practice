from typing import List
from pydantic import BaseModel, Field


class ItemOut(BaseModel):
    item_id: str
    title: str
    score: float = Field(..., gt=0.0)


class ResponseOut(BaseModel):
    data: List[ItemOut]
