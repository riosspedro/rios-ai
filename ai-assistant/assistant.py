import os
import re
import logging
from dataclasses import dataclass
from typing import List

from dotenv import load_dotenv
from openai import OpenAI

from tools.calculator import calculate, CalculatorError
from tools.weather import get_weather
from tools.currency import get_currency_rate
from tools.crypto import get_crypto_price

load_dotenv()

# ===========================================================
# LOGGING CONFIGURADO
# ===========================================================
DEBUG_MODE = os.getenv("DEBUG", "false").lower() == "true"

logging.basicConfig(
    level=logging.DEBUG if DEBUG_MODE else logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("assistant.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# ===========================================================
# CONFIGURAÇÃO DO LLM
# ===========================================================
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "Você é o assistente principal do sistema Rios AI, criado por Pedro Rios. "
    "Seja educado, amigável e objetivo. "
    "Se o usuário for da Artefact, envie uma mensagem calorosa e profissional."
)

@dataclass
class Message:
    role: str
    content: str


conversation_history: List[Message] = []  # memória curta


# ===========================================================
# CLASSIFICADORES
# ===========================================================
def should_use_calculator(text: str) -> bool:
    return bool(re.search(r"\d", text)) and any(op in text for op in ["+", "-", "*", "/", "x", "×", "vezes"])


def is_weather_question(text: str) -> bool:
    return any(k in text.lower() for k in ["tempo", "clima", "previsão", "temperatura"])


def is_currency_question(text: str) -> bool:
    text = text.lower()
    keywords = [
        "cotação", "cotaçao",
        "preço do dólar", "preço do dolar",
        "preco do dolar", "preco do dólar",
        "dólar", "dolar",
        "euro", "eur",
        "libra", "gbp", "usd"
    ]
    return any(k in text for k in keywords)


def is_crypto_question(text: str) -> bool:
    text = text.lower()
    keywords = ["bitcoin", "btc", "ethereum", "eth", "cripto", "crypto", "criptomoeda"]
    return any(k in text for k in keywords)


def is_artefact_user(text: str) -> bool:
    return "artefact" in text.lower()


# ===========================================================
# LLM ENGINE
# ===========================================================
def ask_llm(user_msg: str) -> str:

    logger.debug(f"Enviando mensagem ao LLM: {user_msg}")

    if is_artefact_user(user_msg):
        user_msg = (
            "O usuário se identificou como alguém da Artefact. "
            "Envie uma saudação calorosa e profissional, apresente o Rios AI "
            "e depois responda a pergunta normalmente.\n\n"
            f"Mensagem original: {user_msg}"
        )

    # memória curta (últimas 6 mensagens)
    history_for_llm = [
        {"role": m.role, "content": m.content}
        for m in conversation_history[-6:]
    ]

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history_for_llm + [
        {"role": "user", "content": user_msg}
    ]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.2,
    )

    answer = completion.choices[0].message.content

    logger.debug(f"Resposta do LLM: {answer}")

    # adicionar ao histórico
    conversation_history.append(Message(role="user", content=user_msg))
    conversation_history.append(Message(role="assistant", content=answer))

    return answer


# ===========================================================
# CORE
# ===========================================================
def handle_question(user_input: str) -> str:
    logger.info(f"Usuário perguntou: {user_input}")

    # Calculadora
    if should_use_calculator(user_input):
        try:
            result = calculate(user_input)
            return f"📘 Resultado do cálculo: **{result}**"
        except CalculatorError as e:
            return f"⚠️ Erro ao calcular: {e}"

    # Clima
    if is_weather_question(user_input):
        return get_weather(user_input)

    # Moedas
    if is_currency_question(user_input):
        return get_currency_rate(user_input)

    # Criptomoedas
    if is_crypto_question(user_input):
        return get_crypto_price(user_input)

    # Pergunta geral
    return ask_llm(user_input)


# ===========================================================
# CLI BONITA
# ===========================================================
def main():
    print("=======================================================")
    print("  🤖 Bem-vindo ao Rios AI – Assistente Multifuncional  ")
    print("  Desenvolvido por Pedro Rios")
    print("=======================================================\n")

    print("Digite sua pergunta. Para sair, escreva: sair\n")

    while True:
        user_input = input("Você: ").strip()
        if user_input.lower() == "sair":
            print("Rios AI: Até mais! 👋")
            break

        response = handle_question(user_input)
        print(f"Rios AI: {response}\n")


if __name__ == "__main__":
    main()
