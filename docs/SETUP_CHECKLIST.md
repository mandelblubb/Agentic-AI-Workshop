# Setup-Checkliste für Teilnehmende

Bitte **vor dem Workshop-Termin** durchgehen, nicht erst live vor Ort — so
bleibt am Tag selbst Zeit für den Workshop statt für Fehlersuche.

Den **API-Key für den AIHub bekommt ihr zu Beginn des Workshops** — ihr müsst
ihn vorab nicht beantragen, und ein VPN ist nicht nötig. Alles andere auf
dieser Liste lässt sich vorab erledigen; am Workshop-Tag bleibt dann nur noch
das Setzen einer Umgebungsvariablen.

Bei Problemen: Fehlermeldung/Screenshot vorab an [Kontakt einfügen] schicken.
Falls bis zum Termin nichts behoben werden kann: trotzdem kommen — es gibt
Pairing mit anderen Teilnehmenden und eine Fallback-Demo.

## Für alle (Gruppe A und Gruppe B)

- [ ] Python 3.11 oder neuer installiert (`python --version`)
- [ ] Git installiert (`git --version`)
- [ ] Node.js/npm installiert (`node --version`) — wird von OpenCode benötigt
- [ ] OpenCode installiert, **mindestens Version 1.18**:
      ```bash
      opencode --version
      ```
      Ältere Versionen (1.16.x) melden Verbindungsfehler nicht im Terminal
      — die Fehlersuche wird dadurch unnötig mühsam. Bei Bedarf:
      `opencode upgrade`.
- [ ] OpenCode **einmal gestartet** (beim ersten Start lädt OpenCode Daten
      nach — besser jetzt als am Workshop-Tag)
- [ ] `opencode.json` aus `opencode.json.example` erstellt:
      ```bash
      cp opencode.json.example opencode.json
      ```
      Base-URL und Modelle sind schon eingetragen, ihr müsst nichts anpassen.
      Der API-Key gehört ohnehin **nicht** in diese Datei, sondern in eine
      Umgebungsvariable — und den gibt es erst am Workshop-Tag.
- [ ] Konfiguration geprüft — geht ohne API-Key:
      ```bash
      opencode models
      ```
      In der Ausgabe muss eine Zeile `aihub/qwen-3.8-27b-sovereign` stehen.
      Dann ist die `opencode.json` korrekt und es fehlt wirklich nur noch
      der Key.
- [ ] Workshop-Repository entpackt bzw. geklont, im Terminal geöffnet
- [ ] Abhängigkeiten installiert:
      ```bash
      uv sync --extra dev
      # oder: pip install -e ".[dev]"
      ```
      läuft ohne Fehler durch. Das `--extra dev` bei `uv` bitte nicht
      weglassen — sonst fehlen `pytest` und `httpx2`, und der nächste Punkt
      schlägt fehl. Windows-Hinweis zur `pip`-Variante: Falls
      `.venv\Scripts\Activate.ps1` blockiert wird, einmalig
      `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` ausführen.
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
      (beim ersten Start ggf. den Windows-Firewall-Dialog bestätigen)

## Zusätzlich für Gruppe B (frei: den Agenten selbst erweitern)

- [ ] Mindestens eines der Starter-READMEs einmal gelesen —
      `.opencode/commands/`, `.opencode/skills/`, `.opencode/agents/`,
      `.opencode/plugins/` oder `mcp-starter/`
- [ ] Subagent wird erkannt:
      ```bash
      opencode agent list
      ```
      In der Ausgabe muss `reviewer (subagent)` stehen, neben den
      eingebauten Agenten `build`, `plan`, `explore` und `general`.
      Das geht ohne API-Key.
- [ ] `mcp-starter/`-Abhängigkeiten installiert:
      ```bash
      pip install -r mcp-starter/requirements.txt
      ```
      läuft ohne Fehler durch
- [ ] MCP-Server lässt sich lokal starten/testen:
      ```bash
      mcp dev mcp-starter/server_komplett.py
      ```
      Bewusst die Komplett-Version: `server_template.py` enthält noch
      offene TODOs und lässt sich erst starten, wenn ihr sie ausgefüllt
      habt. Der erste Aufruf lädt den MCP-Inspector über `npx` nach
      (mehrere hundert MB) — deshalb unbedingt vorab einmal ausführen.

## Erfolgskriterien

Ihr seid startklar, wenn:

- ✅ `pytest` zeigt `6 passed`
- ✅ Die App unter `http://127.0.0.1:8000/health` antwortet
- ✅ `opencode models` zeigt euer AIHub-Modell — dann ist alles bereit und
  es fehlt nur noch der echte Key
- ✅ (Gruppe B) `mcp dev` öffnet den MCP-Inspector im Browser

## Am Workshop-Tag

Ihr bekommt den API-Key zu Beginn. Dann fehlt nur noch:

```powershell
$env:AIHUB_API_KEY = "<key-aus-dem-workshop>"   # Windows PowerShell
```

```bash
export AIHUB_API_KEY="<key-aus-dem-workshop>"   # Linux/macOS
```

Wichtig: Die Variable gilt nur im aktuellen Terminal. Setzt sie in demselben
Terminal, aus dem ihr `opencode` startet — ein Auth-Fehler trotz korrektem
Key hat meist genau diese Ursache.

## Zwei Dinge, die euch begegnen können

**„team not allowed to access model"** — das ist kein Zugangsproblem. Wer
OpenCode schon vorher benutzt hat, bei dem gewinnt die alte globale
Konfiguration gegen die `opencode.json` im Projekt. Modell beim Aufruf
erzwingen: `opencode run -m aihub/<euer-modellname> "..."`.

**`Das Token "&&" ist kein gültiges Anweisungstrennzeichen`** — der Agent
versucht unter Windows gelegentlich `cd ... && pytest`, was PowerShell 5.1
nicht kennt. Kein Grund einzugreifen: Er merkt es selbst und wiederholt den
Befehl einzeln. Beobachtet lieber, *wie* er sich fängt.

Viel Erfolg beim Workshop!
