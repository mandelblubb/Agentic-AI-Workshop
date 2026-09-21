# Vorlagen zum Mitnehmen

Leere Gerüste für die sechs Wege, einen Coding Agenten zu erweitern — gedacht
für **euer eigenes Projekt**, nicht für die Convention App.

Der Unterschied zu `.opencode/` in diesem Repository: Dort liegen lauffähige
Beispiele, die gegen *diese* Anwendung arbeiten. Hier liegen Rohlinge, die ihr
in ein beliebiges Repository kopiert und ausfüllt.

## Wohin welche Datei gehört

| Vorlage | Zielort im eigenen Projekt |
|---------|----------------------------|
| `AGENTS.md.template` | `AGENTS.md` im Wurzelverzeichnis |
| `command.md.template` | `.opencode/commands/<name>.md` |
| `SKILL.md.template` | `.opencode/skills/<name>/SKILL.md` |
| `subagent.md.template` | `.opencode/agents/<name>.md` |
| `plugin.js.template` | `.opencode/plugins/<name>.js` |
| `opencode.json.template` | `opencode.json` im Wurzelverzeichnis |

Die Endung `.template` beim Kopieren entfernen. Sie steht nur dran, damit eine
Vorlage voller Platzhalter nicht versehentlich als echte Konfiguration oder als
echtes Regelwerk eingelesen wird.

**Alle Platzhalter in spitzen Klammern ersetzen**, nicht nur die offensichtlichen.
Ein stehengebliebenes `<PluginName>` ist ein JavaScript-Syntaxfehler, der die
Sitzung stört; ein stehengebliebenes `agent: <name-eines-subagenten>` lässt
OpenCode einen Agenten suchen, den es nicht gibt.

## Womit anfangen

`AGENTS.md` zuerst. Es ist die einzige Erweiterung, die ohne jede Konfiguration
wirkt und bei jeder Aufgabe gilt — und in den meisten Projekten holt sie den
größten Teil des Nutzens. Alles andere lohnt sich erst, wenn ihr merkt, dass
ihr dieselbe Anweisung zum dritten Mal tippt.

Danach in dieser Reihenfolge, nach steigendem Aufwand:

1. **Command**, wenn ihr einen Ablauf bewusst startet
2. **Skill**, wenn der Agent selbst erkennen soll, wann etwas gilt
3. **Subagent**, wenn jemand mit weniger Rechten prüfen soll
4. **Plugin**, wenn etwas passieren muss, auch ohne dass das Modell daran denkt
5. **MCP-Server**, wenn der Agent an Daten außerhalb des Repositorys muss

## Ein verbreitetes Missverständnis

Es gibt in OpenCode **keine `mcp.json`**. Diese Datei ist eine Konvention
anderer Clients. In OpenCode werden MCP-Server im `mcp`-Block der
`opencode.json` eingetragen — siehe `opencode.json.template`.

Ebenso gibt es **keinen Konfigurationsschlüssel `hooks`**. Was anderswo Hook
heißt, ist hier ein Plugin; die Hook-Namen sind die Ereignisse darin.

Und ein Command hat **kein Feld `allowed-tools`**. Rechte hängen in OpenCode am
Agenten: Ein Command, der nichts ändern soll, bekommt mit `agent:` einen
Subagenten, dem das Ändern entzogen ist — siehe `command.md.template`.

## Verlässlich statt geraten

Die Schlüsselnamen in diesen Vorlagen stammen aus dem offiziellen Schema unter
<https://opencode.ai/config.json>. Wenn eine Konfiguration nicht greift, lohnt
sich dort der Blick zuerst — Feldnamen ändern sich zwischen Versionen
gelegentlich.

Was ein Plugin-Ereignis an Daten mitbringt, steht nach dem ersten Start
typisiert in `.opencode/node_modules/@opencode-ai/sdk/dist/gen/types.gen.d.ts`.
