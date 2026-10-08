import tkinter as tk
from tkinter import messagebox
import json
import os


# ============================================================
# VOTOS
# ============================================================

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
    "Nulo": 0
}


# ============================================================
# NÚMERO DOS CANDIDATOS
# ============================================================

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


# ============================================================
# CARREGAR VOTOS SALVOS
# ============================================================

def carregar_votos():
    global votos

    if os.path.exists("votos.json"):
        try:
            with open("votos.json", "r", encoding="utf-8") as arquivo:
                votos_salvos = json.load(arquivo)

            # Atualiza somente os candidatos existentes
            for candidato in votos:
                if candidato in votos_salvos:
                    votos[candidato] = votos_salvos[candidato]

        except (json.JSONDecodeError, OSError):
            messagebox.showwarning(
                "Aviso",
                "Não foi possível carregar os votos salvos.\n"
                "O programa será iniciado com zero votos."
            )


# ============================================================
# SALVAR VOTOS
# ============================================================

def salvar_votos():
    try:
        with open("votos.json", "w", encoding="utf-8") as arquivo:
            json.dump(
                votos,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

    except OSError:
        messagebox.showerror(
            "Erro",
            "Não foi possível salvar os votos."
        )


# ============================================================
# REGISTRAR VOTO
# ============================================================

def votar():
    numero = entrada.get().strip()

    # VOTO PARA CANDIDATO
    if numero in candidatos:

        candidato = candidatos[numero]

        votos[candidato] += 1

        salvar_votos()

        messagebox.showinfo(
            "Urna",
            f"Voto registrado para:\n\n{candidato}"
        )

    # VOTO NULO
    elif numero == "00":

        votos["Nulo"] += 1

        salvar_votos()

        messagebox.showinfo(
            "Urna",
            "Voto nulo registrado!"
        )

    # NÚMERO INVÁLIDO
    else:

        messagebox.showwarning(
            "Número inválido",
            "Esse número não corresponde a nenhum candidato."
        )

    # Limpa o campo
    entrada.delete(0, tk.END)
    entrada.focus()


# ============================================================
# MOSTRAR RESULTADO
# ============================================================

def resultado():
    texto = "RESULTADO DA VOTAÇÃO\n\n"

    for candidato, quantidade in votos.items():
        texto += f"{candidato}: {quantidade} voto(s)\n"

    messagebox.showinfo(
        "Resultado",
        texto
    )


# ============================================================
# CARREGA OS VOTOS ANTES DE INICIAR
# ============================================================

carregar_votos()


# ============================================================
# JANELA PRINCIPAL
# ============================================================

janela = tk.Tk()

janela.title("Urna Digital")
janela.geometry("500x600")
janela.resizable(False, False)


# ============================================================
# TÍTULO
# ============================================================

titulo = tk.Label(
    janela,
    text="🗳️ URNA DIGITAL",
    font=("Arial", 22, "bold")
)

titulo.pack(pady=20)


# ============================================================
# INSTRUÇÃO
# ============================================================

tk.Label(
    janela,
    text="Digite o número do candidato:",
    font=("Arial", 12)
).pack()


# ============================================================
# CAMPO PARA DIGITAR
# ============================================================

entrada = tk.Entry(
    janela,
    font=("Arial", 20),
    justify="center"
)

entrada.pack(pady=10)


# ============================================================
# BOTÃO VOTAR
# ============================================================

tk.Button(
    janela,
    text="VOTAR",
    font=("Arial", 14, "bold"),
    command=votar
).pack(pady=10)


# ============================================================
# LISTA DE CANDIDATOS
# ============================================================

lista_candidatos = """13 - Luiz Inácio Lula da Silva
14 - Renan Santos
16 - Hertz Dias
21 - Edmilson Costa
22 - Flavio Bolsonaro
27 - Clariana Barão
28 - Pablo Marçal
29 - Rui Costa Pimenta
30 - Romeu Zema
35 - Wilson Grassi
55 - Ronaldo Caiado
70 - Augusto Cury
80 - Samara Martins

00 - Voto nulo"""


tk.Label(
    janela,
    text=lista_candidatos,
    font=("Arial", 10),
    justify="left"
).pack(pady=15)


# ============================================================
# INICIA O PROGRAMA
# ============================================================

entrada.focus()

janela.mainloop()

votos.json

{
    "Luiz Inácio Lula da Silva": 3,
    "Renan Santos": 1,
    "Hertz Dias": 0,
    "Edmilson Costa": 0,
    "Flavio Bolsonaro": 2,
    "Clariana Barão": 0,
    "Pablo Marçal": 1,
    "Rui Costa Pimenta": 0,
    "Romeu Zema": 0,
    "Wilson Grassi": 0,
    "Ronaldo Caiado": 0,
    "Augusto Cury": 0,
    "Samara Martins": 0,
    "Nulo": 1
}
