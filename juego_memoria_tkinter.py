import random
import tkinter as tk
from tkinter import messagebox


class JuegoMemoria:
    def __init__(self, root, filas=4, columnas=4):
        if (filas * columnas) % 2 != 0:
            raise ValueError("La cantidad de cartas debe ser par.")

        self.root = root
        self.root.title("Juego de Memoria Visual - Emojis")
        self.root.resizable(False, False)

        self.filas = filas
        self.columnas = columnas
        self.total_pares = (filas * columnas) // 2

        self.intentos = 0
        self.pares_encontrados = 0
        self.primera_carta = None
        self.segunda_carta = None
        self.bloqueado = False

        self.tablero = []
        self.botones = []
        self.emojis_disponibles = [
            "🐶",
            "🐱",
            "🦊",
            "🐼",
            "🐵",
            "🦁",
            "🐸",
            "🐯",
            "🐨",
            "🐰",
            "🐮",
            "🦄",
            "🐙",
            "🦋",
            "🐢",
            "🐧",
            "🐠",
            "🦖",
            "🍎",
            "🍕",
        ]

        self.frame_superior = tk.Frame(self.root, padx=10, pady=10)
        self.frame_superior.pack()

        self.label_intentos = tk.Label(
            self.frame_superior,
            text="Intentos: 0",
            font=("Segoe UI", 12, "bold"),
        )
        self.label_intentos.pack(side=tk.LEFT, padx=(0, 12))

        self.boton_reiniciar = tk.Button(
            self.frame_superior,
            text="Reiniciar",
            command=self.reiniciar_juego,
            width=12,
        )
        self.boton_reiniciar.pack(side=tk.LEFT)

        self.frame_tablero = tk.Frame(self.root, padx=10, pady=10)
        self.frame_tablero.pack()

        self.crear_tablero()

    def crear_tablero(self):
        if self.total_pares > len(self.emojis_disponibles):
            raise ValueError("No hay suficientes emojis para el tamano del tablero.")

        valores_base = random.sample(self.emojis_disponibles, self.total_pares)
        valores = valores_base * 2
        random.shuffle(valores)
        self.tablero = valores

        self.botones = []
        for i in range(self.filas):
            fila_botones = []
            for j in range(self.columnas):
                indice = i * self.columnas + j
                boton = tk.Button(
                    self.frame_tablero,
                    text="?",
                    width=6,
                    height=3,
                    font=("Segoe UI Emoji", 16),
                    command=lambda idx=indice: self.voltear_carta(idx),
                )
                boton.grid(row=i, column=j, padx=4, pady=4)
                fila_botones.append(boton)
            self.botones.append(fila_botones)

    def obtener_boton(self, indice):
        fila = indice // self.columnas
        columna = indice % self.columnas
        return self.botones[fila][columna]

    def voltear_carta(self, indice):
        if self.bloqueado:
            return

        boton = self.obtener_boton(indice)

        # Evita reabrir cartas ya reveladas o la misma carta.
        if str(boton["state"]) == "disabled" or boton["text"] != "?":
            return

        valor = self.tablero[indice]
        boton.config(text=valor, bg="#dff6dd")

        if self.primera_carta is None:
            self.primera_carta = indice
            return

        self.segunda_carta = indice
        self.intentos += 1
        self.label_intentos.config(text=f"Intentos: {self.intentos}")
        self.bloqueado = True
        self.root.after(700, self.comprobar_coincidencia)

    def comprobar_coincidencia(self):
        idx1 = self.primera_carta
        idx2 = self.segunda_carta

        boton1 = self.obtener_boton(idx1)
        boton2 = self.obtener_boton(idx2)

        if self.tablero[idx1] == self.tablero[idx2]:
            boton1.config(state=tk.DISABLED, disabledforeground="#0a7f2e", bg="#b5e7a0")
            boton2.config(state=tk.DISABLED, disabledforeground="#0a7f2e", bg="#b5e7a0")
            self.pares_encontrados += 1

            if self.pares_encontrados == self.total_pares:
                messagebox.showinfo(
                    "¡Ganaste!",
                    f"Encontraste todos los pares en {self.intentos} intentos.",
                )
        else:
            boton1.config(text="?", bg="SystemButtonFace")
            boton2.config(text="?", bg="SystemButtonFace")

        self.primera_carta = None
        self.segunda_carta = None
        self.bloqueado = False

    def reiniciar_juego(self):
        self.intentos = 0
        self.pares_encontrados = 0
        self.primera_carta = None
        self.segunda_carta = None
        self.bloqueado = False
        self.label_intentos.config(text="Intentos: 0")

        valores_base = random.sample(self.emojis_disponibles, self.total_pares)
        valores = valores_base * 2
        random.shuffle(valores)
        self.tablero = valores

        for indice in range(self.filas * self.columnas):
            boton = self.obtener_boton(indice)
            boton.config(text="?", state=tk.NORMAL, bg="SystemButtonFace")


def main():
    root = tk.Tk()
    JuegoMemoria(root, filas=4, columnas=4)
    root.mainloop()


if __name__ == "__main__":
    main()
