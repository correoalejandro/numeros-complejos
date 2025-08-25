"""
Biblioteca de operaciones con números complejos representados como tuplas (a, b).
- Representación cartesiana: (real, imag)
- Representación polar: (r, theta) con r >= 0 y theta en radianes
No se utiliza el tipo de datos complex de Python.
Se utilizan las bibliotecas typing y math.
"""


from typing import Tuple
import math

# Tipos
Cartesiano = Tuple[float, float]
Polar = Tuple[float, float]

# ----------------------- Operaciones básicas -----------------------

def suma(z1: Cartesiano, z2: Cartesiano) -> Cartesiano:
    """Suma de complejos: (a, b) + (c, d) = (a+c, b+d)"""
    a, b = z1
    c, d = z2
    return (a + c, b + d)

def resta(z1: Cartesiano, z2: Cartesiano) -> Cartesiano:
    """Resta de complejos: (a, b) - (c, d) = (a-c, b-d)"""
    a, b = z1
    c, d = z2
    return (a - c, b - d)

def producto(z1: Cartesiano, z2: Cartesiano) -> Cartesiano:
    """Producto de complejos: (a, b)*(c, d) = (ac - bd, ad + bc)"""
    a, b = z1
    c, d = z2
    return (a * c - b * d, a * d + b * c)

def division(z1: Cartesiano, z2: Cartesiano) -> Cartesiano:
    """División de complejos: (a, b)/(c, d) = ((ac+bd)/(c^2+d^2), (bc - ad)/(c^2+d^2))"""
    a, b = z1
    c, d = z2
    denom = c * c + d * d
    if denom == 0.0:
        raise ZeroDivisionError("No se puede dividir por 0 + 0i.")
    return ((a * c + b * d) / denom, (b * c - a * d) / denom)

def modulo(z: Cartesiano) -> float:
    """Módulo: |a+bi| = sqrt(a^2 + b^2)"""
    a, b = z
    return math.hypot(a, b)

def conjugado(z: Cartesiano) -> Cartesiano:
    """Conjugado: conj(a, b) = (a, -b)"""
    a, b = z
    return (a, -b)

def fase(z: Cartesiano) -> float:
    """Fase (argumento) en radianes: atan2(b, a). Para (0,0) se retorna 0.0 por convención."""
    a, b = z
    if a == 0.0 and b == 0.0:
        return 0.0
    return math.atan2(b, a)

# ----------------------- Conversiones -----------------------

def cartesiano_a_polar(z: Cartesiano) -> Polar:
    """Convierte (a,b) -> (r, theta). Con r >= 0 y theta en [-pi, pi]."""
    a, b = z
    r = modulo((a, b))
    theta = 0.0 if r == 0.0 else math.atan2(b, a)
    return (r, theta)

def polar_a_cartesiano(p: Polar) -> Cartesiano:
    """Convierte (r, theta) -> (a, b). Acepta r >= 0 y theta en radianes."""
    r, theta = float(p[0]), float(p[1])
    if r < 0:
        # Corregimos: (-r, theta) == (r, theta + pi)
        r = abs(r)
        theta = theta + math.pi
    a = r * math.cos(theta)
    b = r * math.sin(theta)
    
    return (a, b)

# ----------------------- API pública -----------------------

__all__ = [
    "Cartesiano",
    "Polar",
    "suma",
    "resta",
    "producto",
    "division",
    "modulo",
    "conjugado",
    "fase",
    "cartesiano_a_polar",
    "polar_a_cartesiano",
]