# Rios AI – Artefact Edition

Rios AI is a full-stack AI assistant developed as part of the technical challenge for the **Junior AI Engineer** position.

The system combines a Python backend using FastAPI with a Next.js frontend, integrating a Language Model (LLM) with real tools such as:

- 🔢 **Smart Calculator**
- 💱 **Currency Exchange Rates**
- ₿ **Cryptocurrency Prices**
- 🌦 **Weather Information**
- 🤖 **LLM with short-term memory + special greeting for Artefact users**

---

## 📁 Project Architecture

```
rios-ai/
│ README_EN.md <-- Main documentation file (English version)
│
├─ ai-assistant/ <-- Python Backend (FastAPI)
│ ├─ assistant.py       <-- LLM logic + tool routing
│ ├─ server.py          <-- /chat API
│ ├─ tools/
│ │ ├─ calculator.py
│ │ ├─ currency.py
│ │ ├─ crypto.py
│ │ └─ weather.py
│ └─ requirements.txt
│
└─ rios-ai-web/ <-- Next.js Frontend
   ├─ app/
   │ ├─ page.tsx
   │ └─ api/chat/route.ts
   ├─ package.json
   └─ ...
```

---

## 🔄 Application Flow

1. The user types a message on the frontend.
2. Next.js sends the message to `/api/chat`.
3. The route forwards the message to the Python backend.
4. Python decides whether to use:
   - Calculator  
   - Weather  
   - Currency  
   - Crypto  
   - Or the LLM  
5. The response is shown in the chat.

---

# ⚙️ Backend Installation (`ai-assistant/`)

### 1. Create virtual environment

```bash
cd ai-assistant
python -m venv .venv
# Activate:
.\.venv\Scripts ctivate   # Windows
source .venv/bin/activate  # Linux/Mac
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env`

```
OPENAI_API_KEY=your_key_here
DEBUG=true
```

### 4. Run FastAPI server

```bash
uvicorn server:app --reload --host 127.0.0.1 --port 8000
```

Main endpoint:

```
POST http://127.0.0.1:8000/chat
```

---

# 🎨 Frontend Installation (`rios-ai-web/`)

### 1. Install packages

```bash
cd rios-ai-web
npm install
```

### 2. Start dev server

```bash
npm run dev
```

Access:

```
http://localhost:3000
```

---

# ✨ Implemented Features

### 🔢 Smart Calculator  
Parses math expressions in natural language.  
Supports `*`, `/`, `x`, `×`, `^`, etc.

### 🌦 Weather Query  
Real-time temperature + conditions for any city.

### 💱 Currency Exchange  
Live rates for USD, EUR, GBP.

### ₿ Crypto Prices  
BTC and ETH price retrieval.

### 🧠 LLM Engine  
- Short-term memory (last 6 exchanges)  
- Special greeting when user mentions **Artefact**  
- Model: `gpt-4o-mini`  

---

# 🧪 Example Questions

- “How much is 12 + 35 * 2?”
- “What's the price of Bitcoin today?”
- “What’s the dollar exchange rate?”
- “What's the weather like in Uberlândia?”
- “Hello, I’m from Artefact.”

---

# 🚀 Future Enhancements

- Streaming responses on frontend  
- Persistent conversation history  
- Deployment (Vercel + Railway)  
- Admin dashboard  

---

# 👤 Author

**Pedro Rios**  
Engineer & Developer  
Building intelligent solutions with AI 🚀
