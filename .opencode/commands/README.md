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
description: <kurze Beschreibung, wofür der Befehl da ist>
agent: <Subagent mit passenden Rechten, optional>
---

<Prompt-Text als Markdown; $ARGUMENTS steht für alles hinter dem Befehl>
```

Der Dateiname (ohne `.md`) wird zum Befehlsnamen (`/<dateiname>`).

Mehr Felder gibt es nicht — `description`, `agent`, `model`, `subtask`. Ein
Feld `allowed-tools` kennt OpenCode **nicht**; es würde stillschweigend
ignoriert. **Rechte kommen vom Agenten:** `check-acceptance` läuft über
`agent: reviewer`, den Subagenten aus `.opencode/agents/`, dem das Ändern
von Dateien entzogen ist. Ohne `agent:` läuft ein Command mit allen Rechten
des Hauptagenten.

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

- Rechte über `agent:` eng halten — ein Prüfbefehl läuft über einen
  Subagenten, der nichts ändern darf. Ohne `agent:` hat der Command alle
  Rechte des Hauptagenten.
- Keine neuen Abhängigkeiten ohne Grund.
- Realistisch in der verbleibenden Zeit umsetzbar bleiben.

Custom Commands sind niedrigschwelliger als ein eigener MCP-Server (siehe
`mcp-starter/`) — guter Einstieg, bevor man sich an den MCP-Server wagt.
