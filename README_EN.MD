# Rios AI – Artefact Edition

Rios AI is a full-stack AI assistant built as part of the technical challenge for the **AI Engineer Junior** position.

It combines a Python backend (FastAPI) with a modern Next.js frontend, integrating a Large Language Model (LLM) with real functional tools:

- 🔢 Smart calculator  
- 💱 Currency exchange rates  
- ₿ Cryptocurrency prices  
- 🌦 Weather information  
- 🤖 LLM with short-term memory and custom greetings for Artefact users  

---

## 📁 Project Architecture

rios-ai/
│ README.md
│
├─ ai-assistant/ # Python backend (FastAPI)
│ ├─ assistant.py
│ ├─ server.py
│ ├─ tools/
│ │ ├─ calculator.py
│ │ ├─ currency.py
│ │ ├─ crypto.py
│ │ └─ weather.py
│ └─ requirements.txt
│
└─ rios-ai-web/ # Next.js frontend
├─ app/
│ ├─ page.tsx
│ └─ api/chat/route.ts
├─ package.json

markdown
Copiar código

Application flow:

1. User sends a message through the web chat.
2. Next.js calls `/api/chat`.
3. The route forwards the message to the Python backend.
4. The backend chooses between:
   - Calculator  
   - Currency  
   - Crypto  
   - Weather  
   - Or the LLM  
5. The final answer is displayed in the chat UI.

---

## ⚙️ Backend Setup (`ai-assistant/`)

### 1. Create virtual environment

```bash
cd ai-assistant
python -m venv .venv
.\.venv\Scripts\activate
2. Install dependencies
bash
Copiar código
pip install -r requirements.txt
3. Environment variables
Create .env:

env
Copiar código
OPENAI_API_KEY=xxxxxx
DEBUG=true
4. Start FastAPI server
bash
Copiar código
uvicorn server:app --reload --host 127.0.0.1 --port 8000
Endpoint:
POST http://127.0.0.1:8000/chat

🎨 Frontend Setup (rios-ai-web/)
1. Install dependencies
bash
Copiar código
cd rios-ai-web
npm install
2. Start development server
bash
Copiar código
npm run dev
App runs at:

arduino
Copiar código
http://localhost:3000
✨ Features
🔢 Smart Calculator
Detects expressions inside natural language.

Supports multiplication symbols, exponentiation, and sanitization.

🌦 Weather Fetching
Returns city temperature and conditions.

💱 Currency Rates
USD, EUR, GBP support.

₿ Cryptocurrency Prices
Bitcoin and Ethereum.

🧠 LLM Integration
Short-term memory (last 6 messages)

Special greeting when the user mentions “Artefact”

Model: gpt-4o-mini

🧪 Example Queries
“How much is 12 + 35 * 2?”

“Bitcoin price today?”

“USD exchange rate?”

“Weather in Uberlândia?”

“Hello, I am from Artefact.”

🚀 Possible Improvements
Streaming responses

Conversation history persistence

Production deploy

Admin dashboard

👤 Author
Pedro Rios
Developer & Engineer