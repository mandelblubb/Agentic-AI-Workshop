# Prompt: eigenes Issue generieren lassen

Für Gruppen, die mit ISSUE-01 und ISSUE-02 fertig sind und noch Zeit haben (Bonus,
analog zu `issues/ISSUE-03-validation.md`): Teilnehmende überlegen sich selbst eine
kleine Feature-Idee, lassen sich daraus per Prompt ein Issue im Stil der bestehenden
Tickets generieren und lassen ihren Coding Agenten es anschließend umsetzen.

Der Prompt prüft die Idee zuerst gegen feste Leitplanken (Architektur, Zeitrahmen,
keine neuen Dependencies/Auth/externe Aufrufe) und schlägt bei Bedarf eine kleinere
Variante vor, damit kein Ticket entsteht, das in der verbleibenden Zeit nicht lösbar ist.

## Prompt zum Copy-Paste

```text
Du hilfst mir, ein neues Workshop-Issue im Stil der bestehenden Issues in
issues/ISSUE-01-registration.md, issues/ISSUE-02-security-review.md und
issues/ISSUE-03-validation.md zu formulieren.

## Projektkontext
Eine kleine FastAPI-Anwendung zur Verwaltung von Fortbildungsveranstaltungen
(Titel, Datum, Ort, maximale Teilnehmerzahl, Anmeldungen mit Name/Agency).
Architektur strikt dreigeteilt: src/models.py (Pydantic-Modelle),
src/service.py (Fachlogik, eigene Exceptions, In-Memory-Zustand),
src/api.py (dünne HTTP-Routen, Exception-zu-HTTPException-Mapping).
Verbindliche Regeln stehen in AGENTS.md.

## Feste Leitplanken für das neue Issue
- Nur Änderungen an src/models.py, src/service.py, src/api.py und
  passenden Tests unter tests/.
- Keine neuen Dependencies, keine Datenbank, keine externen Netzwerkaufrufe.
- Keine Authentifizierung, keine Rollen/Rechte.
- Muss realistisch in 15-20 Minuten von einem Coding Agenten umsetzbar sein
  (klein und klar geschnitten, nicht mehrere Features gleichzeitig).
- Keine personenbezogenen Daten in Fehlermeldungen oder Logs.

## Meine Feature-Idee (roh, ungeschliffen)
<<<HIER DEINE IDEE IN 1-3 SÄTZEN EINFÜGEN>>>

## Aufgabe
1. Prüfe zuerst kurz, ob die Idee innerhalb der Leitplanken in der
   verfügbaren Zeit umsetzbar ist. Falls nicht: schlage eine kleinere,
   passende Variante vor und erkläre in 1-2 Sätzen, warum du kürzt.
2. Formuliere daraus ein vollständiges Issue in genau diesem Aufbau
   (angelehnt an ISSUE-01):
   - Überschrift "# ISSUE-XX – <kurzer Titel>"
   - "## Ausgangslage" (aktueller Stand, kurz)
   - "## User Story" (Als ... möchte ich ..., damit ...)
   - "## Anforderungen" (relevante Datenfelder, ggf. neuer Endpoint mit
     HTTP-Methode/Pfad und Beispiel-Request als JSON)
   - "## Akzeptanzkriterien" als nummerierte Liste, konkret und testbar
     (inkl. erwarteter HTTP-Statuscodes bei Fehlerfällen), zusätzlich
     immer: "Die bestehende Architektur aus AGENTS.md ist einzuhalten.",
     "Neue Funktionalität wird durch Tests abgesichert.",
     "Alle bestehenden Tests bleiben erfolgreich."
   - "## Nicht Teil dieses Issues" (was explizit ausgeschlossen ist)
3. Halte die Sprache Deutsch, sachlich, im gleichen Ton wie die
   bestehenden Issues.

Gib mir am Ende nur das fertige Markdown-Issue aus, bereit zum Speichern
als issues/ISSUE-XX-<kurzer-slug>.md.
```

## Ablauf für Teilnehmende

1. Feature-Idee in den Platzhalter einsetzen und den Prompt an die KI schicken.
2. Ergebnis als `issues/ISSUE-XX-<slug>.md` speichern.
3. Coding Agenten mit dem neuen Issue starten lassen (gleicher Ablauf wie bei ISSUE-01).
4. Wie gewohnt: Tests ausführen, `git diff` prüfen, Akzeptanzkriterien gegen das Ergebnis checken.
