# MCP-Starter (Spur B)

Startgerüst für Teilnehmende, die in der freien Workshop-Spur einen eigenen
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
3. Server lokal testen (öffnet den MCP-Inspector im Browser):
   ```bash
   mcp dev server_template.py
   # oder, nach Vergleich mit der Lösung:
   mcp dev server_komplett.py
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

Damit euer Coding Agent den Server als Werkzeug nutzen kann, muss er in der
OpenCode-Konfiguration als MCP-Server eingetragen werden (Konfigurationsdatei
und genaue Schlüsselnamen können sich je OpenCode-Version leicht
unterscheiden — im Zweifel in der aktuellen OpenCode-Dokumentation
gegenprüfen). Grundsätzlich braucht ein solcher Eintrag:

- den Startbefehl (`python`, dann `server_komplett.py` bzw. euer eigener
  Dateiname, sobald das Template ausgefüllt oder erweitert ist)
- den Arbeitsordner (`mcp-starter/`)

Nach dem Eintragen sollte euer Agent das Tool `list_events` (und alle
selbst ergänzten Tools) in Prompts nutzen können.

## Leitplanken

- Keine neuen Abhängigkeiten außerhalb von `requirements.txt` ohne Grund.
- Kein Zugriff auf externe Dienste außerhalb der lokalen Workshop-API.
- Realistisch in der verbleibenden Zeit umsetzbar bleiben — lieber ein
  Tool, das wirklich läuft, als drei halbfertige.
