# URL Shortener (FastAPI)

Simple URL shortener built with FastAPI.

## Features
- Shorten URLs
- Redirect URLs
- Random code generator
- In-memory storage

## Tech Stack
- Python
- FastAPI
- Uvicorn

## Run project

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


API

POST /shorten

{
  "url": "https://google.com"
}

Response:

{
  "short_url": "http://127.0.0.1:8000/abc123"
}

---

