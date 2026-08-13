# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A small FastAPI application used as the hands-on subject of a workshop on agentic software
engineering ("Vom Ticket zum getesteten Code mit einem Coding Agenten"). The app itself
(managing Fortbildungsveranstaltungen / training events) is not the point — it exists to be
extended feature-by-feature via `issues/ISSUE-*.md` tickets during the workshop. Everything is
in-memory; there is no database and no external network dependency.

## Binding rules (AGENTS.md)

This repo has an `AGENTS.md` with rules that are enforced during the workshop and must be
followed:

- `src/api.py` = HTTP endpoints and mapping of domain exceptions to HTTP errors only.
- `src/service.py` = all business/domain logic. Business logic must never be implemented
  directly in API routes.
- `src/models.py` = Pydantic data models.
- Tests live only under `tests/`.
- Don't unintentionally change existing behavior; don't delete or weaken existing tests just to
  make a new implementation pass.
- Add tests for new functionality; run the full test suite before considering a task done.
- New dependencies need a clear justification.
- Public functions should use type hints.
- No secrets/credentials in files, no personal data (names, agencies, etc.) in logs or in API
  error messages — this comes up concretely in ISSUE-02.
- Git: `git status`/`git diff`/`git log` are fine to run; never commit or push without explicit
  request; never rewrite/delete git history.

## Commands

```bash
# install (uv)
uv sync
uv run pytest

# install (pip)
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -e ".[dev]"

# run tests
pytest              # whole suite, expected clean baseline: 6 passed
pytest tests/test_service.py::test_service_raises_for_unknown_event   # single test

# run the app
uvicorn src.api:app --reload
# API: http://127.0.0.1:8000  Swagger UI: http://127.0.0.1:8000/docs
```

## Architecture

Three-layer split, strictly enforced by `AGENTS.md`:

- `src/models.py` — Pydantic models (`EventCreate`, `Event`, and future `Registration`-style
  models). No behavior.
- `src/service.py` — `EventService`: holds all state in plain dicts (`self._events`, an
  auto-incrementing `_next_id`) and all domain logic. Domain errors are raised as custom
  exceptions (e.g. `EventNotFoundError`) rather than HTTP exceptions — the service layer must
  stay HTTP-agnostic.
- `src/api.py` — FastAPI app and routes. A single module-level `service = EventService()`
  instance is shared for the app's lifetime. Routes are thin: call the service, catch domain
  exceptions, translate to `HTTPException` with the appropriate status code (e.g.
  `EventNotFoundError` → 404).

Tests mirror this split: `tests/test_service.py` exercises `EventService` directly;
`tests/test_api.py` exercises HTTP behavior via FastAPI's `TestClient`. `tests/conftest.py`
provides a `client` fixture and an autouse `reset_service` fixture that clears
`EventService` state (via `service.reset()`) between tests — new state added to the service
must be cleared in `reset()` too, or tests will leak state across each other.

When extending the domain (e.g. adding registrations to events), follow the same pattern: new
Pydantic model in `models.py`, state + logic + custom exceptions in `service.py`, thin route +
exception-to-HTTPException mapping in `api.py`.

## Workshop context (issues/)

`issues/ISSUE-01-registration.md`, `ISSUE-02-security-review.md`, and `ISSUE-03-validation.md`
are sequential workshop tasks, gated by the workshop facilitator ("Workshop-Leitung") — do not
assume all of them are in scope unless told so. ISSUE-02 in particular is a privacy/security
finding that may require no code change if the ISSUE-01 implementation already avoids leaking
personal data in error responses — in that case, justify why and back it with a test rather than
changing code speculatively.