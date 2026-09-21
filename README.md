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

## Eure Aufgabe

**Gruppe A – App bauen.** Baut mit dem Coding Agenten die Planungs-App für
Fortbildungsveranstaltungen weiter — was genau, entscheidet ihr. Die Tickets
unter `issues/` sind ein Einstieg, kein Pflichtprogramm: ISSUE-01 ist ein
guter erster Schritt, und eigene Ideen macht `docs/CUSTOM_ISSUE_PROMPT.md`
zu einem Ticket. Ihr seid fertig, wenn die App mehr kann als am Anfang,
jede neue Funktion durch Tests abgesichert ist und ihr den `git diff`
selbst gelesen habt — nicht, wenn der Agent sagt, er sei fertig.

**Gruppe B – Werkzeuge bauen.** Baut eine eigene Erweiterung für den Agenten:
einen Command, einen Skill, einen Subagenten, ein Plugin oder ein
MCP-Werkzeug. Ihr seid fertig, wenn OpenCode die Erweiterung kennt und ihr
einmal gezeigt habt, dass sie wirkt. Eine, die läuft, zählt mehr als drei
halbfertige.

**Für beide:** Das Ergebnis ist nicht der Code. Es ist eure Antwort auf die
Frage, mit der der Workshop endet — wo bleibt menschliches Review notwendig?

## Zwei Gruppen

Der Workshop läuft in zwei parallelen Gruppen, je nach technischer Erfahrung:

- **Gruppe A – App bauen:** Die Planungs-App mit dem Coding Agenten
  weiterentwickeln. Die Tickets unter `issues/` sind ein Einstieg für alle,
  die einen wollen (siehe "Workshop-Ablauf" unten) — eigene Funktionen sind
  ebenso willkommen. Empfohlen für Teilnehmende mit weniger
  CLI-/Agenten-Erfahrung. Der Ticket-Weg dient außerdem als Fallback-Demo
  (per Beamer), falls Gruppe B bei einzelnen Gruppen nicht vorankommt.
- **Gruppe B – Werkzeuge bauen (frei):** Den Coding Agenten selbst erweitern. Es gibt fünf Wege,
  für jeden ein lauffähiges Startgerüst:

  | Weg | Startgerüst | Aufwand |
  |-----|-------------|---------|
  | Custom Command — ihr ruft `/name` auf | `.opencode/commands/` | gering |
  | Skill — der Agent lädt ihn selbst | `.opencode/skills/` | gering |
  | Subagent — zweiter Kopf mit eigenen Rechten | `.opencode/agents/` | mittel |
  | Plugin — reagiert auf Ereignisse, ohne das Modell | `.opencode/plugins/` | mittel |
  | MCP-Server — neue Werkzeuge für den Agenten | `mcp-starter/` | hoch |

  Empfohlen für technisch erfahrene Teilnehmende. Commands und Skills sind
  niedrigschwellig und eignen sich als Einstieg; der MCP-Server ist die
  anspruchsvollste Stufe.

  Leere Vorlagen für alle sechs Wege — zum Mitnehmen ins eigene Projekt —
  liegen unter `templates/`.

Bei individuellen technischen Problemen: Pairing mit einer/einem Teilnehmenden,
bei der/dem es läuft — unabhängig von der Gruppe.

**Vor dem Termin:** Setup anhand von `docs/SETUP_CHECKLIST.md` prüfen.
**Ablauf im Detail:** siehe `docs/AGENDA.md`.
**Während des Workshops:** Prompts zum Kopieren stehen in `docs/PROMPTS.md`,
Begriffe in `docs/GLOSSAR.md`.

## Voraussetzungen

- Python 3.11 oder neuer
- Git
- Terminal
- Coding Agent: OpenCode (Open Source, im Polizeikontext zugelassenes Werkzeug)
- Node.js/npm (wird von OpenCode benötigt)
- Zugang zum firmeneigenen AIHub (LLM-Zugang inkl. Budget wird gestellt) —
  der API-Key wird zu Beginn des Workshops verteilt, ihr müsst vorab nichts
  beantragen. Ein VPN ist nicht nötig.

## OpenCode mit dem AIHub verbinden

```bash
cp opencode.json.example opencode.json
```

Base-URL und Modelle sind schon eingetragen. Den
API-Key bekommt ihr zu Beginn des Workshops; er kommt **nicht** in die Datei,
sondern in eine Umgebungsvariable:

```bash
export AIHUB_API_KEY="euer-key"        # Linux/macOS
$env:AIHUB_API_KEY = "euer-key"        # Windows PowerShell
```

Die Variable gilt nur im aktuellen Terminal — setzt sie in demselben
Terminal, aus dem ihr `opencode` startet. Ein Auth-Fehler trotz korrektem Key
hat meist genau diese Ursache.

`opencode.json` ist in `.gitignore` eingetragen und wird nicht committet —
nur `opencode.json.example` (ohne echte Werte) ist Teil des Repos.

**Falls ihr OpenCode schon vorher benutzt habt:** Eine bereits vorhandene
globale Konfiguration gewinnt gegen die `opencode.json` im Projekt — OpenCode
nimmt dann weiter euer altes Modell. Der Fehler sieht aus wie ein
Zugangsproblem (`team not allowed to access model`), ist aber keines. Modell
in dem Fall beim Aufruf erzwingen:

```bash
opencode run -m aihub/qwen-3.8-27b-sovereign "..."
```

## Installation

### Variante A: mit `uv`

```bash
uv sync --extra dev
uv run pytest
```

Das `--extra dev` ist nötig: `uv sync` allein installiert nur die
Hauptabhängigkeiten, nicht `pytest` und `httpx2`. Ohne das Flag meldet
`uv sync` erfolgreich — und `uv run pytest` scheitert erst danach.

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
uv run uvicorn src.api:app --reload    # Variante A
uvicorn src.api:app --reload           # Variante B, in der aktivierten Umgebung
```

Danach:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

## Workshop-Ablauf

Zu Beginn erfolgt die Einteilung in Gruppe A oder Gruppe B (siehe "Zwei Gruppen").
Die folgenden Runden beschreiben den **Ticket-Weg für Gruppe A** — ein
Vorschlag, kein Muss. Wer lieber eine eigene Funktion baut, überspringt die
Runden und lässt sich die Idee mit `docs/CUSTOM_ISSUE_PROMPT.md` zu einem
Ticket ausformulieren. Für **Gruppe B** direkt mit einem der Starter-READMEs
beginnen: `.opencode/commands/README.md`,
`.opencode/skills/README.md`, `.opencode/agents/README.md`,
`.opencode/plugins/README.md` oder `mcp-starter/README.md`.

### Runde 1

Öffne:

```text
issues/ISSUE-01-registration.md
```

Gib dem Coding Agenten beispielsweise diesen Auftrag:

```text
Lies AGENTS.md und issues/ISSUE-01-registration.md.

Analysiere zuerst Architektur und bestehende Tests.
Erstelle einen kurzen Plan und ändere bis dahin keine Dateien.

Implementiere danach das Issue vollständig.
Ergänze sinnvolle Tests, führe alle Tests aus und behebe Fehler.
Prüfe abschließend git diff und alle Akzeptanzkriterien.
Nenne mögliche Restrisiken.
```

Weitere Prompt-Muster — Repository verstehen, zweiter Agent als Reviewer,
Test zuerst, Aufgabe kleiner schneiden — stehen in `docs/PROMPTS.md`.

Unter Windows kann dabei die Meldung `Das Token "&&" ist kein gültiges
Anweisungstrennzeichen` auftauchen — PowerShell 5.1 kennt `&&` nicht. Der
Agent bemerkt das selbst und wiederholt den Befehl. Lasst ihn machen und
schaut zu, wie er sich fängt; das ist einer der Momente, um die es hier geht.

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
