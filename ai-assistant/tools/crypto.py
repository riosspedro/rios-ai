# tools/crypto.py
import requests
from requests.exceptions import RequestException


def detect_crypto(text: str) -> str | None:
    text = text.lower()
    if "bitcoin" in text or "btc" in text:
        return "bitcoin"
    if "ethereum" in text or "eth" in text:
        return "ethereum"
    return None


def get_crypto_price(text: str) -> str:
    crypto = detect_crypto(text)
    if not crypto:
        return "Criptomoeda não reconhecida. Ex: Bitcoin ou Ethereum."

    try:
        data = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": crypto, "vs_currencies": "usd,brl"},
            timeout=5,
        ).json()
    except RequestException as e:
        return (
            "Não consegui consultar o preço das criptos agora "
            f"(erro de conexão: {e.__class__.__name__})."
        )

    if crypto not in data:
        return "Não encontrei dados para essa criptomoeda."

    usd = data[crypto].get("usd")
    brl = data[crypto].get("brl")

    return f"{crypto.capitalize()} hoje:\nUSD: ${usd}\nBRL: R$ {brl}"
