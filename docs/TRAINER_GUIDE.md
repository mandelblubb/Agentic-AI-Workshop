# Trainer Guide

## Ziel

Die Teilnehmenden sollen erleben, dass ein Coding Agent nicht nur Code generiert,
sondern ein Repository analysieren, planen, mehrere Dateien bearbeiten, Tests ausführen,
Fehler korrigieren und seine eigene Änderung reviewen kann.

## Empfohlene Dauer

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

## Vor Beginn prüfen

```bash
pytest
```

Erwartung im Ausgangszustand:

```text
6 passed
```

## Empfohlener Prompt für ISSUE-01

```text
Lies AGENTS.md und issues/ISSUE-01-registration.md.

Analysiere zuerst Architektur und bestehende Tests.
Erstelle einen kurzen Plan und ändere bis dahin keine Dateien.

Implementiere danach das Issue vollständig.
Führe alle Tests aus und behebe Fehler.
Prüfe abschließend git diff und alle Akzeptanzkriterien.
Nenne mögliche Restrisiken.
```

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

## ISSUE-02 als Überraschung

Nach der ersten vermeintlich fertigen Implementierung:

> Es ist ein Ergebnis des Security-/Datenschutz-Reviews eingegangen.
> Öffnet jetzt ISSUE-02.

Wichtig: Wenn eine Lösung bereits datenschutzkonform ist, soll der Agent dies
begründen und durch Tests absichern. Ein Issue muss nicht zwingend eine
Codeänderung erzeugen.

## Optionaler zweiter Agent

```text
Du bist Reviewer, nicht Entwickler.

Lies AGENTS.md, ISSUE-01 und den aktuellen git diff.
Verändere zunächst keine Dateien.

Prüfe:
- Erfüllung der Akzeptanzkriterien
- Testabdeckung
- Architektur
- Datenschutz
- Randfälle

Liefere Findings nach Schweregrad.
```

## Infrastrukturvarianten

### Ohne zentrale Infrastruktur

- ZIP lokal verteilen
- Issues als Markdown-Dateien
- lokales Git
- Coding Agent mit LLM-Zugang

### Mit Hackathon-Infrastruktur

- Repo nach GitLab spiegeln
- Markdown-Issues optional in echte GitLab Issues übertragen
- OpenCode über LiteLLM anbinden
- optional Branch/Merge-Request/CI demonstrieren

Das Workshop-Repository selbst muss dafür nicht verändert werden.
