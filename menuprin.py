import tkinter as tk
from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('pet_shop.db')

class Animal(Model):
    nome = CharField()
    especie = CharField()
    idade = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Animal], safe=True)


def adicionar_animal():
    nome = entry_nome.get()
    especie = entry_especie.get()
    idade = entry_idade.get()
    
    Animal.create(nome=nome, especie=especie, idade=idade)
    
    
    entry_nome.delete(0, tk.END)
    entry_especie.delete(0, tk.END)
    entry_idade.delete(0, tk.END)


def listar_animais():
    lista_animais.delete(0, tk.END)
    for animal in Animal.select():
        lista_animais.insert(tk.END, f"{animal.nome} - {animal.especie} - {animal.idade} anos")


def remover_animal():
    selecao = lista_animais.curselection()
    if selecao:
        indice = selecao[0]
        texto_animal = lista_animais.get(indice)
        nome_animal = texto_animal.split(" - ")[0]
        Animal.delete().where(Animal.nome == nome_animal).execute()
        listar_animais()


root = tk.Tk()
root.title("Pet Shop")


entry_nome = tk.Entry(root, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=5)
entry_especie = tk.Entry(root, width=30)
entry_especie.grid(row=1, column=1, padx=10, pady=5)
entry_idade = tk.Entry(root, width=30)
entry_idade.grid(row=2, column=1, padx=10, pady=5)


label_nome = tk.Label(root, text="Nome do Animal:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
label_especie = tk.Label(root, text="Espécie:")
label_especie.grid(row=1, column=0, padx=10, pady=5)
label_idade = tk.Label(root, text="Idade:")
label_idade.grid(row=2, column=0, padx=10, pady=5)


btn_adicionar = tk.Button(root, text="Adicionar Animal", command=adicionar_animal)
btn_adicionar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
btn_listar = tk.Button(root, text="Listar Animais", command=listar_animais)
btn_listar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
btn_remover = tk.Button(root, text="Remover Animal Selecionado", command=remover_animal)
btn_remover.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


lista_animais = tk.Listbox(root, height=10, width=50)
lista_animais.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
