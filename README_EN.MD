# Rios AI – Artefact Edition

Rios AI is a full‑stack AI assistant developed as part of the technical challenge for the **AI Engineer Junior** position at Artefact.

The system integrates:
- 🧠 **LLM** (gpt-4o-mini)
- 🐍 **Python Backend (FastAPI)**
- ⚛️ **Next.js + React Frontend**
- 🔧 **Real tools for calculations, weather, currency, and crypto queries**

The assistant automatically selects the best tool for each request, maintains short‑term memory, and provides a special greeting when it identifies Artefact users.

---

## 📁 Project Architecture

```text
rios-ai/
│  README.md               <-- Main documentation
│
├─ ai-assistant/           <-- Python Backend
│  ├─ assistant.py         <-- LLM + tool orchestration logic
│  ├─ server.py            <-- FastAPI /chat endpoint
│  ├─ tools/
│  │   ├─ calculator.py
│  │   ├─ currency.py
│  │   ├─ crypto.py
│  │   └─ weather.py
│  └─ requirements.txt
│
└─ rios-ai-web/            <-- Next.js Frontend
   ├─ app/
   │   ├─ page.tsx
   │   └─ api/chat/route.ts
   ├─ package.json
   └─ ...
```

---

# ⚙️ Backend Installation (`ai-assistant/`)

### 1️⃣ Create virtual environment

```bash
cd ai-assistant
python -m venv .venv

# Windows
.\.venv\Scripts ctivate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create `.env`

```env
OPENAI_API_KEY=your_key_here
DEBUG=true
```

### 4️⃣ Run FastAPI server

```bash
uvicorn server:app --reload --host 127.0.0.1 --port 8000
```

---

# 🎨 Frontend Installation (`rios-ai-web/`)

### 1️⃣ Install dependencies

```bash
cd rios-ai-web
npm install
```

### 2️⃣ Run Next.js server

```bash
npm run dev
```

Access:

```
http://localhost:3000
```

---

# 🔎 Implementation Logic

The solution follows a simple, clean, and modular architecture—aligned with the challenge requirement (“solve it in the simplest possible way”), while maintaining professional structure.

### ✔️ 1. Message Classification
The assistant analyzes each input and determines the appropriate tool:

- Mathematical expressions → calculator  
- Weather keywords → weather API  
- Currency terms → exchange rate lookup  
- Crypto terms → cryptocurrency price lookup  
- None of the above → LLM response  

### ✔️ 2. Modular Tool Orchestration  
Each tool is implemented in a dedicated module inside `tools/`, making the system easily extensible.

### ✔️ 3. LLM Fallback  
The `gpt-4o-mini` model answers general questions, with:

- Short‑term memory (last 6 messages)  
- Special greetings for Artefact users  
- Logging for debugging and traceability  

### ✔️ 4. Minimalist Frontend  
The UI was built with Next.js to provide clarity, simplicity, and an intuitive chat interface for evaluators.

---

# 🎓 What I Learned

Throughout the development, I strengthened my skills in:

- Full‑stack architecture for AI applications  
- Tool‑oriented reasoning and LLM orchestration  
- Modular and maintainable system design  
- Integration between Python ↔ Next.js  
- Error handling and professional logging practices  
- Message flow between frontend → API → backend  

---

# 🔧 What I Would Improve With More Time

With extra time, I would enhance the project by:

- Implementing **token streaming** in the frontend  
- Improving intent detection with a small local model  
- Persisting conversation history in a database  
- Deploying the full system (Vercel + Railway or Docker Compose)  
- Adding unit tests for each tool  
- Building an administrative dashboard for monitoring  

---

# 🧪 Examples

```
How much is 12 + 35 * 2?
What is the weather in Uberlândia?
What is the price of Bitcoin today?
Hello, I am from Artefact!
```

---

# 👤 Author

**Pedro Rios**  
Engineer & Developer  
Building intelligent solutions with AI 🚀
