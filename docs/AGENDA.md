# Workshop-Agenda: Agentische Softwareentwicklung

Willkommen zum Workshop! Ihr arbeitet mit einem Coding Agenten (OpenCode) an
einer kleinen Anwendung zur Verwaltung von Veranstaltungen — Ziel ist nicht
die Anwendung selbst, sondern zu erleben, wie ein Coding Agent ein Projekt
analysiert, plant, Code schreibt, testet und sich selbst korrigiert.

## Vorab

Bitte vor dem Termin einmal durchgehen: **`docs/SETUP_CHECKLIST.md`**
(Python, Git, Node, OpenCode, Tests). Den AIHub-Key bekommt ihr zu Beginn des
Workshops — vorab müsst ihr dafür nichts beantragen, und ein VPN ist nicht
nötig. Bei Problemen: vorab melden — bei technischen Problemen am Tag selbst
gibt es Pairing, das ist kein Grund zur Sorge.

## Zwei Gruppen

Nach der Einführung entscheidet ihr euch für eine Gruppe:

- **Gruppe A – App bauen (geführt).** Vorgegebene Tickets Schritt für Schritt mit dem
  Coding Agenten umsetzen. Gut geeignet, wenn ihr mit CLI-Agenten/Coding
  Agenten noch wenig Erfahrung habt.
- **Gruppe B – Werkzeuge bauen (frei).** Eigene Erweiterungen für den Coding Agenten selbst
  bauen — Custom Command, Skill, Subagent, Plugin oder MCP-Server. Für jeden
  dieser fünf Wege liegt ein lauffähiges Startgerüst bereit. Gut geeignet,
  wenn ihr technisch erfahren seid und offener explorieren wollt.

Es gibt kein falsches Ergebnis — beide Gruppen laufen auf dasselbe Lernziel
zu, nur mit unterschiedlichem Startpunkt.

## Während des Workshops

Zwei Dateien sind zum Nachschlagen gedacht, nicht zum Vorablesen:
`docs/PROMPTS.md` (Prompts zum Kopieren, jeweils mit Hinweis worauf man beim
Agenten achten sollte) und `docs/GLOSSAR.md` (die Begriffe, die fallen).

## Ablauf (120 Minuten)

| Zeit       | Programmpunkt                                                                               |
|------------|---------------------------------------------------------------------------------------------|
| vor Start  | Ankommen                                                                                    |
| 0–20 min   | Einführung: Agentische Softwareentwicklung                                                  |
| 20–25 min  | kurzer Technik-Check                                                                        |
| 25–30 min  | Repository kennenlernen, Gruppenwahl                                                           |
| 30–50 min  | **Gruppe A:** erstes Ticket · **Gruppe B:** Setup + erste eigene Erweiterung                    |
| 50–65 min  | **Gruppe A:** zweites Ticket (wird zu diesem Zeitpunkt freigegeben) · **Gruppe B:** weiterbauen |
| 65–75 min  | **Gruppe A:** Agenten-Review · **Gruppe B:** weiterbauen/testen                                 |
| 75–90 min  | **Gruppe A:** Eigene Issues erzeugen und umsetzen · **Gruppe B:** weiterbauen/testen            |
| 90–120 min | Ergebnispräsentation & offene Fragen                                                        |

## Am Ende nehmt ihr mit

- ein konkretes Gefühl dafür, was ein Coding Agent eigenständig leisten kann
  — und wo nicht
- (Gruppe A) ein umgesetztes Feature inklusive Tests, selbst reviewt
- (Gruppe B) einen eigenen Command, Skill oder MCP-Server, der wirklich läuft
- eine Antwort auf die Frage, die den Workshop abschließt: *Wo bleibt
  menschliches Review trotzdem notwendig?*
- `docs/PROMPTS.md` als Prompt-Sammlung, die auch in euren eigenen Projekten
  funktioniert
- `templates/` mit leeren Vorlagen für `AGENTS.md`, Commands, Skills,
  Subagents, Plugins und die `opencode.json` — für euer nächstes Projekt

Viel Erfolg und Spaß beim Ausprobieren!
