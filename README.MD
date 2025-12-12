# Rios AI – Artefact Edition

Rios AI é um assistente de IA full-stack desenvolvido como parte do desafio técnico para a vaga de **AI Engineer Júnior**.  

O sistema combina um backend em Python com FastAPI e um frontend em Next.js, integrando modelos de linguagem (LLMs) com ferramentas externas reais, como:

- 🔢 **Calculadora inteligente**
- 💱 **Cotação de moedas**
- ₿ **Preço de criptomoedas**
- 🌦 **Consulta de clima**
- 🤖 **LLM com memória curta e saudação especial para usuários da Artefact**

---

## 📁 Arquitetura do Projeto

rios-ai/
│ README.md <-- Arquivo principal de documentação
│
├─ ai-assistant/ <-- Backend Python (FastAPI)
│ ├─ assistant.py <-- Lógica: LLM + ferramentas
│ ├─ server.py <-- API /chat
│ ├─ tools/
│ │ ├─ calculator.py
│ │ ├─ currency.py
│ │ ├─ crypto.py
│ │ └─ weather.py
│ └─ requirements.txt
│
└─ rios-ai-web/ <-- Frontend Next.js
├─ app/
│ ├─ page.tsx
│ └─ api/chat/route.ts
├─ package.json
└─ ...

yaml
Copiar código

Fluxo da aplicação:

1. O usuário envia uma mensagem pelo frontend.
2. O Next.js envia a mensagem para `/api/chat`.
3. A rota repassa a mensagem para o backend Python.
4. O backend decide se usa:
   - Calculadora  
   - Clima  
   - Moedas  
   - Criptos  
   - Ou o LLM
5. A resposta é exibida no chat.

---

## ⚙️ Instalação – Backend (`ai-assistant/`)

### 1. Criar o ambiente virtual
```bash
cd ai-assistant
python -m venv .venv
.\.venv\Scripts\activate   # Windows
2. Instalar dependências
bash
Copiar código
pip install -r requirements.txt
3. Criar arquivo .env
env
Copiar código
OPENAI_API_KEY=xxxxxx
DEBUG=true
4. Executar API FastAPI
bash
Copiar código
uvicorn server:app --reload --host 127.0.0.1 --port 8000
Endpoint principal:
POST http://127.0.0.1:8000/chat

🎨 Instalação – Frontend (rios-ai-web/)
1. Instalar pacotes
bash
Copiar código
cd rios-ai-web
npm install
2. Iniciar o servidor
bash
Copiar código
npm run dev
Acesse em:

arduino
Copiar código
http://localhost:3000
✨ Funcionalidades Implementadas
🔢 Calculadora Inteligente
Interpreta expressões dentro de frases.

Suporta multiplicação, potência, “x/×”, "^", etc.

Parser seguro.

🌦 Clima
Consulta temperatura e condições de qualquer cidade.

💱 Moedas
Cotação atualizada de USD, EUR, GBP.

₿ Criptomoedas
Preço do Bitcoin e Ethereum.

🧠 LLM
Memória curta (últimas 6 mensagens)

Saudações especiais quando o usuário menciona “Artefact”

Modelo utilizado: gpt-4o-mini

🧪 Exemplos de Perguntas
“Quanto é 12 + 35 * 2?”

“Qual o preço do Bitcoin hoje?”

“Qual a cotação do dólar?”

“Qual a temperatura de Uberlândia?”

“Sou da Artefact, olá!”

🚀 Melhorias Futuras
Streaming no frontend

Histórico persistente

Deploy (Vercel + Railway)

Painel administrativo

👤 Autor
Pedro Rios
Desenvolvedor e Engenheiro
Construindo soluções inteligentes com IA 🚀