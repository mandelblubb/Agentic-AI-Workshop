# Trainer Guide

## Ziel

Die Teilnehmenden sollen erleben, dass ein Coding Agent nicht nur Code generiert,
sondern ein Repository analysieren, planen, mehrere Dateien bearbeiten, Tests ausführen,
Fehler korrigieren und seine eigene Änderung reviewen kann.

## Zwei Spuren

Der Workshop läuft parallel in zwei Spuren, damit unterschiedliches technisches
Niveau nicht zum Problem wird:

- **Spur A – geführt.** Vorgegebene Tickets (`issues/ISSUE-01` → `ISSUE-02` →
  Bonus) mit dem Coding Agenten umsetzen. Für weniger CLI-/Agenten-erfahrene
  Teilnehmende. Läuft nach den unten stehenden Zeitplänen.
- **Spur B – frei.** Eigene OpenCode Custom Commands (`.opencode/commands/`),
  Skills (`.opencode/skills/`) und einen eigenen MCP-Server (`mcp-starter/`)
  für die Anwendung entwickeln. Für technisch erfahrene Teilnehmende, kein
  Ticket-Skript, offenes Ziel. Custom Commands und Skills sind
  niedrigschwelliger und eignen sich als Einstieg vor dem MCP-Server.

**Spureinteilung** erfolgt direkt nach der Einführung (kurze Selbsteinschätzung:
"Wer hat schon CLI-Agenten/MCP-Erfahrung?" → Spur B, alle anderen → Spur A).

**Spur A ist außerdem die Fallback-Demo.** Falls in Spur B eine Gruppe nicht
vorankommt oder generell etwas ausfällt, wird stattdessen Spur A per Beamer
präsentiert (der Live-Demo-Block ist dafür schon die Generalprobe). Bei
individuellen technischen Problemen einzelner Teilnehmender reicht Pairing mit
einer/einem Teilnehmenden, bei der/dem es läuft — unabhängig von der Spur.

**Personal:** Für den Parallelbetrieb braucht es zwei ansprechbare
Betreuer:innen gleichzeitig — eine:r für Setup-/Pairing-Fragen in Spur A,
eine:r für MCP-/Command-Fragen in Spur B.

## Empfohlene Dauer

Die folgenden Zeitpläne beschreiben **Spur A**. Spur B läuft im selben
Zeitrahmen, aber ohne festen Ablauf — siehe "Spur B: offener Rahmen" weiter
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

## Spur B: offener Rahmen

Kein Minutenplan, aber grobe Orientierung im selben Zeitfenster wie Spur A:

- Setup + Sichten von `.opencode/commands/README.md`, `.opencode/skills/README.md`
  und `mcp-starter/README.md` (~10-15 min)
- eigenen Custom Command oder Skill bauen (niedrigschwelliger Einstieg, ~15-20 min)
- eigenes MCP-Tool entwerfen und im Agenten-Gespräch verfeinern (~15-20 min)
- Umsetzung, Testen gegen die laufende App (~30-45 min)
- kurze Selbstdemo am Ende, parallel zur Abschlussdiskussion von Spur A

Leitplanke, die den Teilnehmenden mitgegeben werden sollte: lieber ein
Command/Skill/Tool, das wirklich läuft, als mehrere halbfertige. Bei
Zeitdruck: auf das Beispiel in `.opencode/commands/check-acceptance.md`,
`.opencode/skills/privacy-safe-error-messages/SKILL.md` bzw.
`mcp-starter/server_komplett.py` zurückfallen und nur eine kleine
Erweiterung ergänzen, statt neu anzufangen. Für den MCP-Server gibt es
zusätzlich `mcp-starter/server_template.py` als Fill-in-the-Blank-Einstieg
mit `# TODO`-Markierungen, bevor man zur Komplett-Version wechselt.

## Vor Beginn prüfen

```bash
pytest
```

Erwartung im Ausgangszustand:

```text
6 passed
```

Teilnehmenden-Checkliste vorab verschicken: `docs/SETUP_CHECKLIST.md`
(VPN, AIHub, OpenCode, `pytest`, für Spur B zusätzlich `mcp-starter/`) —
idealerweise vor dem Termin ausfüllen lassen, nicht erst live.

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

### Zusätzlich für Spur B

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

## Abschlussdiskussion für beide Spuren

Die Ergebnisse sind zwischen den Spuren nicht vergleichbar — die
Abschlussrunde sollte beide Perspektiven einsammeln, statt einen direkten
Vergleich zu erwarten:

- Spur A: "Was habt ihr umgesetzt? Wo hättet ihr dem Agenten nicht vertraut?"
- Spur B: "Was habt ihr gebaut? Wie hat euch der Agent beim Tool-Design
  geholfen oder im Weg gestanden?"

Guter gemeinsamer Abschluss unabhängig von der Spur: die Frage aus
`README.md`, Ziel-Punkt 8 — *"Wo ist menschliches Review weiterhin
notwendig?"*

## Infrastruktur

Keine Hackathon-Infrastruktur (kein GitLab-Server) nötig. Es reicht:

- VPN-Zugang ins interne Netz
- Zugang zum firmeneigenen AIHub (LLM-Zugang inkl. Budget wird von uns gestellt)
- OpenCode, gegen den AIHub konfiguriert
- lokales Git, Issues als Markdown-Dateien im Repo — kein zentraler
  Issue-Tracker nötig

Optionale Erweiterung, falls später gewünscht: Repo nach GitLab spiegeln und
Markdown-Issues in echte GitLab-Issues übertragen. Für den Kern-Workshop
(beide Spuren) nicht erforderlich; das Workshop-Repository selbst muss dafür
nicht verändert werden.
