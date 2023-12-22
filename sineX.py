import re
import math

def evaluate(expression):
    expression = str(expression)
    if expression.__contains__("^"):
        expression = expression.replace("^", "**")
    if expression.__contains__("√"):
        expression = replacer(expression)
    if expression.__contains__("!"):
        expression = replacer(expression)
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"


def replacer(expression):
    def sqrt_replace(match):
        number = match.group(1)
        return f"math.sqrt({number})"

    def fact_replace(match):
        number = match.group(1)
        return f"math.factorial({number})"

    if expression.__contains__("√"):
        pattern = r'√(\d+)'
        replaced_expression = re.sub(pattern, sqrt_replace, expression)
    if expression.__contains__("!"):
        pattern = r'(\d+)!'
        replaced_expression = re.sub(pattern, fact_replace, expression)
    return replaced_expression
