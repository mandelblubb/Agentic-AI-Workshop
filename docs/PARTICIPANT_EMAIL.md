# E-Mail-Vorlage: Vorab-Info an Teilnehmende

Zum Kopieren in euer E-Mail-Programm. Anhang: das kuratierte Teilnehmenden-ZIP
(nicht der komplette Repository-Export — siehe Hinweis unten).

---

**Betreff:** Vorbereitung Workshop "Agentische Softwareentwicklung" — bitte vor dem Termin lesen

Hallo zusammen,

im Anhang findet ihr alle Unterlagen für den Workshop
"Agentische Softwareentwicklung" am [DATUM, UHRZEIT, ORT].

**Bitte vor dem Termin:**

1. Anhang entpacken.
2. `README.md` einmal durchlesen (Überblick, zwei Workshop-Gruppen).
3. `docs/SETUP_CHECKLIST.md` Schritt für Schritt durchgehen — Python, Git,
   Node.js, OpenCode, Beispieltests.
4. Bei Problemen: bitte **vorab** melden unter [Kontakt einfügen], nicht
   erst am Workshop-Tag. Falls etwas bis dahin nicht gelöst werden kann:
   trotzdem kommen, es gibt Pairing mit anderen Teilnehmenden.

Der Ablauf des Workshop-Tags selbst steht in `docs/AGENDA.md` — kurz
zusammengefasst: Es gibt zwei Gruppen (eine geführte mit vorgegebenen
Aufgaben, eine freie zum eigenständigen Erweitern des Coding Agenten), ihr
entscheidet euch dafür direkt vor Ort.

Ebenfalls im Anhang, aber ausdrücklich **keine Hausaufgabe**:
`docs/PROMPTS.md` (Prompts zum Kopieren) und `docs/GLOSSAR.md` (Begriffe) —
beides ist zum Nachschlagen während des Workshops gedacht.

**Zum Modellzugang:** Den API-Key für den firmeneigenen AIHub bekommt ihr
zu Beginn des Workshops — ihr müsst vorab nichts beantragen, und ein VPN ist
nicht nötig. Genau deshalb ist die Checkliste wichtig: Alles andere lässt
sich vorab erledigen, sodass am Workshop-Tag nur noch eine Umgebungsvariable
gesetzt werden muss.

Bei Fragen jederzeit melden.

Bis zum [DATUM]!

[Name/Team]

---

## Hinweis für die Workshop-Leitung

Dieser Anhang ist bewusst **nicht** der komplette Projektordner. Ausgenommen
sind drei Dateien, die Teile der Übung vorab verraten würden:

- `docs/TRAINER_GUIDE.md` — Fallback-Logik und Beobachtungspunkte
- `docs/SOLUTION_HINTS.md` — Lösungshinweise zu ISSUE-01 und ISSUE-03
- `docs/agenten-werkstatt.html` — das Beamer-Werkzeug; seine Module 1 und 5
  zeigen den Lösungsweg zu ISSUE-01 und die Pointe von ISSUE-02

Ein passendes ZIP lässt sich z. B. so bauen (PowerShell, aus dem
Projektordner heraus):

```powershell
$stage = "$env:TEMP\agentic-workshop-teilnehmer"
New-Item -ItemType Directory -Path $stage -Force | Out-Null
Copy-Item README.md, AGENTS.md, pyproject.toml, .gitignore, opencode.json.example $stage
Copy-Item src, tests, issues, mcp-starter, .opencode, templates $stage -Recurse
New-Item -ItemType Directory -Path "$stage\docs" -Force | Out-Null
Copy-Item docs\AGENDA.md, docs\SETUP_CHECKLIST.md, docs\CUSTOM_ISSUE_PROMPT.md,
          docs\PROMPTS.md, docs\GLOSSAR.md "$stage\docs"
Get-ChildItem $stage -Recurse -Filter "__pycache__" -Directory | Remove-Item -Recurse -Force
Get-ChildItem $stage -Recurse -Filter "*.egg-info" -Directory | Remove-Item -Recurse -Force
Get-ChildItem $stage -Recurse -Filter "node_modules" -Directory | Remove-Item -Recurse -Force
Remove-Item "$stage\.opencode\package.json", "$stage\.opencode\package-lock.json" -Force -ErrorAction SilentlyContinue
Compress-Archive -Path "$stage\*" -DestinationPath "agentic-workshop-teilnehmer.zip" -Force
```

**Vor dem Versand außerdem ausfüllen:** `[Kontakt einfügen]` in
`docs/SETUP_CHECKLIST.md` sowie alle `[...]`-Platzhalter oben in der E-Mail
(Datum, Uhrzeit, Ort, Kontakt).
