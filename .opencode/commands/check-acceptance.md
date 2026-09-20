---
description: Prüft die aktuelle Implementierung gegen die Akzeptanzkriterien eines Issues und listet offene Punkte auf. Ändert keine Dateien.
agent: reviewer
---

# check-acceptance

Prüft, ob der aktuelle Stand des Repositories die Akzeptanzkriterien aus
`$ARGUMENTS` erfüllt (Standard, falls kein Argument übergeben wurde: das
zuletzt bearbeitete Issue unter `issues/`).

Dies ist ein reiner Prüf-Befehl. Ändere dabei **keine** Dateien.

## Ablauf

1. Lies die angegebene Issue-Datei und extrahiere die Akzeptanzkriterien.
2. Lies `AGENTS.md` und den aktuellen Stand von `src/`.
3. Führe `pytest` aus und `git diff` aus, um den tatsächlichen Implementierungsstand zu sehen.
4. Gehe jedes Akzeptanzkriterium einzeln durch: erfüllt / nicht erfüllt / unklar,
   jeweils mit kurzer, konkreter Begründung (Dateiverweis wo möglich).
5. Liste am Ende offene Punkte und mögliche Restrisiken.

## Beispiel-Aufruf

```text
/check-acceptance issues/ISSUE-01-registration.md
```
