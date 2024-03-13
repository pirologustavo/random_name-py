import random
from tkinter import *

def sortear_nome():
    random_name = []
    name = ["Rafaela", "Pitura", "Lucas"]
    while len(random_name) <= 6:
        lucky_name = (random.choice(name))
        random_name.append(lucky_name)   

    sorteio = random.choice(random_name)
    texto_sorteio["text"] = sorteio

janela = Tk()
janela.iconbitmap('D:/DSUsers/uig09733/OneDrive - Continental AG/Área de Trabalho/random-py/baixados.ico')
janela.title("Continental - Random Name")
janela.geometry("350x250")

texto = Label(janela, text="Continental")
texto.grid(column=5, row=0, pady=10)

botao = Button(janela, text="Sortear nome", command=sortear_nome)
botao.grid(column=5, row=1, padx=130, pady=10)

texto_sorteio = Label(janela, text="")
texto_sorteio.grid(column=5, row=2, pady=10)
janela.mainloop()

    