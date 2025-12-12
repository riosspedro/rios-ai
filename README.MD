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

```txt
rios-ai/
│
├── README.md               <-- Arquivo principal de documentação
│
├── ai-assistant/           <-- Backend Python (FastAPI)
│   ├── assistant.py        <-- Lógica: LLM + ferramentas
│   ├── server.py           <-- API /chat
│   ├── tools/
│   │   ├── calculator.py
│   │   ├── currency.py
│   │   ├── crypto.py
│   │   └── weather.py
│   └── requirements.txt
│
└── rios-ai-web/            <-- Frontend Next.js
    ├── app/
    │   ├── page.tsx
    │   └── api/chat/route.ts
    └── package.json
Fluxo da aplicação:
O usuário envia uma mensagem pelo frontend.

O Next.js envia a mensagem para /api/chat.

A rota repassa a mensagem para o backend Python.

O backend decide se usa:

Calculadora

Clima

Moedas

Criptos

Ou o LLM

A resposta é exibida no chat.

⚙️ Instalação – Backend (ai-assistant/)
1. Criar o ambiente virtual
Bash

cd ai-assistant
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
2. Instalar dependências
Bash

pip install -r requirements.txt
3. Configurar variáveis de ambiente
Crie um arquivo .env na raiz da pasta ai-assistant:

Snippet de código

OPENAI_API_KEY=sua_chave_aqui
DEBUG=true
4. Executar API FastAPI
Bash

uvicorn server:app --reload --host 127.0.0.1 --port 8000
Endpoint principal: POST http://127.0.0.1:8000/chat

🎨 Instalação – Frontend (rios-ai-web/)
1. Instalar pacotes
Bash

cd rios-ai-web
npm install
2. Iniciar o servidor
Bash

npm run dev
Acesse o projeto em: http://localhost:3000

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
Memória curta (últimas 6 mensagens).

Saudações especiais quando o usuário menciona “Artefact”.

Modelo utilizado: gpt-4o-mini.

🧪 Exemplos de Perguntas (Prompts)
“Quanto é 12 + 35 * 2?”

“Qual o preço do Bitcoin hoje?”

“Qual a cotação do dólar?”

“Qual a temperatura de Uberlândia?”

“Sou da Artefact, olá!”

🚀 Melhorias Futuras
[ ] Streaming de resposta no frontend

[ ] Histórico persistente (Banco de dados)

[ ] Deploy (Vercel + Railway/Render)

[ ] Painel administrativo

👤 Autor
Pedro Rios Desenvolvedor e Engenheiro Construindo soluções inteligentes com IA 🚀
