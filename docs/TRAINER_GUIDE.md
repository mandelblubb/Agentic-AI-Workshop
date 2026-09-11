# Trainer Guide

## Ziel

Die Teilnehmenden sollen erleben, dass ein Coding Agent nicht nur Code generiert,
sondern ein Repository analysieren, planen, mehrere Dateien bearbeiten, Tests ausführen,
Fehler korrigieren und seine eigene Änderung reviewen kann.

## Zwei Gruppen

Der Workshop läuft parallel in zwei Gruppen, damit unterschiedliches technisches
Niveau nicht zum Problem wird:

- **Gruppe A – App bauen (geführt).** Vorgegebene Tickets (`issues/ISSUE-01` → `ISSUE-02` →
  Bonus) mit dem Coding Agenten umsetzen. Für weniger CLI-/Agenten-erfahrene
  Teilnehmende. Läuft nach den unten stehenden Zeitplänen.
- **Gruppe B – Werkzeuge bauen (frei).** Eigene OpenCode Custom Commands (`.opencode/commands/`),
  Skills (`.opencode/skills/`) und einen eigenen MCP-Server (`mcp-starter/`)
  für die Anwendung entwickeln. Für technisch erfahrene Teilnehmende, kein
  Ticket-Skript, offenes Ziel. Custom Commands und Skills sind
  niedrigschwelliger und eignen sich als Einstieg vor dem MCP-Server.

**Gruppeneinteilung** erfolgt direkt nach der Einführung (kurze Selbsteinschätzung:
"Wer hat schon CLI-Agenten/MCP-Erfahrung?" → Gruppe B, alle anderen → Gruppe A).

**Gruppe A ist außerdem die Fallback-Demo.** Falls in Gruppe B eine Gruppe nicht
vorankommt oder generell etwas ausfällt, wird stattdessen Gruppe A per Beamer
präsentiert (der Live-Demo-Block ist dafür schon die Generalprobe). Bei
individuellen technischen Problemen einzelner Teilnehmender reicht Pairing mit
einer/einem Teilnehmenden, bei der/dem es läuft — unabhängig von der Gruppe.

**Personal:** Für den Parallelbetrieb braucht es zwei ansprechbare
Betreuer:innen gleichzeitig — eine:r für Setup-/Pairing-Fragen in Gruppe A,
eine:r für MCP-/Command-Fragen in Gruppe B.

## Empfohlene Dauer

Die folgenden Zeitpläne beschreiben **Gruppe A**. Gruppe B läuft im selben
Zeitrahmen, aber ohne festen Ablauf — siehe "Gruppe B: offener Rahmen" weiter
unten.

### 60 Minuten

- 0–10 min: Einführung
- 10–15 min: Repository und `AGENTS.md`
- 15–40 min: ISSUE-01
- 40–50 min: Review / `git diff`
- 50–60 min: Diskussion

### 90 Minuten – Empfehlung

- 0–10 min: Einführung agentische Softwareentwicklung
- 10–20 min: kurze Live-Demo
- 20–25 min: Repository erklären
- 25–55 min: ISSUE-01 bearbeiten
- 55–70 min: ISSUE-02 freigeben
- 70–80 min: Agenten-Review
- 80–90 min: Ergebnisse und Grenzen diskutieren

### 120 Minuten

Wie 90 Minuten, anschließend:

- ISSUE-03
- zweiter Agent als Reviewer/Test-Agent
- Vergleich der Agentenstrategien

## Gruppe B: offener Rahmen

Kein Minutenplan, aber grobe Orientierung im selben Zeitfenster wie Gruppe A:

- Setup + Sichten der Starter-READMEs unter `.opencode/` und `mcp-starter/`
  (~10-15 min)
- eigenen Custom Command oder Skill bauen (niedrigschwelliger Einstieg, ~15-20 min)
- eigenen Subagenten, ein Plugin oder ein MCP-Tool entwerfen und im
  Agenten-Gespräch verfeinern (~15-20 min)
- Umsetzung, Testen gegen die laufende App (~30-45 min)
- kurze Selbstdemo am Ende, parallel zur Abschlussdiskussion von Gruppe A

Leitplanke, die den Teilnehmenden mitgegeben werden sollte: lieber ein
Command/Skill/Tool, das wirklich läuft, als mehrere halbfertige. Bei
Zeitdruck auf eines der fertigen Beispiele zurückfallen und nur eine kleine
Erweiterung ergänzen, statt neu anzufangen:

| Weg | Beispiel | geprüft mit |
|-----|----------|-------------|
| Command | `.opencode/commands/check-acceptance.md` | Aufruf `/check-acceptance` |
| Skill | `.opencode/skills/privacy-safe-error-messages/SKILL.md` | im Referenzlauf selbst geladen |
| Subagent | `.opencode/agents/reviewer.md` | `opencode agent list` zeigt `reviewer (subagent)` |
| Plugin | `.opencode/plugins/edit-log.js` | schreibt nach einer Änderung nach `.opencode/edit-log.txt` |
| MCP | `mcp-starter/server_komplett.py` | `mcp dev` öffnet den Inspector |

Alle fünf sind auf diesem Stand gegen OpenCode 1.18.29 getestet worden.

**Hinweis zum Plugin:** Beim ersten Start mit einem Plugin legt OpenCode
`.opencode/node_modules/` an und lädt Abhängigkeiten nach. Das dauert einen
Moment und ist kein Fehler; das Verzeichnis ist bereits in
`.opencode/.gitignore` eingetragen. Für den MCP-Server gibt es
zusätzlich `mcp-starter/server_template.py` als Fill-in-the-Blank-Einstieg
mit `# TODO`-Markierungen, bevor man zur Komplett-Version wechselt.

## Agenten-Werkstatt am Beamer

`docs/agenten-werkstatt.html` ist ein interaktives Begleitwerkzeug für die
Präsentation: eine einzelne Datei, per Doppelklick im Browser zu öffnen, ohne
Internet.

**Bewusst nicht im Teilnehmenden-ZIP.** Modul 1 zeigt den Lösungsweg zu
ISSUE-01 einschließlich `strip()`/`casefold()`, Modul 1 Schritt 10 und Modul 5
nehmen die Pointe von ISSUE-02 vorweg. Wer das vorab sieht, braucht die Übung
nicht mehr — deshalb bleibt es in eurer Hand.

| Slot laut Agenda      | Was zeigen                                                                       |
|-----------------------|----------------------------------------------------------------------------------|
| 0–20 min Einführung   | Modul 1 (Die Schleife) und Modul 5 (Erst der Plan) — dieser Block hat sonst kein Material |
| 25–30 min Gruppenwahl    | Modul 3 (Drei Wege) — die Entscheidung Command/Skill/MCP fällt genau hier         |
| 90–120 min Abschluss  | Modul 4 (Was geht ans Modell) als Einstieg in die Datenschutzfrage                |

Modul 2 (Prompt-Labor) ist inhaltsgleich mit `docs/PROMPTS.md`, das die
Teilnehmenden ohnehin im Anhang haben — im Vortrag überspringbar.

Modul 1 lässt sich mit den Pfeiltasten durchsteppen. Wenn die Zeit knapp wird,
mindestens Schritt 7 (die Tests werden rot, der Agent merkt es selbst) und
Schritt 10 (alles grün, alle Kriterien erfüllt — und trotzdem stand ein
Klarname in der Fehlermeldung) zeigen. Diese beiden tragen die Kernaussagen.

## Gemessener Referenzlauf — bitte vorher lesen

ISSUE-01 wurde einmal vollständig mit OpenCode 1.18.29 durchgespielt
(unbeaufsichtigt, `--auto`, Modell `qwen-3.6-35b-sovereign` über den AIHub).
Ergebnis:

| | |
|---|---|
| Dauer | **51 Minuten** (3072 s) |
| Ergebnis | alle 12 Akzeptanzkriterien erfüllt, 6 → 29 Tests, alle grün |
| Umfang | 632 geänderte Zeilen in 6 Dateien |

**Die Dauer ist das Problem.** Die Agenda gibt Gruppe A für dieses Ticket 20
Minuten, der 90-Minuten-Plan 30. Mit einem langsamen Modell ist der Ablauf
nicht durchführbar — nicht annähernd.

Zwei Konsequenzen:

1. **Modell vorher testen und ein schnelles wählen.** Was der Account
   freigibt, verrät eine absichtlich falsche Modellangabe: Der Fehler listet
   alle erlaubten Modelle auf. Ein `opencode run -m aihub/<modell> "Antworte
   nur mit OK."` am Vortag kostet eine Minute und beantwortet die Frage.
2. **Abbruchkriterien setzen, statt zu hoffen.** Wenn nach 25 Minuten das
   erste Ticket nicht durch ist: ISSUE-02 streichen und direkt ins Review
   gehen. Der Erkenntniswert liegt im Zuschauen, nicht im fertigen Feature —
   ein halb fertiger Lauf, gemeinsam angesehen, trägt die Abschlussfrage
   genauso.

### Was der Referenzlauf sonst zeigte

Vorbildlich: erst gelesen und geplant, dann geschrieben — bis zum Plan kein
einziger schreibender Werkzeugaufruf. Bestehende Tests vor den eigenen
gelesen. `pytest` tatsächlich ausgeführt. Architektur eingehalten, Fachlogik
im Service, dünne Routen. Restrisiken selbst benannt.

Weniger vorbildlich, und damit gutes Diskussionsmaterial: Er hat zwei
GET-Endpoints ergänzt, die im Ticket nicht stehen (Beobachtungspunkt
„Erfindet er zusätzliche Anforderungen?"), normalisiert mit `lower()` statt
`casefold()`, und seine eigene Abschlussbilanz zählte falsch — „4 bestehende
Tests" statt 6.

## Vor Beginn prüfen

```bash
pytest
```

Erwartung im Ausgangszustand:

```text
6 passed
```

Teilnehmenden-Checkliste vorab verschicken: `docs/SETUP_CHECKLIST.md`
(Python, Git, Node, OpenCode, `pytest`, für Gruppe B zusätzlich
`mcp-starter/`) — idealerweise vor dem Termin ausfüllen lassen, nicht erst
live. Der AIHub-Key ist bewusst **nicht** Teil der Vorbereitung: Er wird zu
Beginn des Workshops verteilt.

## Empfohlener Prompt für ISSUE-01

Der Plan-first-Prompt steht in `docs/PROMPTS.md` (Muster 2) und wortgleich in
`README.md` unter "Runde 1" — Teilnehmende finden ihn also dort, wo sie
ohnehin nachschlagen. Verweist im Zweifel auf `docs/PROMPTS.md`, statt ihn
vorzulesen; dort stehen auch die übrigen Muster.

Entscheidend an diesem Prompt ist die Trennung von Planen und Ändern
("ändere bis dahin keine Dateien") — das ist zugleich der erste
Beobachtungspunkt unten.

## Beobachtungspunkte

- Hat der Agent `AGENTS.md` gelesen?
- Liest er vorhandene Tests?
- Trennt er API und Fachlogik?
- Schreibt er neue Tests?
- Führt er Tests wirklich aus?
- Normalisiert er Name/Agency sinnvoll?
- Verändert er unnötig viele Dateien?
- Erfindet er zusätzliche Anforderungen?
- Gibt er personenbezogene Daten in Fehlermeldungen aus?

### Zusätzlich für Gruppe B

- Entwirft der Agent ein sinnvolles, klar abgegrenztes Tool-/Command-Schema,
  statt zu breit/vage zu werden?
- Baut er auf den Startgerüsten auf, oder verliert er Zeit mit Dingen, die
  `.opencode/commands/check-acceptance.md` bzw. `mcp-starter/server_komplett.py`
  schon lösen würden?
- Testet er das neue Tool/Command wirklich gegen die laufende App, oder
  bleibt es ungetestet?
- Hält sich ein selbst gebauter Command an die `allowed-tools`-Leitplanke,
  oder räumt er sich mehr Rechte ein, als für die Aufgabe nötig?
- Bei selbst gebauten Skills: Formulieren die Teilnehmenden eine `description`,
  die tatsächlich trifft — und lädt der Agent den Skill danach erkennbar von
  selbst, ohne dass man explizit danach fragt?

## ISSUE-02 als Überraschung

Nach der ersten vermeintlich fertigen Implementierung:

> Es ist ein Ergebnis des Security-/Datenschutz-Reviews eingegangen.
> Öffnet jetzt ISSUE-02.

Wichtig: Wenn eine Lösung bereits datenschutzkonform ist, soll der Agent dies
begründen und durch Tests absichern. Ein Issue muss nicht zwingend eine
Codeänderung erzeugen.

**Rechnet damit, dass genau das eintritt — und zwar systematisch.** Der
Beispiel-Skill `.opencode/skills/privacy-safe-error-messages/` liegt im
Teilnehmenden-Paket, und der Agent lädt ihn von selbst, sobald er an
Fehlerbehandlung arbeitet. Im Referenzlauf stand im Protokoll
`Skill "privacy-safe-error-messages"`, die Fehlermeldung lautete von Anfang an
`"Registration already exists"`, und der Agent schrieb ungefragt einen Test
namens `test_registration_error_does_not_expose_personal_data`. ISSUE-02 war
gelöst, bevor es ausgegeben wurde.

Das ist kein Unfall, sondern die beste Demonstration, die der Workshop zu
bieten hat: Ein Skill, den niemand aufgerufen hat, hat ein Datenschutzproblem
verhindert, das erst eine Runde später zur Sprache kommen sollte. Nutzt es so
— nicht als Panne, sondern als Brücke zwischen den Gruppen:

> Warum musste hier niemand an den Datenschutz denken? Schaut ins Protokoll.
> Genau das baut Gruppe B gerade.

Anschließend bleibt ISSUE-02 trotzdem sinnvoll: Der Agent soll begründen,
*warum* das Finding nicht zutrifft, und es durch einen Test absichern. Falls
eine Gruppe die Überraschung erhalten will, den Skill vor der Runde aus
`.opencode/skills/` verschieben.

## Optionaler zweiter Agent

Der Reviewer-Prompt steht in `docs/PROMPTS.md` (Muster 3), ist also auch für
Teilnehmende sichtbar und muss nicht mehr diktiert werden.

Wichtig beim Einsatz: in einer **neuen** Session starten. Ein Agent, der
seinen eigenen Code prüft, findet erfahrungsgemäß weniger — und genau dieser
Unterschied ist der Lerneffekt des Blocks. Gut geeignet als Einstieg in die
Abschlussdiskussion: Was hat der zweite Agent gefunden, was hat *keiner* von
beiden gefunden?

## Abschlussdiskussion für beide Gruppen

Die Ergebnisse sind zwischen den Gruppen nicht vergleichbar — die
Abschlussrunde sollte beide Perspektiven einsammeln, statt einen direkten
Vergleich zu erwarten:

- Gruppe A: "Was habt ihr umgesetzt? Wo hättet ihr dem Agenten nicht vertraut?"
- Gruppe B: "Was habt ihr gebaut? Wie hat euch der Agent beim Tool-Design
  geholfen oder im Weg gestanden?"

Guter gemeinsamer Abschluss unabhängig von der Gruppe: die Frage aus
`README.md`, Ziel-Punkt 8 — *"Wo ist menschliches Review weiterhin
notwendig?"*

## Infrastruktur

Keine Hackathon-Infrastruktur (kein GitLab-Server) nötig. Es reicht:

- Zugang zum firmeneigenen AIHub (LLM-Zugang inkl. Budget wird von uns
  gestellt) — kein VPN nötig
- OpenCode, gegen den AIHub konfiguriert
- lokales Git, Issues als Markdown-Dateien im Repo — kein zentraler
  Issue-Tracker nötig

### API-Keys am Workshop-Tag verteilen

Die Teilnehmenden bekommen den AIHub-Key erst vor Ort. Damit der
Technik-Check nicht zum Engpass wird:

- **Kopierbar verteilen** (Chat, Handout-Datei, QR-Code) — nicht diktieren
  und nicht als Screenshot. Ein Tippfehler in einem langen Key kostet den
  gesamten Slot.
- **Früh verteilen**, idealerweise beim Ankommen, damit die Verbindung
  während der Einführung im Hintergrund aufgebaut werden kann.
- **Häufigster Fehler:** `$env:AIHUB_API_KEY` gilt nur im aktuellen
  Terminal. Wer OpenCode aus einem anderen Fenster oder aus der IDE startet,
  sieht einen Auth-Fehler und sucht an der falschen Stelle. Den Setz-Befehl
  am besten auf eine Folie legen, mit dem Hinweis: im selben Terminal, aus
  dem `opencode` gestartet wird.
- **Kein npm-Engpass:** `@ai-sdk/openai-compatible` ist im OpenCode-Binary
  enthalten und wird trotz des `npm`-Eintrags in der Config *nicht*
  nachgeladen — geprüft mit frischen Profilen unter OpenCode 1.16.2 und
  1.18.25. Der erste Start legt nur das Plugin-Verzeichnis unter
  `~/.config/opencode/node_modules` an; deshalb steht "einmal starten" in
  der Checkliste.
- **Mindestversion 1.18 durchsetzen.** Unter 1.16.2 gibt `opencode run` bei
  falschem Key oder unerreichbarer URL *keine* Fehlermeldung im Terminal aus
  und endet mit Exit-Code 0 — es sieht aus, als passiere einfach nichts; die
  Meldung steht nur im Log unter `~/.local/share/opencode/log/`. Ab 1.18.25
  erscheint sie im Terminal (`Error: Cannot connect to API: ...`, Exit-Code
  1). Wer am Workshop-Tag mit einer alten Version auftaucht, kostet euch
  sonst unnötig Support-Zeit.
- **Support-Reflex:** Wenn doch nichts sichtbar ist, zuerst ins Log unter
  `~/.local/share/opencode/log/` schauen — dort steht die echte Meldung
  (z. B. `AI_APICallError` / `FailedToOpenSocket`).

Optionale Erweiterung, falls später gewünscht: Repo nach GitLab spiegeln und
Markdown-Issues in echte GitLab-Issues übertragen. Für den Kern-Workshop
(beide Gruppen) nicht erforderlich; das Workshop-Repository selbst muss dafür
nicht verändert werden.
