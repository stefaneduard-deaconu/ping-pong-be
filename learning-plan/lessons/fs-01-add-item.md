# FS-01 — Add a Player: End-to-End

**Goal:** One complete flow — user types a name, Angular sends POST, FastAPI adds to the list, Angular refreshes and shows the new player.

> **Ce vei învăța / What you'll learn**
> - Cum funcționează un flow complet frontend ↔ backend *(full request/response cycle)*
> - Debugging: Network tab în browser + FastAPI `/docs` *(how to debug HTTP)*
> - Gestionarea erorilor de bază *(basic error handling in the UI)*

> **Prerequisite:** BE-02 and FE-04 must be complete.

---

## Concept

This lesson is mostly **integration** — making the backend from BE-02 and the frontend from FE-04 work together cleanly.

**Common problems and how to fix them:**

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `CORS error` in browser console | `allow_origins` in `main.py` doesn't include `http://localhost:4200` | Add it to the list |
| `422 Unprocessable Entity` from backend | The JSON body doesn't match the Pydantic model | Check the field name — must be `"name"` |
| Player added but list doesn't update | `loadPlayers()` not called after POST | Call it in the `next` callback |

**How to debug step by step:**

1. Open browser DevTools → **Network** tab
2. Click "Add" and find the POST request
3. Check: Request URL, Request Body (under Payload), Response status and body
4. If the request never shows up → the button click handler is not wired correctly
5. If the request shows up with an error → fix the backend or the body format

---

## Exercise

Verify the complete add-player flow works end-to-end:

1. Start backend: `uvicorn main:app --reload`
2. Start frontend: `npm start`
3. Type a name and click "Add"
4. In the Network tab, confirm:
   - Method is `POST`, URL is `http://localhost:8000/players`
   - Request body contains `{ "name": "..." }`
   - Response is `200` with the new player's data
5. The new player appears in the list immediately

If something breaks — debug it step by step. Do not guess; read the error.

---

## Done when…

- The complete add flow works reliably
- You can explain what happens at each step:  
  *button click → service method → HTTP POST → backend route → list updated → response → signal updated → template re-renders*

---

## Stretch 🏓

Show an error message in the UI (not just `console.error`) if the POST fails — for example when the backend is offline.
