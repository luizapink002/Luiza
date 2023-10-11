from tkinter import *
from tkinter import ttk as tk

def fechartela(tela):



    def desenha_animais(tela):
        tela1=Toplevel(tela) 
        tela1.title("cadastro de animais")
        tela1.geometry("900x700")

        texto1 = Label(tela1,text="nome do dono").place(x=20,y=30)

        entry1 = Entry(tela1,width=50).place(x=20,y=50)

        texto2 = Label(tela1,text="raça").place(x=20,y=70)

        entry2 = Entry(tela1,width=50).place(x=20,y=90)

        texto3 = Label(tela1, text="porte").place(x=20,y=130)

        entry3 = Entry(tela1,width=50).place(x=20,y=130)  

        texto4 = Label(tela1, text="problema encontrado").place(x=20,y=170)

        entry4 = Entry(tela1, width=50).place(x=20,y=170)

        exit_button= Button(tela1,text="Sair",command=tela1.destroy)
        exit_button.place(x=20,y=190)    

