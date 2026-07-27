# Lösungshinweise für die Workshop-Leitung

## ISSUE-01 – sinnvolle Struktur

Typischerweise sollten entstehen:

- ein `Registration`-Modell in `src/models.py`
- Registrierungszustand im `EventService`
- Service-Methoden zur Anmeldung
- eigene Exceptions für unbekanntes Event, ausgebucht und Doppelanmeldung
- Mapping auf HTTP 404/409 in `src/api.py`
- Tests auf Service- und/oder API-Ebene

## Normalisierung

Für Doppelanmeldungen ist beispielsweise plausibel:

```python
value.strip().casefold()
```

`casefold()` ist für robuste Unicode-Groß-/Kleinschreibung geeigneter als nur `lower()`.

## Datenschutz

Ungünstig:

```text
"Max Beispiel von Polizei Beispielstadt ist bereits angemeldet"
```

Besser:

```text
"Registration already exists"
```

## ISSUE-03

Typischerweise sauber im Pydantic-Modell:

```python
max_participants: int = Field(ge=1)
```
