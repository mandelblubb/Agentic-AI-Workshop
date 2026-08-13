"""Minimaler MCP-Server als Startgerüst für Spur B (freie Entwicklung).

Enthält ein einziges, funktionierendes Beispiel-Tool, das gegen die laufende
Workshop-API (uvicorn src.api:app) spricht. Teilnehmende erweitern diesen
Server um eigene Tools, statt bei einem leeren Blatt zu starten.

Voraussetzung: die Workshop-App läuft lokal (siehe README.md), z. B.
    uvicorn src.api:app --reload
"""

from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

API_BASE_URL = "http://127.0.0.1:8000"

mcp = FastMCP("convention-app-tools")


@mcp.tool()
def list_events() -> list[dict[str, Any]]:
    """Listet alle Veranstaltungen der Convention App auf."""
    response = httpx.get(f"{API_BASE_URL}/events", timeout=5.0)
    response.raise_for_status()
    return response.json()


# --- Ab hier: eigene Tools ergänzen -----------------------------------
#
# Ideen zum Weiterbauen (nur Anregungen, keine Vorgabe):
#   - freie_kapazitaet(): Kapazität je Veranstaltung berechnen
#     (max_participants - Anzahl Anmeldungen), sobald es einen
#     /events/{id}/registrations-Endpoint gibt.
#   - doppelbuchungen_pruefen(): auffällige Muster über mehrere
#     Veranstaltungen hinweg zusammenfassen.
#   - wochenbericht(): neu angelegte Veranstaltungen der letzten
#     N Tage als kurzen Text zusammenfassen.
#
# Ein neues Tool braucht nur eine mit @mcp.tool() dekorierte Funktion mit
# Type Hints und Docstring - FastMCP generiert das Tool-Schema daraus
# automatisch.


if __name__ == "__main__":
    mcp.run()
