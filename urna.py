import tkinter as tk
from tkinter import messagebox

# Todos começam com ZERO votos
votos = {
    "Luiz Inácio Lula da Silva": 0,
    "Renan Santos": 0,
    "Hertz Dias": 0,
    "Edmilson Costa": 0,
    "Flavio Bolsonaro": 0,
    "Clariana Barão": 0,
    "Pablo Marçal": 0,
    "Rui Costa Pimenta": 0,
    "Romeu Zema": 0,
    "Wilson Grassi": 0,
    "Ronaldo Caiado": 0,
    "Augusto Cury": 0,
    "Samara Martins": 0,
    "Branco": 0,
    "Nulo": 0
}

# Relaciona o número ao nome do candidato
candidatos = {
    "13": "Luiz Inácio Lula da Silva",
    "14": "Renan Santos",
    "16": "Hertz Dias",
    "21": "Edmilson Costa",
    "22": "Flavio Bolsonaro",
    "27": "Clariana Barão",
    "28": "Pablo Marçal",
    "29": "Rui Costa Pimenta",
    "30": "Romeu Zema",
    "35": "Wilson Grassi",
    "55": "Ronaldo Caiado",
    "70": "Augusto Cury",
    "80": "Samara Martins"
}


def votar():
    numero = entrada.get().strip()

    # Verifica se é candidato
    if numero in candidatos:
        candidato = candidatos[numero]
        votos[candidato] += 1

        messagebox.showinfo(
            "Urna",
            f"Voto registrado para:\n{candidato}"
        )

    # Voto em branco
    elif numero == "0" or numero == "00":
        votos["Branco"] += 1

        messagebox.showinfo(
            "Urna",
            "Voto em branco registrado!"
        )

    # Voto nulo
    else:
        votos["Nulo"] += 1

        messagebox.showinfo(
            "Urna",
            "Voto nulo registrado!"
        )

    # Limpa o campo depois do voto
    entrada.delete(0, tk.END)


def resultado():
    texto = "RESULTADO DA VOTAÇÃO\n\n"

    for candidato, quantidade in votos.items():
        texto += f"{candidato}: {quantidade} voto(s)\n"

    messagebox.showinfo("Resultado", texto)


# Janela principal
janela = tk.Tk()
janela.title("Urna Digital")
janela.geometry("500x600")
janela.resizable(False, False)


# Título
titulo = tk.Label(
    janela,
    text="🗳️ URNA DIGITAL",
    font=("Arial", 22, "bold")
)
titulo.pack(pady=20)


# Instrução
tk.Label(
    janela,
    text="Digite o número do candidato:",
    font=("Arial", 12)
).pack()


# Campo para digitar o número
entrada = tk.Entry(
    janela,
    font=("Arial", 20),
    justify="center"
)
entrada.pack(pady=10)


# Botão votar
tk.Button(
    janela,
    text="VOTAR",
    font=("Arial", 14, "bold"),
    command=votar
).pack(pady=10)


# Botão resultado
tk.Button(
    janela,
    text="VER RESULTADO",
    font=("Arial", 12),
    command=resultado
).pack(pady=10)


# Lista de candidatos
tk.Label(
    janela,
    text="""13 - Luiz Inácio Lula da Silva
14 - Renan Santos
16 - Hertz Dias
21 - Edmilson Costa
22 - Flávio Bolsonaro
27 - Clariana Barão
28 - Pablo Marçal
29 - Rui Costa Pimenta
30 - Romeu Zema
35 - Wilson Grassi
55 - Ronaldo Caiado
70 - Augusto Cury
80 - Samara Martins
00 - Voto em branco""",
    font=("Arial", 10)
).pack(pady=10)


# Inicia o programa
janela.mainloop()
