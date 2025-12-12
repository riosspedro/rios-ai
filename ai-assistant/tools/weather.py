# tools/weather.py
import re
import unicodedata
import requests
from requests.exceptions import RequestException


def _strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if unicodedata.category(c) != "Mn"
    )


def extract_city(text: str) -> str:
    # tira pontuação e normaliza espaços
    cleaned = re.sub(r"[^\w\s]", " ", text.lower())
    cleaned = " ".join(cleaned.split())
    words = cleaned.split()

    city = None
    if "em" in words:
        idx = words.index("em")
        if idx + 1 < len(words):
            city = words[idx + 1]
    if not city:
        city = words[-1]

    # normaliza para tratar acentos manualmente
    norm = _strip_accents(city)

    mapping = {
        "uberlandia": "Uberlândia",
        # coloca outros mapeamentos se quiser
    }

    return mapping.get(norm, city.capitalize())


def get_weather(text: str) -> str:
    city = extract_city(text)

    try:
        geo = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1},
            timeout=5,
        ).json()
    except RequestException as e:
        return (
            f"Não consegui consultar o clima agora "
            f"(erro de conexão: {e.__class__.__name__})."
        )

    if not geo.get("results"):
        return f"Não encontrei a cidade {city}."

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    try:
        forecast = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current_weather": True,
            },
            timeout=5,
        ).json()
    except RequestException as e:
        return (
            f"Não consegui consultar o clima agora "
            f"(erro de conexão: {e.__class__.__name__})."
        )

    w = forecast.get("current_weather", {})
    temp = w.get("temperature")
    wind = w.get("windspeed")

    if temp is None:
        return f"Não consegui obter a temperatura atual em {city}."

    return f"Tempo em {city}: {temp}°C, vento {wind} km/h."
