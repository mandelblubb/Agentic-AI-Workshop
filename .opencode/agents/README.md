# Subagent-Starter (Gruppe B)

Minimales Startgerüst für Teilnehmende, die in der freien Workshop-Gruppe einen
eigenen Subagenten für die Convention App bauen wollen.

**Ein Subagent ist ein eigener Agent mit eigenem Auftrag und eigenen Rechten.**
Der Hauptagent kann ihn beauftragen, oder ihr ruft ihn selbst mit `@name` auf.
Das ist der Unterschied zu den anderen Erweiterungen: Ein Command ist ein
gespeicherter Prompt, ein Skill ist Hintergrundwissen — ein Subagent ist ein
zweiter Kopf, der unabhängig arbeitet und dem ihr weniger erlauben könnt als
euch selbst.

`reviewer.md` ist ein **funktionierendes Beispiel**: ein Reviewer, der den
aktuellen Stand gegen die Akzeptanzkriterien prüft und dem das Bearbeiten von
Dateien entzogen ist. Aufruf in OpenCode:

```text
@reviewer Prüf den aktuellen Stand gegen issues/ISSUE-01-registration.md.
```

Prüfen, ob OpenCode ihn kennt:

```bash
opencode agent list
```

In der Ausgabe muss `reviewer (subagent)` stehen — neben den eingebauten
Agenten `build`, `plan`, `explore` und `general`.

## Aufbau eines Subagenten

```text
.opencode/agents/<name>.md
```

```yaml
---
description: <wofür der Agent da ist - danach entscheidet der Hauptagent,
              ob er ihn beauftragt>
mode: subagent
permission:
  edit: deny
---

<Systemprompt als Markdown: Rolle, Ablauf, gewünschte Ausgabe>
```

Der Dateiname ohne `.md` wird zum Agentennamen. Weitere Frontmatter-Felder:
`model` (anderes Modell als der Hauptagent), `temperature`, `hidden`, `color`.

**Die interessanteste Zeile ist `permission`.** Ein Reviewer, der nichts
ändern darf, kann auch nichts kaputtmachen — und muss seine Findings
formulieren, statt sie stillschweigend einzubauen. Das ist keine
Höflichkeitsregel, sondern eine Leitplanke, die der Agent nicht umgehen kann.

## Eigene Subagenten ergänzen

Ideen zum Weiterbauen (nur Anregungen, keine Vorgabe):

- ein Test-Agent, der ausschließlich Tests schreiben darf und keinen
  Produktivcode anfassen kann
- ein Datenschutz-Agent, der jede Fehlermeldung im Diff auf personenbezogene
  Daten prüft
- ein Architektur-Agent, der nur die Regeln aus `AGENTS.md` gegenprüft

**Praktischer Tipp:** Wie bei den anderen Startern gilt — `reviewer.md` als
Vorlage geben und den Coding Agenten bitten, daraus einen neuen Subagenten mit
passender `description` und passenden `permission`-Regeln zu schreiben.

## Leitplanken

- `permission` bewusst eng setzen. Ein Agent, der alles darf, ist kein
  eigener Agent, sondern nur ein längerer Prompt.
- Die `description` entscheidet, ob der Hauptagent ihn von selbst beauftragt —
  so konkret wie möglich formulieren.
- Kein Ersatz für Tests. Ein Reviewer findet, was er sucht; ein Test findet,
  was ihr festgelegt habt.
