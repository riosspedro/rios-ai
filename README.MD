# Rios AI – Artefact Edition

Rios AI é um assistente de IA full-stack desenvolvido como parte do desafio técnico para a vaga de **AI Engineer Júnior** na Artefact.

O sistema combina:
- 🧠 **LLM** (gpt-4o-mini)
- 🐍 **Backend em Python (FastAPI)**
- ⚛️ **Frontend com Next.js + React**
- 🔧 **Ferramentas reais para cálculos, clima, moedas e criptos**

O assistente escolhe automaticamente a melhor ferramenta para cada pergunta, possui memória curta e envia saudações especiais quando identifica usuários da Artefact.

---

## 📁 Arquitetura do Projeto

```text
rios-ai/
│  README.md               <-- Documentação principal
│
├─ ai-assistant/           <-- Backend Python
│  ├─ assistant.py         <-- LLM + lógica de ferramentas
│  ├─ server.py            <-- API FastAPI /chat
│  ├─ tools/
│  │   ├─ calculator.py
│  │   ├─ currency.py
│  │   ├─ crypto.py
│  │   └─ weather.py
│  └─ requirements.txt
│
└─ rios-ai-web/            <-- Frontend Next.js
   ├─ app/
   │   ├─ page.tsx
   │   └─ api/chat/route.ts
   ├─ package.json
   └─ ...
```

---

## ⚙️ Instalação – Backend (`ai-assistant/`)

### 1️⃣ Criar ambiente virtual

```bash
cd ai-assistant
python -m venv .venv

# Windows
.\.venv\Scripts\activate
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Criar arquivo `.env`

```env
OPENAI_API_KEY=sua_chave_aqui
DEBUG=true
```

### 4️⃣ Rodar o servidor FastAPI

```bash
uvicorn server:app --reload --host 127.0.0.1 --port 8000
```

---

## 🎨 Instalação – Frontend (`rios-ai-web/`)

### 1️⃣ Instalar dependências

```bash
cd rios-ai-web
npm install
```

### 2️⃣ Rodar servidor Next.js

```bash
npm run dev
```

Acesse:

```
http://localhost:3000
```

---

## ✨ Funcionalidades

- 🔢 Calculadora Inteligente  
- 🌦 Consulta de Clima  
- 💱 Cotação de Moedas  
- ₿ Preço de Criptomoedas  
- 🤖 LLM com Memória Curta  

---

## 🧪 Exemplos

```
Quanto é 12 + 35 * 2?
Qual a temperatura de Uberlândia?
Qual o preço do Bitcoin hoje?
Sou da Artefact, olá!
```

---

## 🚀 Melhorias Futuras

- Streaming no frontend  
- Persistência de conversas  
- Deploy  
- Dashboard administrativo  

---

## 👤 Autor

**Pedro Rios**  
Engenheiro & Desenvolvedor  
Construindo soluções inteligentes com IA 🚀
