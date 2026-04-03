# Ping-Pong — Learning Plan

> **Pace:** small focused lessons (~30–60 min each). One lesson per session is enough.

## Student context

- Learning FastAPI (Python) + Angular (TypeScript) to build a full-stack web app
- Also studying DSA, C, and Assembly at university — keep sessions small and focused

---

## Phase 1 — Foundation (no database) · ~3–4 weeks

The backend runs with a simple **in-memory list** instead of a real database.  
This removes all setup friction so we can focus purely on learning concepts.

### Backend

| #  | Lesson | Topic |
|----|--------|-------|
| 1  | [be-01 — Modularise the backend](lessons/be-01-modularize.md) | APIRouter, remove DB dependency |
| 2  | [be-02 — CRUD on in-memory list](lessons/be-02-crud-memory.md) | GET / POST / DELETE, Pydantic |

### Frontend

| #  | Lesson | Topic |
|----|--------|-------|
| 3  | [fe-01 — Template basics](lessons/fe-01-template-basics.md) | Interpolation, @if, @for, component data |
| 4  | [fe-02 — New component](lessons/fe-02-new-component.md) | ng generate, @Input, reusable component |
| 5  | [fe-03 — Fetch data from backend](lessons/fe-03-fetch-data.md) | Service, HttpClient, signals |
| 6  | [fe-04 — Send data to backend](lessons/fe-04-post-data.md) | Form input, POST request |

### Full-stack

| #  | Lesson | Topic |
|----|--------|-------|
| 7  | [fs-01 — Add a player end-to-end](lessons/fs-01-add-item.md) | Form ? POST ? refresh list |
| 8  | [fs-02 — Delete a player end-to-end](lessons/fs-02-delete-item.md) | Delete button ? DELETE ? refresh list |

---

## Phase 2 — Real database + Docker · ~2–3 weeks

| #  | Lesson | Topic |
|----|--------|-------|
| 9  | [db-01 — SQLite + SQLAlchemy](lessons/db-01-sqlite.md) | ORM intro, no Docker needed |
| 10 | [db-02 — MySQL in Docker](lessons/db-02-docker.md) | Docker Compose, environment variables |
| 11 | [db-03 — Full CRUD with DB](lessons/db-03-full-crud.md) | Sessions, dependency injection, all routes |

---

## Progress tracker

- [ ] be-01
- [ ] be-02
- [ ] fe-01
- [ ] fe-02
- [ ] fe-03
- [ ] fe-04
- [ ] fs-01
- [ ] fs-02
- [ ] db-01
- [ ] db-02
- [ ] db-03
