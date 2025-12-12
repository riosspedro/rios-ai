import re
import math

class CalculatorError(Exception):
    pass

def clean_expression(expr: str) -> str:
    """
    Extrai apenas a expressão matemática.
    Ex: 'Quanto é 12 + 35 * 2?' -> '12 + 35 * 2'
    """

    # converte “x” ou “×” para *
    expr = expr.replace("x", "*").replace("×", "*")

    # converte ^ para ** (potência)
    expr = expr.replace("^", "**")

    # pega somente caracteres permitidos: números, operadores e parênteses
    cleaned = re.findall(r"[0-9+\-*/().**]+", expr)

    if not cleaned:
        raise CalculatorError("Nenhuma expressão matemática encontrada.")

    return "".join(cleaned)


def calculate(expression: str) -> float:
    """
    Calcula expressão matemática de forma segura.
    """

    expr = clean_expression(expression)

    # valida operadores permitidos
    if not re.fullmatch(r"[0-9+\-*/().* ]+", expr):
        raise CalculatorError("Expressão contém caracteres inválidos.")

    try:
        return eval(expr, {"__builtins__": {}}, math.__dict__)
    except Exception:
        raise CalculatorError("Expressão inválida.")
