# Platform Demo Backend

REST API built with FastAPI, deployed on Cloud Run via the GCP Serverless Platform.

## Architecture

- **Runtime**: Cloud Run (Direct VPC Egress)
- **Database**: Cloud SQL PostgreSQL (IAM Auth)
- **Storage**: Cloud Storage (volume mount)
- **Secrets**: Secret Manager (volume mount, auto-rotation)
- **Auth**: JWT signed with API key from Secret Manager

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | /health | No | Liveness check |
| GET | /readiness | No | Readiness check (DB) |
| POST | /auth/token | No | Get JWT token |
| GET | /items | Yes | List items |
| POST | /items | Yes | Create item |
| GET | /items/{id} | Yes | Get item |
| PUT | /items/{id} | Yes | Update item |
| DELETE | /items/{id} | Yes | Delete item |
| POST | /files/upload | Yes | Upload to Cloud Storage |
| GET | /files | Yes | List uploaded files |

## Running locally

```bash
cp .env.example .env
# fill in DATABASE_URL and API_SECRET_KEY
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

## Running tests

```bash
pytest --cov=app tests/
```
