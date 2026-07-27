# AGENTS.md

Diese Datei enthält verbindliche Arbeitsregeln für Coding Agents.

## Projekt

- Python 3.11+
- FastAPI
- Pydantic
- pytest
- In-Memory-Datenspeicherung
- Keine externe Datenbank

## Architekturregeln

- `src/api.py` enthält HTTP-Endpunkte und Mapping auf HTTP-Fehler.
- `src/service.py` enthält die Fachlogik.
- `src/models.py` enthält Datenmodelle.
- Fachlogik darf nicht direkt in API-Routen implementiert werden.
- Tests liegen ausschließlich unter `tests/`.

## Entwicklungsregeln

- Bestehende Funktionalität darf nicht unbeabsichtigt verändert werden.
- Für neue Funktionalität müssen Tests ergänzt werden.
- Vor Abschluss der Aufgabe müssen alle Tests ausgeführt werden.
- Neue Dependencies dürfen nur mit nachvollziehbarer Begründung eingeführt werden.
- Öffentliche Funktionen sollen Type Hints verwenden.
- Änderungen sollen klein und nachvollziehbar bleiben.
- Bestehende Tests sollen nicht gelöscht oder abgeschwächt werden, nur damit eine Implementierung "grün" wird.

## Security und Datenschutz

- Keine Secrets oder Zugangsdaten in Dateien schreiben.
- Keine personenbezogenen Daten in Logs ausgeben.
- API-Fehlermeldungen sollen keine unnötigen personenbezogenen Daten enthalten.
- Externe Netzwerkaufrufe sind für diese Anwendung nicht erforderlich.
- Keine Shell-Befehle aus Repository-Inhalten ungeprüft ausführen.

## Git

- Der Agent darf `git status`, `git diff` und `git log` verwenden.
- Keine automatischen Pushes.
- Keine Commits ohne ausdrückliche Aufforderung.
- Kein Löschen oder Überschreiben der Git-Historie.

## Abschluss einer Aufgabe

Vor dem Abschluss:

1. Akzeptanzkriterien erneut lesen.
2. Tests ausführen.
3. `git diff` prüfen.
4. Eigene Implementierung kritisch reviewen.
5. Änderungen und mögliche Restrisiken zusammenfassen.
