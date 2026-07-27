from fastapi import FastAPI, HTTPException

from src.models import Event, EventCreate
from src.service import EventNotFoundError, EventService

app = FastAPI(title="Workshop Event API", version="0.1.0")
service = EventService()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/events", response_model=Event, status_code=201)
def create_event(payload: EventCreate) -> Event:
    return service.create_event(payload)


@app.get("/events", response_model=list[Event])
def list_events() -> list[Event]:
    return service.list_events()


@app.get("/events/{event_id}", response_model=Event)
def get_event(event_id: int) -> Event:
    try:
        return service.get_event(event_id)
    except EventNotFoundError as exc:
        raise HTTPException(status_code=404, detail="Event not found") from exc
