# ISSUE-03 – Eingabevalidierung für Veranstaltungskapazität

> Bonus-Aufgabe für längere Workshops.

## Problem

Derzeit kann eine Veranstaltung mit einer sinnlosen Kapazität angelegt werden.

## Akzeptanzkriterien

1. `max_participants` muss mindestens `1` sein.
2. Ungültige Requests sollen über die normale FastAPI/Pydantic-Validierung abgewiesen werden.
3. Es soll keine redundante manuelle Validierungslogik in der API-Route entstehen.
4. Geeignete Tests werden ergänzt.
5. Bestehende Tests bleiben erfolgreich.
