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
2. `README.md` einmal durchlesen (Überblick, zwei Workshop-Spuren).
3. `docs/SETUP_CHECKLIST.md` Schritt für Schritt durchgehen — Python, Git,
   OpenCode, VPN, AIHub-Zugang, Beispieltests.
4. Bei Problemen: bitte **vorab** melden unter [Kontakt einfügen], nicht
   erst am Workshop-Tag. Falls etwas bis dahin nicht gelöst werden kann:
   trotzdem kommen, es gibt Pairing mit anderen Teilnehmenden.

Der Ablauf des Workshop-Tags selbst steht in `docs/AGENDA.md` — kurz
zusammengefasst: Es gibt zwei Spuren (eine geführte mit vorgegebenen
Aufgaben, eine freie zum eigenständigen Erweitern des Coding Agenten), ihr
entscheidet euch dafür direkt vor Ort.

**Voraussetzungen, die ihr vorab braucht:**
- VPN-Zugang zum internen Netz (falls noch nicht vorhanden: [Hinweis, wie
  man ihn beantragt])
- Zugriff auf den firmeneigenen AIHub ([Hinweis, wie man ihn beantragt])

Bei Fragen jederzeit melden.

Bis zum [DATUM]!

[Name/Team]

---

## Hinweis für die Workshop-Leitung

Dieser Anhang ist bewusst **nicht** der komplette Projektordner. Ausgenommen
sind `docs/TRAINER_GUIDE.md` und `docs/SOLUTION_HINTS.md` (Fallback-Logik,
Lösungshinweise, Beobachtungspunkte) sowie `CLAUDE.md`/`.claude/`
(Repo-Wartungsdokumentation) — diese Dateien sind nicht für Teilnehmende
gedacht und würden Teile der Übung vorab verraten.

Ein passendes ZIP lässt sich z. B. so bauen (PowerShell, aus dem
Projektordner heraus):

```powershell
$stage = "$env:TEMP\agentic-workshop-teilnehmer"
New-Item -ItemType Directory -Path $stage -Force | Out-Null
Copy-Item README.md, AGENTS.md, pyproject.toml, .gitignore, opencode.json.example $stage
Copy-Item src, tests, issues, mcp-starter, .opencode $stage -Recurse
New-Item -ItemType Directory -Path "$stage\docs" -Force | Out-Null
Copy-Item docs\AGENDA.md, docs\SETUP_CHECKLIST.md, docs\CUSTOM_ISSUE_PROMPT.md "$stage\docs"
Get-ChildItem $stage -Recurse -Filter "__pycache__" -Directory | Remove-Item -Recurse -Force
Compress-Archive -Path "$stage\*" -DestinationPath "agentic-workshop-teilnehmer.zip" -Force
```

**Vor dem Versand außerdem ausfüllen:** `[Kontakt einfügen]` in
`docs/SETUP_CHECKLIST.md` sowie alle `[...]`-Platzhalter oben in der E-Mail
(Datum, Ort, Kontakt, VPN/AIHub-Beantragung).
