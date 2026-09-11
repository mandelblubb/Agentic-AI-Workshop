# Prompt-Bibliothek

Prompts zum Kopieren — für den Workshop und danach für eure eigenen Projekte.
Begriffe, die hier vorkommen, stehen in `docs/GLOSSAR.md`.

Das sind Ausgangspunkte, keine Zaubersprüche: passt sie an eure Aufgabe an.
Der gemeinsame Nenner der wirksamen Muster ist immer derselbe — **erst
verstehen und planen lassen, dann ändern lassen, dann prüfen.**

## 1. Repository verstehen

*Wann:* Ihr steht vor einer fremden Codebasis und wollt wissen, wie sie gebaut
ist.

```text
Analysiere dieses Repository.

Verändere keine Dateien.

Erkläre mir:
- wofür die Anwendung da ist
- wie der Code aufgeteilt ist und welche Datei wofür zuständig ist
- wie die Tests aufgebaut sind und wie ich sie ausführe
- welche Konventionen ich beachten muss, wenn ich etwas ergänze

Nenne am Ende drei Stellen, an denen du dir unsicher bist.
```

*Worauf achten:* Liest er wirklich Dateien, oder rät er aus den Dateinamen?
Dieser Prompt ist zugleich der beste Einstieg in ein Projekt, das ihr im
Alltag übernehmt.

## 2. Ticket umsetzen (Plan-first)

*Wann:* Der Standard-Auftrag für ein Issue. Trennt bewusst Planen von Ändern.

```text
Lies AGENTS.md und issues/ISSUE-01-registration.md.

Analysiere zuerst Architektur und bestehende Tests.
Erstelle einen kurzen Plan und ändere bis dahin keine Dateien.

Implementiere danach das Issue vollständig.
Ergänze sinnvolle Tests, führe alle Tests aus und behebe Fehler.
Prüfe abschließend git diff und alle Akzeptanzkriterien.
Nenne mögliche Restrisiken.
```

*Worauf achten:* Hält er sich an „bis dahin keine Dateien"? Und führt er die
Tests wirklich aus — oder behauptet er nur, dass sie grün sind? Der
Unterschied ist im Verlauf sichtbar: Es muss ein Tool-Call mit `pytest` und
dessen Ausgabe zu sehen sein.

## 3. Zweiter Agent als Reviewer

*Wann:* Nach einer vermeintlich fertigen Implementierung. In einer **neuen**
Session starten — ein Agent, der seinen eigenen Code prüft, findet
erfahrungsgemäß weniger.

```text
Du bist Reviewer, nicht Entwickler.

Lies AGENTS.md, das umgesetzte Issue und den aktuellen git diff.
Verändere keine Dateien.

Prüfe:
- Erfüllung der Akzeptanzkriterien
- Testabdeckung
- Architektur
- Datenschutz
- Randfälle

Liefere Findings nach Schweregrad.
```

*Worauf achten:* Findet der zweite Agent etwas, das der erste übersehen hat?
Und findet *ihr* etwas, das beide übersehen haben — das ist die interessantere
Frage.

## 4. „Wo bist du unsicher?"

*Wann:* Direkt nach einer Änderung, bevor ihr sie selbst durchgeht. Kostet
zehn Sekunden und lenkt euer Review auf die richtigen Stellen.

```text
Gehe deine eigene Änderung noch einmal durch.

Nenne mir:
- die Stelle, bei der du dir am unsichersten bist, und warum
- Annahmen, die du getroffen hast, ohne dass sie im Issue standen
- was bei deiner Lösung kaputtgehen könnte, ohne dass ein Test es merkt
```

*Worauf achten:* Antwortet er konkret und mit Dateiverweisen — oder allgemein
und gefällig („man könnte noch mehr Tests schreiben")? Nur die konkrete
Antwort ist etwas wert.

## 5. Test zuerst

*Wann:* Bei Fehlerbehebungen und bei Anforderungen, die sich klar als Testfall
formulieren lassen.

```text
Schreibe zuerst einen Test, der das gewünschte Verhalten prüft und
mit dem aktuellen Stand fehlschlägt. Führe ihn aus und zeige mir,
dass er rot ist.

Implementiere erst danach die Änderung, bis der Test grün ist.
Lösche oder entschärfe dabei keine bestehenden Tests.
```

*Worauf achten:* Der rote Test ist der Beweis, dass er tatsächlich das
Richtige prüft. Ein Test, der von Anfang an grün ist, sichert oft gar nichts
ab.

## 6. Commit-Message aus dem Diff

*Wann:* Wenn eine Änderung fertig und von euch geprüft ist.

```text
Lies git diff und schlage eine Commit-Message vor.

Erste Zeile knapp und in der Sache, danach eine kurze Begründung,
warum die Änderung nötig war.
Committe nicht selbst — gib mir nur den Text.
```

*Worauf achten:* Beschreibt die Message, was sich fachlich ändert, oder zählt
sie nur Dateien auf? Nebenbei ein guter Test dafür, ob die Änderung klein
genug geschnitten war: Wenn die Message eine Aufzählung braucht, waren es
mehrere Änderungen.

## 7. Aufgabe kleiner schneiden

*Wann:* Wenn der Agent zu viel auf einmal anfasst, sich festfährt oder ihr den
Überblick über den Diff verliert.

```text
Halte an. Verändere vorerst nichts mehr.

Zerlege die Aufgabe in die kleinstmöglichen Schritte, die einzeln
lauffähig und testbar sind.
Zeige mir die Liste und beginne erst nach meiner Freigabe mit Schritt 1.
```

*Worauf achten:* Das ist der wirksamste Notausgang. Wenn auch das nicht hilft:
Änderungen mit `git checkout -- .` verwerfen und in einer neuen Session mit
einem kleineren Auftrag anfangen.

## Eigenes Issue erzeugen lassen

Dafür gibt es einen eigenen, längeren Prompt inklusive Leitplanken:
`docs/CUSTOM_ISSUE_PROMPT.md`.
