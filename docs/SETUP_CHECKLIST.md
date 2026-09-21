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

**Dienstliches/gesperrtes Gerät ohne Admin-Rechte?** Die Installationsbefehle
unten setzen voraus, dass ihr selbst Software installieren dürft. Ist das
nicht der Fall: internen Software-Katalog/Self-Service nutzen oder IT
kontaktieren, statt den Installer direkt herunterzuladen — und das frühzeitig,
nicht erst kurz vor dem Termin.

**Die Liste ist für alle gleich**, unabhängig von der Gruppe. Die Gruppenwahl
fällt erst vor Ort, und Pairing über Gruppengrenzen funktioniert nur, wenn
bei allen dasselbe läuft.

## Vor dem Termin

- [ ] Python 3.11 oder neuer installiert (`python --version`)
  - Windows: `winget install Python.Python.3.12`
  - macOS: meist schon vorhanden, sonst `brew install python3`
  - Linux: `sudo apt install python3` (oder das Äquivalent eurer Distribution)
- [ ] Git installiert (`git --version`)
  - Windows: `winget install Git.Git`
  - macOS: `brew install git`
  - Linux: `sudo apt install git`
- [ ] Node.js/npm installiert (`node --version`) — wird von OpenCode benötigt
  - Windows: `winget install OpenJS.NodeJS.LTS`
  - macOS: `brew install node`
  - Linux: [nodejs.org](https://nodejs.org/) (LTS-Version) für eine aktuelle
    Version, Distributions-Pakete sind oft veraltet
- [ ] OpenCode installiert, **mindestens Version 1.18**:
      ```bash
      opencode --version
      ```
      Installation, funktioniert auf allen Plattformen (Node ist ja schon da):
      ```bash
      npm install -g opencode-ai
      ```
  - Alternative macOS/Linux: `curl -fsSL https://opencode.ai/install | bash`
  - Alternative Windows: `choco install opencode` oder `scoop install opencode`

  Ältere Versionen (1.16.x) melden Verbindungsfehler nicht im Terminal — die
  Fehlersuche wird dadurch unnötig mühsam. Bei Bedarf: `opencode upgrade`.
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
- [ ] Abhängigkeiten installiert — **einer** der beiden Wege, nicht beide:

      **Variante A – mit `uv`:**
      ```bash
      uv sync --extra dev
      ```
      Das `--extra dev` nicht weglassen — sonst fehlen `pytest` und `httpx2`,
      und der nächste Punkt schlägt fehl. Bei diesem Weg bekommen alle
      weiteren Befehle ein `uv run` davor.

      **Variante B – mit `pip`:**
      ```powershell
      python -m venv .venv
      .venv\Scripts\Activate.ps1        # Windows PowerShell
      # source .venv/bin/activate       # Linux/macOS
      pip install -e ".[dev]"
      ```
      Falls `Activate.ps1` blockiert wird, einmalig
      `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` ausführen.

      Warum eine eigene Umgebung: Ohne sie landet alles im System-Python —
      und `pytest` findet dort womöglich ein fremdes, das grün meldet,
      obwohl im Projekt nichts installiert ist.
- [ ] Tests laufen durch:
      ```bash
      uv run pytest      # Variante A
      pytest             # Variante B, in der aktivierten Umgebung
      ```
      Erwartung: `6 passed`
- [ ] Anwendung startet:
      ```bash
      uv run uvicorn src.api:app --reload    # Variante A
      uvicorn src.api:app --reload           # Variante B
      ```
      `http://127.0.0.1:8000/health` antwortet mit `{"status": "ok"}`
      (beim ersten Start ggf. den Windows-Firewall-Dialog bestätigen)

- [ ] Subagent wird erkannt:
      ```bash
      opencode agent list
      ```
      In der Ausgabe muss `reviewer (subagent)` stehen, neben den
      eingebauten Agenten `build`, `plan`, `explore` und `general`.
      Das geht ohne API-Key.
- [ ] `mcp-starter/`-Abhängigkeiten installiert — in dieselbe Umgebung wie oben:
      ```bash
      uv pip install -r mcp-starter/requirements.txt    # Variante A
      pip install -r mcp-starter/requirements.txt       # Variante B, in der aktivierten Umgebung
      ```
      läuft ohne Fehler durch
- [ ] MCP-Server lässt sich lokal starten/testen:
      ```bash
      uv run mcp dev mcp-starter/server_komplett.py    # Variante A
      mcp dev mcp-starter/server_komplett.py           # Variante B
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
- ✅ `opencode agent list` zeigt `reviewer (subagent)`
- ✅ `mcp dev` öffnet den MCP-Inspector im Browser

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
