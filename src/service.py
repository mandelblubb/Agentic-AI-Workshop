from src.models import Event, EventCreate


class EventNotFoundError(Exception):
    pass


class EventService:
    def __init__(self) -> None:
        self._events: dict[int, Event] = {}
        self._next_id = 1

    def reset(self) -> None:
        self._events.clear()
        self._next_id = 1

    def create_event(self, payload: EventCreate) -> Event:
        event = Event(id=self._next_id, **payload.model_dump())
        self._events[event.id] = event
        self._next_id += 1
        return event

    def list_events(self) -> list[Event]:
        return list(self._events.values())

    def get_event(self, event_id: int) -> Event:
        try:
            return self._events[event_id]
        except KeyError as exc:
            raise EventNotFoundError(f"Event {event_id} not found") from exc
