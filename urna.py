import tkinter as tk
from tkinter import messagebox

votos = {
    "Luiz Inácio Lula da Silva": 13,
    "Renan Santos": 14,
    "Hertz Dias": 16,
    "Edmilson Costa": 21,
    "Flavio Bolsonaro": 22,
    "Clariana Barão": 27,
    "Pablo Marçal": 28,
    "Rui Costa Pimenta": 29,
    "Romeu Zema": 30,
    "Wilson Grassi": 35,
    "Ronaldo Caiado": 55,
    "Augusto Cury": 70,
    "Samara Martins": 80,
    "Branco": 0,
    "Nulo": 0
}

def votar():
    numero = entrada.get()

    if numero == "13":
        votos["Luiz Inácio Lula da Silva"] += 13
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "14":
        votos["Renan Santos"] += 14
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "16":
        votos["Hertz Dias"] += 16
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "21":
        votos["Edmilson Costa"] += 21
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "21":
        votos["Flavio Bolsonaro"] += 22
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "27":
        votos["Clariana Barão"] += 27
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "28":
        votos["Pablo Marçal"] += 28
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "29":
        votos["Rui Costa Pimenta"] += 29
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "30":
        votos["Romeu Zema"] += 30
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "35":
        votos["Wilson Grassi"] += 35
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "55":
        votos["Ronaldo Caiado"] += 55
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "70":
        votos["Augusto Cury"] += 70
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "80":
        votos["Samara Martins"] += 80
        messagebox.showinfo("Urna", "Voto registrado!")
    elif numero == "0":
        votos["Branco"] += 1
        messagebox.showinfo("Urna", "Voto em branco registrado!")
    else:
        votos["Nulo"] += 1
        messagebox.showinfo("Urna", "Voto nulo registrado!")

    entrada.delete(0, tk.END)


def resultado():
    texto = "RESULTADO DA VOTAÇÃO\n\n"

    for candidato, quantidade in votos.items():
        texto += f"{candidato}: {quantidade} voto(s)\n"

    messagebox.showinfo("Resultado", texto)


janela = tk.Tk()
janela.title("Urna Digital")
janela.geometry("500x600")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="🗳️ URNA DIGITAL",
    font=("Arial", 22, "bold")
)
titulo.pack(pady=20)

tk.Label(
    janela,
    text="Digite o número do candidato:",
    font=("Arial", 12)
).pack()

entrada = tk.Entry(
    janela,
    font=("Arial", 20),
    justify="center"
)
entrada.pack(pady=10)

tk.Button(
    janela,
    text="VOTAR",
    font=("Arial", 14, "bold"),
    command=votar
).pack(pady=10)

tk.Button(
    janela,
    text="VER RESULTADO",
    font=("Arial", 12),
    command=resultado
).pack(pady=10)


tk.Label(
    janela,
    text="""13 - Luiz Inácio Lula da Silva
14 - Renan Santos
16 - Hertz Dias
21 - Edmilson Costa
22 - Flávio Bolsonaro
25 - Wilson Grassi
27 - Clariana Barão
29 - Rui Costa Pimenta
30 - Romeu Zema
55 - Ronaldo Caiado
70 - Augusto Cury
80 - Samara Martins
00 - Voto em branco""",
    font=("Arial", 10)
).pack(pady=10)


janela.mainloop()