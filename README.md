# Memorytest — Juego de memoria visual

Juego de cartas con **Python** y **Tkinter**: cuadrícula boca abajo, al hacer clic se revelan; si coinciden quedan visibles, si no se vuelven a ocultar. Incluye contador de intentos, emojis y botón para reiniciar.

## Requisitos

- **Python 3** (en Windows suele venir `tkinter` incluido con el instalador oficial).
- Si al ejecutar fallara por falta de Tk, en algunas distribuciones Linux: `sudo apt install python3-tk` (o el equivalente de tu sistema).

## Cómo ejecutarlo

Desde la carpeta del proyecto:

```bash
python juego_memoria_tkinter.py
```

O con la ruta completa al archivo.

## Controles

- Clic en una carta para voltearla.
- Tras voltear dos, si no coinciden se ocultan tras un breve tiempo.
- **Reiniciar** baraja de nuevo y pone el contador de intentos en cero.

## Estructura

```
juego-memoria-tkinter/
├── juego_memoria_tkinter.py
├── README.md
└── .gitignore
```

## Licencia

Uso libre para aprendizaje y proyectos personales.
