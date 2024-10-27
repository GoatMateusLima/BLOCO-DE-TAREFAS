#bibliotecas
from tkinter import *
import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage 
from PIL import Image, ImageTk #biblioteca que suporta varias imagens
import os #biblioteca usada para colocar a logo do programa

#cores usadas
co1 = '#f0f0f0'
co2 = '#000'
co3 = '#e33207'
co4 = '#059540'
co5 = '#034c7c'

#cria janela e adiciona tamanho da pagina e nome
janela = tk.Tk()
janela.title("App de Tarefas")
janela.configure(bg=co1)
janela.geometry('500x600')

#logo
caminho_icon = os.path.join('IMG', 'favicon.ico')
janela.iconbitmap(caminho_icon)


#imagem de fundo
#tive que usar uma biblioteca especifica para usar todos os tipos de imagem
caminho_img = os.path.join('icon', 'fundo.jpg')
img_original = Image.open(caminho_img) # vai carregar a imagem
img = ImageTk.PhotoImage(img_original) # converte para ImageTk

#aqui vai mostrar a imagem no fundo
label_fundo = tk.Label(janela, image=img)
label_fundo.place(x=0,y=0, relwidth=1, relheight=1)


#titulo da pagina
fonte_cabecalho = font.Font(family="Garamond", size=24, weight="bold")
rotulo_cabecalho = tk.Label(janela, text="MEU APP DE TAREFAS",padx=610,font=fonte_cabecalho, bg=co5, fg=co1).pack(pady=20)


frame_em_edicao = None

#funcao adicionar tarefa
def adicionar_tarefas():
    global frame_em_edicao

    tarefa = entrada_tarefa.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frame_em_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_em_edicao = None
        else:
            adicionar_item_tarefa(tarefa)
            entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning('Entrada Invalida', 'Por favor adicione uma tarefa')

def adicionar_item_tarefa(tarefa):
    frame_tarefa = tk.Frame(canvas_interior, bg='white', bd=1, relief=tk.SOLID)

    label_tarefa = tk.Label(frame_tarefa, text=tarefa, font=("Garamond", 16), bg="white", width=25, height=2, anchor="w")

    label_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

    botao_editar = tk.Button(frame_tarefa, image=icon_editar, command=lambda f=frame_tarefa, l=label_tarefa: preparar_edicao(f, l), bg='white', relief=tk.FLAT)
    botao_editar.pack(side=tk.RIGHT, padx=5)

    botao_deletar=tk.Button(frame_tarefa, image=icon_deletar, command=lambda f=frame_tarefa: deletar_tarefa(f), bg='white', relief=tk.FLAT)
    botao_deletar.pack(side=tk.RIGHT, padx=5)

    frame_tarefa.pack(fill=tk.X, padx=5, pady=5)


    Checkbutton = ttk.Checkbutton(frame_tarefa, command=lambda label=label_tarefa: alternar_sublinhado(label))
    Checkbutton.pack(side=tk.RIGHT, padx=5)

    canvas_interior.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))


def preparar_edicao(frame_tarefa, label_tarefa):
    global frame_em_edicao

    frame_em_edicao = frame_tarefa
    entrada_tarefa.delete(0, tk.END)
    entrada_tarefa.insert(0, label_tarefa.cget("text"))

def atualizar_tarefa(nova_tarefa):
    global frame_em_edicao

    for widget in frame_em_edicao.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text = nova_tarefa)


def deletar_tarefa(frame_tarefa):
    frame_tarefa.destroy()
    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

def alternar_sublinhado(label):
    fonte_atual = label.cget('font')
    if 'overstrike' in fonte_atual:
        nova_fonte = fonte_atual.replace(' overstrike', '')
    else:
        nova_fonte = fonte_atual + ' overstrike'
    label.config(font=nova_fonte)
  #caminho dos icones
caminho_icon_editar = os.path.join('icon','edit.png')
caminho_icon_deletar = os.path.join('icon','deletar.png')


icon_editar = PhotoImage(file=caminho_icon_editar).subsample(7,7)
icon_deletar = PhotoImage(file=caminho_icon_deletar).subsample(7,7)

#Barra onde ira receber o texto(input)
frame = tk.Frame(janela, bg=co1)
frame.pack(pady=10)

entrada_tarefa = tk.Entry(frame, font=('Garamond', 14), relief=tk.FLAT, bg='white', fg=co2, width=30)
entrada_tarefa.pack(side=tk.LEFT, padx=10)

#botao de clicar para adiconar a lista pelo bota e pelo ENTER
botao_adicionar = tk.Button(frame, command=adicionar_tarefas, text='Adicionar Tarefa', bg=co5, fg=co1, height=1, width=15, font=('Roboto',11),relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)

entrada_tarefa.bind('<Return>', lambda event: adicionar_tarefas())

# Contêiner da lista de tarefas com rolagem
conteiner_lista = tk.Frame(janela, bg=co1)
conteiner_lista.pack(pady=10, fill=tk.BOTH, expand=True)

# Frame para a lista de tarefas com altura fixa
frame_lista_tarefa = tk.Frame(conteiner_lista, bg='white', width=450, height=300)
frame_lista_tarefa.pack_propagate(False)
frame_lista_tarefa.pack(pady=10, fill=tk.BOTH, expand=True)


#canvas e barra de rolagem
canvas = tk.Canvas(frame_lista_tarefa, bg='white')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame_lista_tarefa, orient='vertical', command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)



# Frame interno para adicionar tarefas
canvas_interior = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=canvas_interior, anchor="nw")

# Atualiza a região de rolagem
canvas_interior.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))


janela.mainloop()