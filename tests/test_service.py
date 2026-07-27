from datetime import date

import pytest

from src.models import EventCreate
from src.service import EventNotFoundError, EventService


def test_service_creates_incrementing_ids() -> None:
    service = EventService()

    first = service.create_event(
        EventCreate(
            title="A",
            date=date(2026, 10, 1),
            location="München",
            max_participants=10,
        )
    )
    second = service.create_event(
        EventCreate(
            title="B",
            date=date(2026, 10, 2),
            location="Berlin",
            max_participants=15,
        )
    )

    assert first.id == 1
    assert second.id == 2


def test_service_raises_for_unknown_event() -> None:
    service = EventService()

    with pytest.raises(EventNotFoundError):
        service.get_event(123)
