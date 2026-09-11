# Command-Starter (Gruppe B)

Minimales Startgerüst für Teilnehmende, die in der freien Workshop-Gruppe einen
eigenen OpenCode Custom Command für die Convention App bauen wollen.

Custom Commands sind explizit per `/befehlsname` aufrufbare, gespeicherte
Prompts — zu unterscheiden von OpenCode Skills (`.opencode/skills/`), die der
Agent selbstständig lädt, wenn eine Aufgabe zur Skill-Beschreibung passt.

`check-acceptance.md` ist ein **funktionierendes Beispiel**: Es prüft die
aktuelle Implementierung gegen die Akzeptanzkriterien eines Issues, ohne
Dateien zu ändern. Aufruf in OpenCode:

```text
/check-acceptance issues/ISSUE-01-registration.md
```

## Aufbau eines Custom Commands

Jede Datei in diesem Ordner ist ein eigener Befehl, den OpenCode automatisch
erkennt — keine zusätzliche Konfiguration nötig. Aufbau:

```yaml
---
name: <befehlsname>
description: <kurze Beschreibung, wofür der Befehl da ist>
argument-hint: "<was als Argument erwartet wird>"
allowed-tools: <Liste erlaubter Werkzeuge, z. B. Read Grep Bash(pytest *)>
---

<Prompt-Text als Markdown, der beim Aufruf ausgeführt wird>
```

Der Dateiname (ohne `.md`) wird zum Befehlsnamen (`/<dateiname>`).

**Hinweis:** Das genaue Frontmatter-Schema kann sich je OpenCode-Version
leicht unterscheiden — im Zweifel gegen die aktuelle OpenCode-Dokumentation
prüfen.

## Eigene Commands ergänzen

Ideen zum Weiterbauen (nur Anregungen, keine Vorgabe):

- ein Command, der ein neues Feature-Issue aus einer kurzen Idee generiert
  (siehe `docs/CUSTOM_ISSUE_PROMPT.md` als Vorlage für den Prompt-Text)
- ein Command, der vor jedem Commit automatisch `pytest` und einen kurzen
  Architektur-Check gegen `AGENTS.md` durchführt
- ein Command, der eine kurze Zusammenfassung offener
  Registrierungen/Kapazitäten erzeugt

**Praktischer Tipp:** Den Command nicht zwingend von Hand tippen — die
Beispieldatei als Vorlage geben und den Coding Agenten bitten, daraus einen
neuen Command mit passendem Frontmatter zu schreiben. Das ist näher am
eigentlichen Workshop-Gedanken als reines Copy-Paste.

## Leitplanken

- `allowed-tools` bewusst eng halten — nur, was der Command wirklich braucht.
- Keine neuen Abhängigkeiten ohne Grund.
- Realistisch in der verbleibenden Zeit umsetzbar bleiben.

Custom Commands sind niedrigschwelliger als ein eigener MCP-Server (siehe
`mcp-starter/`) — guter Einstieg, bevor man sich an den MCP-Server wagt.
