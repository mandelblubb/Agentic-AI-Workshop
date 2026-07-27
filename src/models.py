from datetime import date

from pydantic import BaseModel, Field


class EventCreate(BaseModel):
    title: str = Field(min_length=1)
    date: date
    location: str = Field(min_length=1)
    max_participants: int


class Event(BaseModel):
    id: int
    title: str
    date: date
    location: str
    max_participants: int
