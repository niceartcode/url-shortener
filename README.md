# 🚀 URL Shortener (FastAPI)

A simple but powerful URL shortener built with FastAPI.

---

## ✨ Features
- 🔗 Shorten long URLs
- ↪️ Redirect short URLs
- ⚡ FastAPI backend
- 🎲 Random code generator
- 💾 In-memory storage (demo)

---

## 🛠 Tech Stack
- Python 🐍
- FastAPI ⚡
- Uvicorn 🚀



## 📦 Installation


git clone https://github.com/niceartcode/url-shortener.git
cd url-shortener/backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt


▶️ Run Project

bash
uvicorn main:app --reload

Then open:

http://127.0.0.1:8000/docs
📌 API Usage
🔹 POST /shorten

Request:

{
  "url": "https://google.com"
}

Response:

{
  "short_url": "http://127.0.0.1:8000/abc123"
}
🔹 Redirect

Open in browser:

http://127.0.0.1:8000/abc123

➡️ Redirects to original URL

🧠 How it works
User sends URL to /shorten
Server generates random code
Stores it in memory (dictionary)
Returns short URL
Visiting short URL redirects to original URL
⚠️ Limitations
❌ No database (data resets on restart)
❌ No authentication
❌ Demo project only
🚀 Future Improvements
SQLite / PostgreSQL database
Click tracking
Frontend UI
User system
Deploy to cloud (Render / Railway)



---
