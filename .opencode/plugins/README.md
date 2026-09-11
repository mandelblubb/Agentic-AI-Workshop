# Plugin-Starter (Gruppe B)

Minimales Startgerüst für Teilnehmende, die in der freien Workshop-Gruppe den
Coding Agenten selbst um Verhalten erweitern wollen.

**Was anderswo „Hook" heißt, heißt in OpenCode Plugin.** Es gibt keinen
Konfigurationsschlüssel `hooks` — ein Plugin ist eine JavaScript-Datei, die
sich auf Ereignisse des Agenten hängt. Die Hook-Namen sind dann die
Ereignisse *innerhalb* des Plugins.

Das ist die einzige der fünf Erweiterungen, die **nicht** über den Prompt
läuft: Command, Skill und Subagent beeinflussen, was das Modell denkt. Ein
Plugin läuft als Code, unabhängig davon, was das Modell vorhat.

`edit-log.js` ist ein **funktionierendes Beispiel**: Es hängt sich auf
`file.edited` und schreibt jede Dateiänderung mit Zeitstempel nach
`.opencode/edit-log.txt` — Nachvollziehbarkeit, wer wann was angefasst hat.

Ausprobieren: OpenCode starten, den Agenten irgendeine Datei ändern lassen,
danach

```bash
cat .opencode/edit-log.txt
```

Erwartete Ausgabe, eine Zeile je Änderung:

```text
2026-09-07T10:01:06.485Z  C:\...\README.md
```

**Beim ersten Start mit einem Plugin legt OpenCode `.opencode/node_modules/`
an** und lädt Abhängigkeiten nach. Das ist normal und dauert einen Moment;
`node_modules` ist bereits in `.opencode/.gitignore` eingetragen.

## Aufbau eines Plugins

```text
.opencode/plugins/<name>.js
```

```javascript
export const MeinPlugin = async ({ directory, project, client, $ }) => {
  return {
    event: async ({ event }) => {
      if (event.type !== "file.edited") return
      // hier passiert etwas
    },
  }
}
```

Nützliche Ereignisse:

| Ereignis | Wann |
|---|---|
| `tool.execute.before` | bevor ein Werkzeug läuft |
| `tool.execute.after` | danach |
| `file.edited` | eine Datei wurde geändert |
| `session.created` | neue Sitzung |
| `session.idle` | der Agent ist fertig |
| `permission.asked` | der Agent fragt um Erlaubnis |

**Welche Daten ein Ereignis mitbringt, müsst ihr nicht raten.** Nach dem
ersten Start steht es typisiert in

```text
.opencode/node_modules/@opencode-ai/sdk/dist/gen/types.gen.d.ts
```

Für `file.edited` ist es `{ file: string }` — deshalb steht im Beispiel
`event.properties.file`.

## Eigene Plugins ergänzen

Ideen zum Weiterbauen (nur Anregungen, keine Vorgabe):

- auf `session.idle` automatisch `pytest` starten und das Ergebnis melden
- auf `tool.execute.before` mitschreiben, welche Werkzeuge der Agent
  überhaupt benutzt — die ehrlichste Antwort auf „was tut er eigentlich?"
- auf `permission.asked` protokollieren, wofür der Agent um Erlaubnis
  gefragt hat und was geantwortet wurde

## Leitplanken

- Ein Plugin läuft bei **jedem** passenden Ereignis. Haltet es klein und
  schnell, sonst bremst es jede Sitzung.
- Nichts Blockierendes und keine Netzwerkaufrufe.
- Fehler im Plugin können die Sitzung stören — im Zweifel `opencode run
  --pure` starten, das lädt keine Plugins.
