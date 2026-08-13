# Agentic Software Engineering Workshop

Hands-on-Workshop: **Vom Ticket zum getesteten Code mit einem Coding Agenten**

Dieses Repository ist für einen 60–120-minütigen Workshop zur agentischen
Softwareentwicklung vorbereitet. Es funktioniert vollständig lokal und benötigt
keinen GitLab-Server.

## Szenario

Wir entwickeln eine kleine API zur Verwaltung von Fortbildungsveranstaltungen.

Eine Veranstaltung besitzt:

- Titel
- Datum
- Ort
- maximale Teilnehmerzahl

Im Verlauf des Workshops wird die Anwendung schrittweise durch einen Coding Agenten erweitert.

## Zwei Spuren

Der Workshop läuft in zwei parallelen Spuren, je nach technischer Erfahrung:

- **Spur A – geführt:** Vorgegebene Tickets unter `issues/` schrittweise mit dem
  Coding Agenten umsetzen (siehe "Workshop-Ablauf" unten). Empfohlen für
  Teilnehmende mit weniger CLI-/Agenten-Erfahrung. Dient außerdem als
  Fallback-Demo (per Beamer), falls Spur B bei einzelnen Gruppen nicht
  vorankommt.
- **Spur B – frei:** Eigene OpenCode Custom Commands, Skills und einen
  eigenen MCP-Server für die Anwendung entwickeln, ausgehend von den
  Startgerüsten in `.opencode/commands/` (Custom Commands),
  `.opencode/skills/` (Skills) und `mcp-starter/` (MCP-Server). Empfohlen für
  technisch erfahrene Teilnehmende. Custom Commands und Skills sind
  niedrigschwelliger und eignen sich als Einstieg, bevor man sich an den
  MCP-Server wagt.

Bei individuellen technischen Problemen: Pairing mit einer/einem Teilnehmenden,
bei der/dem es läuft — unabhängig von der Spur.

**Vor dem Termin:** Setup anhand von `docs/SETUP_CHECKLIST.md` prüfen.
**Ablauf im Detail:** siehe `docs/AGENDA.md`.

## Voraussetzungen

- Python 3.11 oder neuer
- Git
- Terminal
- Coding Agent: OpenCode (Open Source, im Polizeikontext zugelassenes Werkzeug)
- VPN-Zugang zum internen Netz
- Zugriff auf den firmeneigenen AIHub (LLM-Zugang inkl. Budget wird gestellt)

## OpenCode mit dem AIHub verbinden

```bash
cp opencode.json.example opencode.json
```

In `opencode.json` `<AIHUB_BASE_URL>` und `<AIHUB_MODEL_NAME>` mit den
Werten aus der Setup-Anleitung eintragen. Den API-Key **nicht** direkt in
die Datei schreiben, sondern als Umgebungsvariable setzen:

```bash
export AIHUB_API_KEY="euer-key"        # Linux/macOS
$env:AIHUB_API_KEY = "euer-key"        # Windows PowerShell
```

`opencode.json` ist in `.gitignore` eingetragen und wird nicht committet —
nur `opencode.json.example` (ohne echte Werte) ist Teil des Repos.

## Installation

### Variante A: mit `uv`

```bash
uv sync
uv run pytest
```

### Variante B: mit `pip`

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Dann:

```bash
pip install -e ".[dev]"
pytest
```

## Anwendung starten

```bash
uvicorn src.api:app --reload
```

Danach:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

## Workshop-Ablauf

Zu Beginn erfolgt die Einteilung in Spur A oder Spur B (siehe "Zwei Spuren").
Die folgenden Runden beschreiben **Spur A**. Für **Spur B** direkt mit
`.opencode/commands/README.md` (Custom Commands), `.opencode/skills/README.md`
(Skills) und/oder `mcp-starter/README.md` (MCP-Server) starten.

### Runde 1

Öffne:

```text
issues/ISSUE-01-registration.md
```

Gib dem Coding Agenten beispielsweise diesen Auftrag:

```text
Lies AGENTS.md und issues/ISSUE-01-registration.md.

Analysiere zunächst das Repository und die bestehende Architektur.
Erstelle einen kurzen Implementierungsplan, bevor du Dateien änderst.

Implementiere anschließend das Issue vollständig.
Ergänze sinnvolle Tests, führe alle Tests aus und behebe auftretende Fehler.

Prüfe am Ende deine eigenen Änderungen gegen die Akzeptanzkriterien
und fasse Änderungen und verbleibende Risiken zusammen.
```

### Runde 2

Erst wenn die Workshop-Leitung dies freigibt:

```text
issues/ISSUE-02-security-review.md
```

### Runde 3 / Bonus

```text
issues/ISSUE-03-validation.md
```

## Nützliche Git-Befehle

```bash
git status
git diff
git log --oneline
```

Der Coding Agent darf Git verwenden, aber **nicht automatisch committen oder externe Repositories verändern**, sofern die Workshop-Leitung nichts anderes vorgibt.

## Ziel des Workshops

Nicht die API selbst ist das Lernziel.

Beobachtet vielmehr:

1. Wie analysiert der Agent ein bestehendes Repository?
2. Plant er vor der Implementierung?
3. Welche Dateien verändert er?
4. Schreibt er Tests?
5. Führt er Tests wirklich aus?
6. Erkennt und korrigiert er eigene Fehler?
7. Befolgt er die Regeln in `AGENTS.md`?
8. Wo ist menschliches Review weiterhin notwendig?
