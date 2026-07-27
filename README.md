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

## Voraussetzungen

- Python 3.11 oder neuer
- Git
- Terminal
- Coding Agent, z. B. OpenCode, Claude Code, Codex oder vergleichbares Werkzeug
- Zugriff auf ein geeignetes LLM

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
