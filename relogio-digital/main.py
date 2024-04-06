from tkinter import NW, Tk, Label
import tkinter
from datetime import datetime

cor1 = "#333333" #preta
cor2 = "#fafcff" #branca
cor3 = "#3080f0" #azul

fundo = cor1
cor_numero1 = cor3
cor_numero2 = cor2

janela = Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width = False, height= False)
janela.configure(bg=cor1)


def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")

    label1.config(text= hora)
    label1.after(200, relogio)
    label2.config(text = dia_semana + " " + str(dia) + " / " + str(mes)  + "/" + str(ano))
 
label1 = Label(janela, text="", font = ("Arial 80"),  bg = (fundo), fg = cor_numero1)
label1.grid(row = 0, column = 0, sticky = NW, padx = 5)

label2 = Label(janela, text="", font = ("Arial 20"),  bg = (fundo), fg = cor_numero2)
label2.grid(row = 1, column = 0, sticky = NW, padx = 5)


relogio()
janela.mainloop()