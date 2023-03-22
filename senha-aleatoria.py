import random
import string
import tkinter as tk

def gerar_senha():
    # Comprimento da senha
    comprimento = comprimento_var.get()

    # Caracteres para incluir na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Gera a senha
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))

    # Exibe a senha na interface gráfica
    senha_var.set(senha)

# Janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")

# Caixa de entrada para o comprimento da senha
comprimento_label = tk.Label(janela, text="Comprimento:")
comprimento_label.grid(row=0, column=0, padx=5, pady=5)
comprimento_var = tk.IntVar(value=8)
comprimento_entry = tk.Entry(janela, textvariable=comprimento_var)
comprimento_entry.grid(row=0, column=1, padx=5, pady=5)

# Cria botão para gerar senha
gerar_senha_button = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
gerar_senha_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Caixa de texto para exibir a senha gerada
senha_label = tk.Label(janela, text="Senha:")
senha_label.grid(row=2, column=0, padx=5, pady=5)
senha_var = tk.StringVar()
senha_entry = tk.Entry(janela, textvariable=senha_var, state="readonly")
senha_entry.grid(row=2, column=1, padx=5, pady=5)

# Inicia o loop principal da janela
janela.mainloop()
