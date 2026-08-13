"""Template: MCP-Server fuer Spur B (freie Entwicklung).

Fuellt die TODOs aus, um einen MCP-Server zu bauen, der gegen die laufende
Workshop-API (uvicorn src.api:app) spricht. Vergleicht euer Ergebnis danach
mit server_komplett.py.

Voraussetzung: die Workshop-App laeuft lokal (siehe README.md), z. B.
    uvicorn src.api:app --reload
"""

import httpx
from mcp.server.fastmcp import FastMCP

API_BASE_URL = "http://127.0.0.1:8000"

mcp = None  # TODO FastMCP-Server mit einem aussagekraeftigen Namen erstellen


@mcp.tool()
def list_events():
    # TODO Docstring: was macht dieses Tool? (wird als Tool-Beschreibung genutzt)

    # TODO GET-Request gegen API_BASE_URL + "/events" ausfuehren
    response = None

    # TODO Response validieren (z. B. response.raise_for_status()) und als
    # Liste von Dicts zurueckgeben
    return None


# --- Ab hier: eigene Tools ergaenzen -----------------------------------
#
# Ideen zum Weiterbauen (nur Anregungen, keine Vorgabe):
#   - freie_kapazitaet(): Kapazitaet je Veranstaltung berechnen
#     (max_participants - Anzahl Anmeldungen), sobald es einen
#     /events/{id}/registrations-Endpoint gibt.
#   - doppelbuchungen_pruefen(): auffaellige Muster ueber mehrere
#     Veranstaltungen hinweg zusammenfassen.
#   - wochenbericht(): neu angelegte Veranstaltungen der letzten
#     N Tage als kurzen Text zusammenfassen.


if __name__ == "__main__":
    pass  # TODO Server starten
