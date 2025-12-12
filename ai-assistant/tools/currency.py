# tools/currency.py
import requests
from requests.exceptions import RequestException


def detect_currency(text: str) -> str | None:
    text = text.lower()
    if "dólar" in text or "dolar" in text or "usd" in text:
        return "USD"
    if "euro" in text or "eur" in text:
        return "EUR"
    if "libra" in text or "gbp" in text:
        return "GBP"
    return None


def get_currency_rate(text: str) -> str:
    currency = detect_currency(text)
    if not currency:
        return "Moeda não reconhecida. Tente: dólar, euro ou libra."

    try:
        resp = requests.get(
            "https://open.er-api.com/v6/latest/USD",
            timeout=5,
        )
        resp.raise_for_status()
        data = resp.json()
    except RequestException as e:
        return (
            "Não consegui consultar a cotação agora "
            f"(erro de conexão: {e.__class__.__name__}). "
            "Tente novamente mais tarde."
        )
    except ValueError:
        return "Erro ao interpretar a resposta da API de câmbio."

    if data.get("result") != "success" or "rates" not in data:
        return "A API de câmbio retornou uma resposta inesperada."

    rates = data["rates"]

    if "BRL" not in rates:
        return "Não encontrei taxa de câmbio para BRL."

    brl = rates["BRL"]

    if currency == "USD":
        return f"1 USD vale aproximadamente R$ {brl:.2f}"

    if currency not in rates:
        return f"Não encontrei a cotação para {currency}."

    base_to_currency = rates[currency]
    value_in_brl = brl / base_to_currency

    return f"1 {currency} vale aproximadamente R$ {value_in_brl:.2f}"
