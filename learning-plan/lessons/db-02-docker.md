# DB-02 — MySQL in Docker

**Goal:** Run MySQL in a Docker container instead of installing it locally, and connect the FastAPI backend to it.

> **Ce vei învăța / What you'll learn**
> - Ce este Docker și de ce e util *(what Docker is and why it matters)*
> - `docker-compose.yml` — definești servicii cu un singur fișier *(define services in one YAML file)*
> - Variabile de mediu cu `.env` *(environment variables)*
> - Cum reconectezi SQLAlchemy la MySQL *(switching back to MySQL)*

---

## Concept

**Docker** packages a program (like MySQL) with everything it needs to run — so you don't install MySQL, you just run a container.

**Docker Compose** lets you define services in a YAML file and start them all with one command:

```yaml
# docker-compose.yml
services:
  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: ping_pong_db
    ports:
      - "3306:3306"
```

Start it:

```bash
docker compose up -d
```

Stop it:

```bash
docker compose down
```

Then point the backend at it via `.env`:

```
DATABASE_USER=root
DATABASE_PASSWORD=secret
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_NAME=ping_pong_db
```

And update `db/__init__.py` to read from `.env`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}"
    f"@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
)
```

---

## Exercise

1. Create `docker-compose.yml` in the project root with a MySQL 8 service
2. Update `.env` with matching credentials
3. Run `docker compose up -d` and confirm MySQL is running (`docker ps`)
4. Start the FastAPI server — it should connect and create the `players` table
5. Test with a POST and GET via `/docs`

---

## Done when…

- `docker compose up -d` starts MySQL with no errors
- The FastAPI server connects and `players` table is created automatically
- Data added via POST persists in the running container

---

## Stretch 🏓

Add a `volumes:` section to Docker Compose so data survives container restarts:

```yaml
volumes:
  - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```
