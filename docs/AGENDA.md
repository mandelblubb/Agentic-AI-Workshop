# Workshop-Agenda: Agentische Softwareentwicklung

Willkommen zum Workshop! Ihr arbeitet mit einem Coding Agenten (OpenCode) an
einer kleinen Anwendung zur Verwaltung von Veranstaltungen — Ziel ist nicht
die Anwendung selbst, sondern zu erleben, wie ein Coding Agent ein Projekt
analysiert, plant, Code schreibt, testet und sich selbst korrigiert.

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

## Vorab

Bitte vor dem Termin einmal durchgehen: **`docs/SETUP_CHECKLIST.md`**
(Python, Git, Node, OpenCode, Tests). Den AIHub-Key bekommt ihr zu Beginn des
Workshops — vorab müsst ihr dafür nichts beantragen, und ein VPN ist nicht
nötig. Bei Problemen: vorab melden — bei technischen Problemen am Tag selbst
gibt es Pairing, das ist kein Grund zur Sorge.

## Zwei Gruppen

Nach der Einführung entscheidet ihr euch für eine Gruppe:

- **Gruppe A – App bauen.** Die Planungs-App mit dem Coding Agenten
  weiterentwickeln — entlang der vorbereiteten Tickets oder mit eigenen
  Ideen. Gut geeignet, wenn ihr mit CLI-Agenten/Coding Agenten noch wenig
  Erfahrung habt.
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
| 30–50 min  | **Gruppe A:** erste Funktion (z. B. ISSUE-01) · **Gruppe B:** Setup + erste eigene Erweiterung  |
| 50–65 min  | **Gruppe A:** weiterbauen — auf dem Ticket-Weg wird jetzt ISSUE-02 freigegeben · **Gruppe B:** weiterbauen |
| 65–75 min  | **Gruppe A:** Agenten-Review · **Gruppe B:** weiterbauen/testen                                 |
| 75–90 min  | **Gruppe A:** nächste Funktion, eigene Idee als Ticket · **Gruppe B:** weiterbauen/testen       |
| 90–120 min | Ergebnispräsentation & offene Fragen                                                        |

## Am Ende nehmt ihr mit

- ein konkretes Gefühl dafür, was ein Coding Agent eigenständig leisten kann
  — und wo nicht
- (Gruppe A) eine Planungs-App, die mehr kann als am Anfang — inklusive
  Tests, selbst reviewt
- (Gruppe B) einen eigenen Command, Skill oder MCP-Server, der wirklich läuft
- eine Antwort auf die Frage, die den Workshop abschließt: *Wo bleibt
  menschliches Review trotzdem notwendig?*
- `docs/PROMPTS.md` als Prompt-Sammlung, die auch in euren eigenen Projekten
  funktioniert
- `templates/` mit leeren Vorlagen für `AGENTS.md`, Commands, Skills,
  Subagents, Plugins und die `opencode.json` — für euer nächstes Projekt

Viel Erfolg und Spaß beim Ausprobieren!
