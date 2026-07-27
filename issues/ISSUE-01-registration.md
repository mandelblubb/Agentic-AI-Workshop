# ISSUE-01 – Teilnehmer zu Veranstaltungen anmelden

## Ausgangslage

Die Anwendung kann Veranstaltungen anlegen, auflisten und einzeln abrufen.

Nun soll die Anmeldung von Teilnehmerinnen und Teilnehmern ergänzt werden.

## User Story

Als Veranstaltungsorganisator möchte ich Personen zu einer Veranstaltung anmelden können,
damit die verfügbaren Plätze verwaltet werden können.

## Anforderungen

Eine Anmeldung enthält:

- `name`
- `agency` – die Dienststelle bzw. Organisation

### Neuer Endpoint

```http
POST /events/{event_id}/registrations
```

Beispiel-Request:

```json
{
  "name": "Max Beispiel",
  "agency": "Polizei Beispielstadt"
}
```

## Akzeptanzkriterien

1. Eine Person kann zu einer existierenden Veranstaltung angemeldet werden.
2. Anmeldung bei einer unbekannten Veranstaltung liefert HTTP 404.
3. Eine Veranstaltung darf nicht überbucht werden.
4. Bei ausgebuchter Veranstaltung liefert die API HTTP 409.
5. Dieselbe Person darf innerhalb einer Veranstaltung nicht doppelt angemeldet werden.
6. Für die Erkennung einer Doppelanmeldung werden `name` und `agency` gemeinsam betrachtet.
7. Groß-/Kleinschreibung und führende bzw. nachfolgende Leerzeichen sollen bei der Prüfung auf Doppelanmeldungen ignoriert werden.
8. Bei Doppelanmeldung liefert die API HTTP 409.
9. Die bestehende Architektur aus `AGENTS.md` ist einzuhalten.
10. Neue Funktionalität wird durch Tests abgesichert.
11. Alle bestehenden Tests bleiben erfolgreich.
12. `README.md` wird um ein kurzes API-Beispiel für Registrierungen ergänzt.

## Nicht Teil dieses Issues

- Persistente Datenbank
- Authentifizierung
- Rollen- und Rechtesystem
- Löschen von Anmeldungen
- Bearbeiten von Anmeldungen
- Externe Schnittstellen
