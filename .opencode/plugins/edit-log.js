/**
 * Nachvollziehbarkeit: schreibt jede Dateiänderung des Agenten mit
 * Zeitstempel nach .opencode/edit-log.txt.
 *
 * Startgerüst für Gruppe B (Werkzeuge bauen). Ein Plugin ist die Stelle, an
 * der ihr euch auf Ereignisse des Agenten hängt. Hier: "file.edited".
 *
 * Weitere Ereignisse, an die ihr euch hängen könnt:
 *   tool.execute.before   bevor ein Werkzeug läuft
 *   tool.execute.after    danach
 *   session.created       neue Sitzung
 *   session.idle          Agent ist fertig
 *   permission.asked      Agent fragt um Erlaubnis
 *
 * Die Nutzlast je Ereignis steht typisiert in
 * .opencode/node_modules/@opencode-ai/sdk/dist/gen/types.gen.d.ts —
 * dort nachsehen, statt zu raten. Für file.edited ist es { file: string }.
 */

import { appendFile } from "node:fs/promises"
import { join } from "node:path"

export const EditLog = async ({ directory }) => {
  const logPath = join(directory, ".opencode", "edit-log.txt")

  return {
    event: async ({ event }) => {
      if (event.type !== "file.edited") return

      const zeile = `${new Date().toISOString()}  ${event.properties.file}\n`
      await appendFile(logPath, zeile, "utf8")
    },
  }
}
