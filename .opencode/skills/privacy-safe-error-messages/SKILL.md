---
name: privacy-safe-error-messages
description: Verwende dieses Skill, wenn Fehlerbehandlung, Fehlermeldungen, HTTPException-Details oder Logging in dieser Codebasis geschrieben oder überprüft werden - insbesondere wenn dabei personenbezogene Daten von Teilnehmenden (Name, Agency, o. Ä.) im Spiel sein könnten, z. B. bei Konflikten wie Doppelanmeldung.
---

# Privacy-safe Fehlermeldungen

Hintergrundwissen für diese Codebasis: API-Fehlermeldungen und Logs dürfen
**keine personenbezogenen Daten** der beteiligten Personen enthalten -
weder direkt noch indirekt (z. B. durch Rückschluss aus dem Wortlaut).

## Regel

- Fehlermeldungen dürfen `name` und `agency` (oder vergleichbare
  personenbezogene Felder) einer bereits gespeicherten Person **nicht**
  enthalten - auch nicht bei Konfliktfällen wie einer Doppelanmeldung.
- Logs dürfen ebenfalls keine personenbezogenen Daten ausgeben.
- Diese Regel steht auch in `AGENTS.md`: *"Keine personenbezogenen Daten in
  Logs ausgeben. API-Fehlermeldungen sollen keine unnötigen
  personenbezogenen Daten enthalten."*

## Negativbeispiel (nicht zulässig)

```json
{
  "detail": "Max Beispiel von Polizei Beispielstadt ist bereits angemeldet"
}
```

## Positivbeispiel (zulässig)

```json
{
  "detail": "Registration already exists"
}
```

Neutral formuliert, weiterhin mit korrektem HTTP-Statuscode (z. B. 409),
aber ohne Daten der betroffenen Person preiszugeben.

## Anwendung

Beim Schreiben oder Überprüfen von Fehlerfällen (`HTTPException`,
Service-Exceptions, Logging-Aufrufen) in dieser Codebasis:

1. Prüfen, ob die Fehlermeldung Daten einer konkreten, bereits gespeicherten
   Person offenlegt - auch indirekt.
2. Falls ja: neutral formulieren, ohne Informationsverlust für den
   HTTP-Status/die Fehlerursache.
3. Einen Test ergänzen, der sicherstellt, dass der Response-Body/Log-Output
   keine sensiblen Felder (`name`, `agency`) enthält.
