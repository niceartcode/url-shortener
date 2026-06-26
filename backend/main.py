from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import random
import string

app = FastAPI()

# Түр хадгалах сан (database биш, memory)
db = {}

# Request body
class URLRequest(BaseModel):
    url: str

# Random code үүсгэх функц
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# Home page
@app.get("/")
def home():
    return {"message": "URL Shortener is running"}


# URL shorten хийх endpoint
@app.post("/shorten")
def shorten_url(request: URLRequest):
    code = generate_code()

    db[code] = request.url

    return {
        "short_url": f"http://127.0.0.1:8000/{code}"
    }


# Redirect хийх endpoint
@app.get("/{code}")
def redirect_url(code: str):
    url = db.get(code)

    if url:
        return RedirectResponse(url=url)

    return {"error": "URL not found"}
