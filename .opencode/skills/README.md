# Skill-Starter (Gruppe B)

Minimales Startgerüst für Teilnehmende, die in der freien Workshop-Gruppe einen
eigenen OpenCode Skill für die Convention App bauen wollen.

**Skills sind kein Command.** Ein Skill wird nicht per `/befehl` aufgerufen,
sondern vom Agenten **selbstständig geladen**, wenn eine Aufgabe zur
`description` des Skills passt. Skills sind Hintergrundwissen, keine
gespeicherten Prompts (dafür: `.opencode/commands/`, siehe dort).

`privacy-safe-error-messages/SKILL.md` ist ein **funktionierendes Beispiel**:
Es beschreibt die Regel aus ISSUE-02 (keine personenbezogenen Daten in
Fehlermeldungen/Logs), damit der Agent sie automatisch berücksichtigt, sobald
er an Fehlerbehandlung in dieser Codebasis arbeitet - ohne dass jemand
explizit danach fragen muss.

## Aufbau eines Skills

```text
.opencode/skills/<skill-name>/SKILL.md
```

```yaml
---
name: <skill-name>
description: <wann der Agent diesen Skill laden soll - möglichst konkret>
---

<Markdown-Anleitung: Regel, Beispiele, wie anzuwenden>
```

Die `description` ist entscheidend: Der Agent entscheidet allein anhand
dieses Textes, ob der Skill zur aktuellen Aufgabe passt. Zu vage formuliert,
wird der Skill nie geladen; zu eng formuliert, verpasst er relevante Fälle.

**Hinweis:** Das genaue Schema kann sich je OpenCode-Version leicht
unterscheiden - im Zweifel gegen die aktuelle OpenCode-Dokumentation prüfen.

## Eigene Skills ergänzen

Ideen zum Weiterbauen (nur Anregungen, keine Vorgabe):

- ein Skill, der beschreibt, wie Namen/Agencies für den Doppelanmeldungs-
  Check normalisiert werden sollen (`strip()` + `casefold()`, siehe
  `docs/SOLUTION_HINTS.md`)
- ein Skill, der die Architekturregel aus `AGENTS.md` zusammenfasst
  (`api.py`/`service.py`/`models.py`-Trennung), damit der Agent sie auch
  ohne expliziten Hinweis im Prompt berücksichtigt
- ein Skill, der beschreibt, wann ein neuer Endpoint einen Test in
  `tests/test_api.py` **und** `tests/test_service.py` braucht

**Praktischer Tipp:** Auch hier gilt wie beim Command-Starter: nicht
zwingend von Hand tippen. Der Beispiel-Skill als Vorlage geben und den
Coding Agenten bitten, daraus einen neuen Skill mit passender `description`
zu schreiben.

## Wie prüfen, ob der Skill wirklich greift?

Anders als bei Commands lässt sich ein Skill nicht direkt aufrufen. Am
einfachsten testen: eine Aufgabe formulieren, die klar in den
Beschreibungsbereich des Skills fällt (z. B. *"Ergänze eine Fehlermeldung für
den Fall X"*), und beobachten, ob der Agent das Skill-Wissen sichtbar
anwendet (z. B. bewusst neutral formuliert, statt personenbezogene Daten
einzubauen).

## Leitplanken

- Beschreibung so konkret wie möglich halten, damit der Skill zuverlässig
  (und nicht ständig unnötig) geladen wird.
- Kein Ersatz für Tests - ein Skill beeinflusst das Verhalten des Agenten,
  garantiert es aber nicht. Wichtige Regeln bleiben zusätzlich durch Tests
  abgesichert.
