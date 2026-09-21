# MCP-Starter (Gruppe B)

Startgerüst für Teilnehmende, die in der freien Workshop-Gruppe einen eigenen
MCP-Server für die Convention App bauen wollen — statt bei einem leeren
Blatt anzufangen.

Zwei Dateien, gleiches Tool (`list_events`, spricht gegen die laufende
Workshop-API):

- **`server_template.py`** — Gerüst mit `# TODO`-Markierungen. Hier fangt
  ihr an: Server erstellen, Tool-Docstring schreiben, Request implementieren,
  Server starten.
- **`server_komplett.py`** — fertige Lösung. Zum Vergleichen, wenn ihr fertig
  seid oder nicht weiterkommt.

Danach: eigene Tools ergänzen (siehe unten) — ausgehend vom Template oder
direkt in der Komplett-Version.

## Setup

1. Workshop-App in einem Terminal starten (siehe Haupt-`README.md`):
   ```bash
   uvicorn src.api:app --reload
   ```
2. In einem zweiten Terminal, im Ordner `mcp-starter/`:
   ```bash
   pip install -r requirements.txt
   ```
3. Setup testen (öffnet den MCP-Inspector im Browser):
   ```bash
   mcp dev server_komplett.py
   ```
   Bewusst die Komplett-Version: `server_template.py` lässt sich mit den
   offenen TODOs noch nicht starten (`mcp` ist dort `None`). Sobald ihr sie
   ausgefüllt habt, funktioniert auch:
   ```bash
   mcp dev server_template.py
   ```

## Eigene Tools ergänzen

Ein neues Tool ist nur eine mit `@mcp.tool()` dekorierte Python-Funktion mit
Type Hints und Docstring — FastMCP generiert das Tool-Schema automatisch
daraus. Beispiel-Anregungen stehen als Kommentar in beiden Server-Dateien,
u. a.:

- freie Kapazität je Veranstaltung berechnen
- Doppelbuchungen über mehrere Veranstaltungen hinweg zusammenfassen
- neu angelegte Veranstaltungen als kurzen Wochenbericht ausgeben

Eigene Ideen sind ausdrücklich erwünscht — die Liste ist nur ein Startpunkt,
keine Vorgabe.

## In OpenCode einbinden

Damit euer Coding Agent den Server als Werkzeug nutzen kann, muss er in
`opencode.json` als MCP-Server eingetragen werden — als neuer Top-Level-Key
`mcp`, **neben** dem bestehenden `provider`-Block, nicht anstelle davon:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "aihub/qwen-3.6-35b-sovereign",
  "mcp": {
    "convention-app-tools": {
      "type": "local",
      "command": ["python", "mcp-starter/server_komplett.py"],
      "enabled": true
    }
  },
  "provider": { "...": "euer bestehender provider-Block bleibt unverändert" }
}
```

`server_komplett.py` durch euren eigenen Dateinamen ersetzen, sobald ihr das
Template ausgefüllt oder erweitert habt. Danach **OpenCode neu starten**
(`/exit`, dann `opencode` erneut) — MCP-Server werden nur beim Start
geladen, eine laufende Session merkt eine nachträgliche Änderung nicht.

**Hinweis:** Das genaue Schema kann sich je OpenCode-Version leicht
unterscheiden — im Zweifel in der aktuellen OpenCode-Dokumentation
gegenprüfen.

Nach dem Neustart testen, ob es wirklich greift — nicht nur, ob der Server
in der Config steht:

```text
Nutze dein verfügbares Tool, um mir alle aktuellen Veranstaltungen
aufzulisten.
```

Erscheint dabei ein sichtbarer Tool-Call in der TUI (nicht nur eine Antwort
aus geratenem Wissen), ist die Einbindung erfolgreich.

## Leitplanken

- Keine neuen Abhängigkeiten außerhalb von `requirements.txt` ohne Grund.
- Kein Zugriff auf externe Dienste außerhalb der lokalen Workshop-API.
- Realistisch in der verbleibenden Zeit umsetzbar bleiben — lieber ein
  Tool, das wirklich läuft, als drei halbfertige.
