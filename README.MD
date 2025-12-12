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

# ⚙️ Instalação – Backend (`ai-assistant/`)

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

# 🎨 Instalação – Frontend (`rios-ai-web/`)

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

# 🔎 Lógica de Implementação

A implementação segue uma arquitetura simples, clara e modular — alinhada ao pedido do desafio (“resolver da forma mais simples possível”), mas com estrutura profissional.

### ✔️ 1. Classificação da mensagem  
O assistente analisa cada entrada e decide qual ferramenta usar:

- Expressões matemáticas → calculadora  
- Palavras de clima → consulta de tempo  
- Termos relacionados a moedas → câmbio  
- Termos de criptomoedas → preços de cripto  
- Se nada se aplica → LLM

### ✔️ 2. Orquestração modular  
Cada ferramenta possui seu próprio módulo em `tools/`, permitindo expansão sem complexidade adicional.

### ✔️ 3. LLM como fallback  
O modelo `gpt-4o-mini` assume as respostas quando nenhuma ferramenta é acionada, com:

- Memória curta (últimas 6 mensagens)  
- Saudações especiais para usuários Artefact  
- Logging avançado para depuração  

### ✔️ 4. Frontend minimalista  
A UI é construída com Next.js para clareza, simplicidade e foco na experiência do avaliador.

---

# 🎓 O que Aprendi

- Arquitetura full-stack aplicada a IA  
- Orquestração de ferramentas com LLMs  
- Design modular e sustentável  
- Integração Python ↔ Next.js  
- Tratamento de erros e logging profissional  
- Comunicação entre frontend → API → backend  

---

# 🔧 O que Eu Faria Diferente com Mais Tempo

- Streaming de tokens no frontend  
- Melhorar detecção de intenções com modelo local  
- Persistência de conversas em banco de dados  
- Deploy completo usando Vercel + Railway  
- Testes unitários para cada módulo  
- Dashboard administrativo e monitoramento  

---

# 🧪 Exemplos

```
Quanto é 12 + 35 * 2?
Qual a temperatura de Uberlândia?
Qual o preço do Bitcoin hoje?
Sou da Artefact, olá!
```

---

# 👤 Autor

**Pedro Rios**  
Engenheiro & Desenvolvedor  
Construindo soluções inteligentes com IA 🚀
