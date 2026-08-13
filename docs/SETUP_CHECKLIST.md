# Setup-Checkliste für Teilnehmende

Bitte **vor dem Workshop-Termin** durchgehen, nicht erst live vor Ort — so
bleibt am Tag selbst Zeit für den Workshop statt für Fehlersuche.

Bei Problemen: Fehlermeldung/Screenshot vorab an [Kontakt einfügen] schicken.
Falls bis zum Termin nichts behoben werden kann: trotzdem kommen — es gibt
Pairing mit anderen Teilnehmenden und eine Fallback-Demo.

## Für alle (Spur A und Spur B)

- [ ] Python 3.11 oder neuer installiert (`python --version`)
- [ ] Git installiert (`git --version`)
- [ ] OpenCode installiert und startet
- [ ] `opencode.json` aus `opencode.json.example` erstellt und mit den
      AIHub-Werten befüllt (API-Key als Umgebungsvariable, **nicht** in die
      Datei schreiben — siehe `README.md`, "OpenCode mit dem AIHub verbinden")
- [ ] VPN-Verbindung ins interne Netz funktioniert
- [ ] AIHub über OpenCode erreichbar (kurze Testnachricht schicken, z. B.
      "Hallo, funktionierst du?" — es kommt eine Antwort)
- [ ] Workshop-Repository entpackt bzw. geklont, im Terminal geöffnet
- [ ] Abhängigkeiten installiert:
      ```bash
      uv sync
      # oder: pip install -e ".[dev]"
      ```
      läuft ohne Fehler durch
- [ ] Tests laufen durch:
      ```bash
      pytest
      ```
      Erwartung: `6 passed`
- [ ] Anwendung startet:
      ```bash
      uvicorn src.api:app --reload
      ```
      `http://127.0.0.1:8000/health` antwortet mit `{"status": "ok"}`

## Zusätzlich für Spur B (frei: eigene Commands, Skills, MCP-Server)

- [ ] `.opencode/commands/README.md` und `.opencode/skills/README.md`
      einmal gelesen
- [ ] `mcp-starter/`-Abhängigkeiten installiert:
      ```bash
      pip install -r mcp-starter/requirements.txt
      ```
      läuft ohne Fehler durch
- [ ] MCP-Server lässt sich lokal starten/testen:
      ```bash
      mcp dev mcp-starter/server_template.py
      ```

## Erfolgskriterien

Ihr seid startklar, wenn:

- ✅ `pytest` zeigt `6 passed`
- ✅ Die App unter `http://127.0.0.1:8000/health` antwortet
- ✅ Euer Coding Agent (OpenCode) eine Testnachricht über den AIHub
  beantwortet
- ✅ (Spur B) `mcp-starter/` lässt sich lokal starten

Viel Erfolg beim Workshop!
