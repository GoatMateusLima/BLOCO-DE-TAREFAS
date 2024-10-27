#bibliotecas
from tkinter import *
import tkinter as tk
from tkinter import ttk, font, messagebox, PhotoImage
from tkinter import PhotoImage 
import os

#cores usadas
co1 = '#f0f0f0'
co2 = '#000'
co3 = '#e33207'
co4 = '#059540'

#tamanho da pagina e nome
janela = tk.Tk()
janela.title("App de Tarefas")
janela.configure(bg=co1)
janela.geometry('500x600')

#logo
caminho_icon = os.path.join('IMG', 'favicon.ico')
janela.iconbitmap(caminho_icon)

#logo do cabecalho
caminho_img = os.path.join('IMG', 'favicon-32x32.png')
img = PhotoImage(file = caminho_img)

#titulo da pagina
fonte_cabecalho = font.Font(family="Garamond", size=24, weight="bold")
rotulo_cabecalho = tk.Label(janela, text="Meu App de Tarefas",padx=610,font=fonte_cabecalho, bg=co3, fg=co1).pack(pady=20)

#funcao adicionar tarefa
frame_em_edicao = None

#Barra onde ira receber o texto(input)
frame = tk.Frame(janela, bg=co2).pack(pady=10)
entrada_tarefa = tk.Entry(frame, font=('Garamond', 14), relief= tk.FLAT, bg='white', fg=co4, width=30)
entrada_tarefa.pack(side=tk.LEFT, padx=10)

#botao de clicar para adiconar a lista
botao_adicionar = tk.Button(frame, text='Adicionar Tarefa', bg=co4, fg=co1, height=1, width=15, font=('Roboto',11),relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)

#criando frame da lista de tarefas com rolagem
frame_lista_tarefa = tk.Frame(janela, bg='white')
frame_lista_tarefa.pack(fill=tk.BOTH,expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_lista_tarefa, bg='white')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame_lista_tarefa,orient='vertical', command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas_interior = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=canvas_interior, anchor="nw")
canvas_interior.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))




janela.mainloop()