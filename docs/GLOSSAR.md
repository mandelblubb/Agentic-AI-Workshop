# Glossar

Die Begriffe, die im Workshop fallen — kurz erklärt. Gedacht zum Nachschlagen
zwischendurch; ihr müsst das nicht vorab lernen.

Passend dazu: `docs/PROMPTS.md` — Prompts zum Kopieren.

## Grundbegriffe

| Begriff | Was es ist | Warum es im Workshop vorkommt |
|---|---|---|
| **Coding Agent** | Ein Modell, das selbst Dateien liest und schreibt, Befehle ausführt und aus dem Ergebnis weiterarbeitet — in einer Schleife, bis die Aufgabe erledigt ist. | Genau dieser Unterschied ist das Thema: Ein Chat schlägt Code vor, ein Agent ändert euer Repository. |
| **Prompt** | Der Auftrag, den ihr dem Agenten gebt. | Wie genau ihr formuliert, entscheidet über das Ergebnis — deshalb die Prompt-Bibliothek. |
| **Kontext (Kontextfenster)** | Alles, was das Modell gerade sieht: euer Auftrag, gelesene Dateien, Befehlsausgaben, der bisherige Verlauf. Das Fenster ist begrenzt. | Erklärt zwei Beobachtungen: Der Agent kennt nur, was er gelesen hat — und sehr lange Sitzungen werden schlechter, weil Wichtiges hinten herausfällt. |
| **Token** | Die Abrechnungseinheit für Modelle, grob ein Wortteil. Jede gelesene Datei kostet Token. | Der AIHub-Zugang hat ein Budget. Wer den Agenten das halbe Repo lesen lässt, merkt das. |
| **Session** | Ein zusammenhängender Arbeitsverlauf mit dem Agenten. | Wenn er sich festfährt, ist eine neue Session oft schneller als weiterdiskutieren — sie startet mit leerem Kontext. |
| **Tool-Call** | Ein Werkzeugaufruf des Agenten: Datei lesen, Datei schreiben, `pytest` starten, `git diff` anzeigen. | Hier tut der Agent tatsächlich etwas. Beim Zuschauen lohnt die Frage: Warum ruft er *das* jetzt auf? |

## Erweiterungen des Agenten

| Begriff | Was es ist | Warum es im Workshop vorkommt |
|---|---|---|
| **`AGENTS.md`** | Datei im Repository mit verbindlichen Regeln für den Agenten — Architektur, Testpflicht, Datenschutz, Git. Er liest sie zu Beginn. | Die zentrale Beobachtungsfrage in Gruppe A: Hält er sich wirklich daran? |
| **Custom Command** | Ein gespeicherter Prompt, den *ihr* mit `/name` aufruft. Liegt unter `.opencode/commands/`. | Gruppe B, niedrigschwelliger Einstieg. Beispiel im Repo: `/check-acceptance`. |
| **Skill** | Hintergrundwissen, das der *Agent selbst* lädt, sobald die `description` zur Aufgabe passt. Liegt unter `.opencode/skills/`. | Der verwechselbare Zwilling zum Command: nicht aufgerufen, sondern erkannt. |
| **MCP-Server** | Ein eigenes Programm, das dem Agenten neue Werkzeuge bereitstellt (Model Context Protocol) — z. B. Zugriff auf die laufende Workshop-API. | Gruppe B, die anspruchsvollste Ausbaustufe. Startgerüst: `mcp-starter/`. |

## Werkzeuge im Workshop

| Begriff | Was es ist | Warum es im Workshop vorkommt |
|---|---|---|
| **OpenCode** | Der Coding Agent, mit dem wir arbeiten — Open Source, im Polizeikontext zugelassen. | Läuft im Terminal; mindestens Version 1.18 (ältere melden Verbindungsfehler nicht). |
| **AIHub** | Der firmeneigene LLM-Zugang, gegen den OpenCode konfiguriert wird. | Kein VPN nötig; den API-Key bekommt ihr zu Beginn des Workshops. |
| **`git diff`** | Zeigt alle Änderungen seit dem letzten Commit. | Euer wichtigstes Review-Werkzeug: Was hat der Agent *tatsächlich* angefasst? |
