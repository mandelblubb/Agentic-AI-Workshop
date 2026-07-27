from fastapi.testclient import TestClient


def test_health(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_read_event(client: TestClient) -> None:
    create_response = client.post(
        "/events",
        json={
            "title": "Fortbildung Cybercrime",
            "date": "2026-10-12",
            "location": "München",
            "max_participants": 30,
        },
    )

    assert create_response.status_code == 201
    event = create_response.json()
    assert event["id"] == 1
    assert event["title"] == "Fortbildung Cybercrime"

    read_response = client.get("/events/1")
    assert read_response.status_code == 200
    assert read_response.json() == event


def test_list_events(client: TestClient) -> None:
    client.post(
        "/events",
        json={
            "title": "Fortbildung A",
            "date": "2026-10-12",
            "location": "München",
            "max_participants": 20,
        },
    )
    client.post(
        "/events",
        json={
            "title": "Fortbildung B",
            "date": "2026-11-05",
            "location": "Berlin",
            "max_participants": 15,
        },
    )

    response = client.get("/events")
    assert response.status_code == 200
    assert [event["title"] for event in response.json()] == [
        "Fortbildung A",
        "Fortbildung B",
    ]


def test_unknown_event_returns_404(client: TestClient) -> None:
    response = client.get("/events/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Event not found"
