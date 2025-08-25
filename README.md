# Biblioteca de Números Complejos - Taller 1

Este proyecto implementa operaciones con números complejos representados como tuplas.
No se utiliza el tipo de datos complex de Python.

## Funciones incluidas

- `suma((a,b), (c,d)) -> (a+c, b+d)`  
- `resta((a,b), (c,d)) -> (a-c, b-d)`  
- `producto((a,b), (c,d)) -> (ac - bd, ad + bc)`  
- `division((a,b), (c,d)) -> ((ac+bd)/(c^2+d^2), (bc-ad)/(c^2+d^2))`  
- `modulo((a,b)) -> |z|`  
- `conjugado((a,b)) -> (a, -b)`  
- `fase((a,b)) -> atan2(b, a)`  
- `cartesiano_a_polar((a,b)) -> (r, theta)`  
- `polar_a_cartesiano((r, theta)) -> (a, b)`

## Instalación local

```bash
git clone <TU_REPO_GITHUB>.git
cd <TU_REPO_GITHUB>
```

## Uso rápido

```python

from numeros_complejos.operaciones_complejas import suma, cartesiano_a_polar

z1 = (3, 4)
z2 = (1, -2)

print(suma(z1, z2))            # (4, 2)
print(cartesiano_a_polar(z1))  # (5.0, 0.927...)
```

## Pruebas unitarias

El proyecto incluye pruebas con `unittest'.
Para ejecutarlas:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## Estructura del proyecto

```text
├── numeros_complejos/
│   └── operaciones_complejas.py   # Biblioteca principal
├── tests/
│   └── test_operaciones_complejas.py   # Pruebas unitarias
├── .gitignore
├── LICENSE
└── README.md

```

## Estilo y decisiones de diseño

- API **funcional**  con anotaciones de tipo y comentarios
- Tolerancia numérica en pruebas con `assertAlmostEqual` donde conviene.
- Corrección en `polar_a_cartesiano` si `r < 0`.
- Verifiación de **división por cero** con `ZeroDivisionError`.

## Licencia

Apache 2.0.  
Eres libre de usarlo, modificarlo y distribuirlo, siempre que se conserve el aviso de copyright y la licencia original.
