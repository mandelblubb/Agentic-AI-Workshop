# ISSUE-02 – Ergebnis des Security- und Datenschutz-Reviews

> Dieses Issue erst bearbeiten, wenn die Workshop-Leitung es freigibt.

## Review-Finding

Bei einer Doppelanmeldung darf die API **keine personenbezogenen Informationen
der bereits gespeicherten Person** in der Fehlermeldung zurückgeben.

Eine Implementierung wie

```json
{
  "detail": "Max Beispiel von Polizei Beispielstadt ist bereits angemeldet"
}
```

ist daher nicht zulässig.

## Anforderungen

1. Die API muss bei Doppelanmeldung weiterhin HTTP 409 liefern.
2. Die Fehlermeldung darf weder `name` noch `agency` der vorhandenen Anmeldung enthalten.
3. Eine neutrale Fehlermeldung ist ausreichend, beispielsweise:

```json
{
  "detail": "Registration already exists"
}
```

4. Prüfe, ob personenbezogene Daten anderweitig unnötig in Fehlermeldungen oder Logs erscheinen.
5. Ergänze oder verbessere Tests so, dass dieses Datenschutzverhalten dauerhaft abgesichert ist.
6. Alle Tests müssen erfolgreich sein.

## Review-Auftrag an den Agenten

Vor Änderungen:

- prüfe die aktuelle Implementierung,
- benenne konkret, ob das Finding tatsächlich zutrifft,
- beschreibe die kleinste sinnvolle Korrektur.

Erst danach soll Code verändert werden.
