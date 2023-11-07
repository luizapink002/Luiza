from tkinter import*
from tkinter import ttk as tk

def fechar_tela(tela):
    tela.destroy()

    
def desenha_serviços(tela):

    tela1=Toplevel(tela)
    tela1.title("Tipo de serviços")
    tela1.geometry("900x700")

    texto1=Label(tela1,text="Raio X").place(x=20, y=30)

    entry1 = Entry(tela1, width=50).place(x=20,y=50)

    texto2=Label(tela1,text="Banho e Tosa").place(x=20, y=70)

    entry2 = Entry(tela1, width=50).place(x=20,y=90)

    texto3 = Label(tela1, text="Banho").place(x=20, y=110)

    entry3 = Entry(tela1, width=50).place(x=20,y=130)

    texto4 = Label(tela1, text="Vacina").place(x=20, y=150)

    entry4 = Entry(tela1, width=50).place(x=20,y=170)

    texto5 = Label(tela1, text="Exame de Rotina").place(x=20, y=190)

    entry5 = Entry(tela1, width=50).place(x=20,y=210)

    exit_button= Button(tela1,text="Sair",command=tela1.destroy)
    exit_button.place(x=20,y=250)

