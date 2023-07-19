import math


def get_equation_roots(a: float, b: float, c: float) -> tuple:
    """Получить корни квадратного уравнения."""
    discriminant: float = (b * b) - (4 * a * c)

    if discriminant < 0:
        return None, None
    if discriminant == 0:
        x: float = -b / (2 * a)
        return x, x
    if discriminant > 0:
        x1: float = (-b + math.sqrt(discriminant)) / (2 * a)
        x2: float = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
