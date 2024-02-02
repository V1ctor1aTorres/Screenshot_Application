from unicodedata import name
import pyautogui
#Funcionalidades para automação de tarefas no computador
import time
#Utilizado para pausar a execução do programa
import tkinter as tk
#construir a interface gráfica

def screenshot():
    #Dar tempo ao usuário de mudar para a janela desejada antes de tirar a captura de tela
    time.sleep(5)
    #obter o timestamp atual e o transforma em uma string para criar um nome de arquivo único para a captura de tela
    name = time.time()
    #O arquivo será salvo no diretório especificado.
    name = f'C:/Users/Documents/projetos/{name}.png'
    #Tirar uma captura de tela do monitor atual. A imagem resultante é armazenada na variável img.
    img = pyautogui.screenshot()
    #A captura de tela é salva como um arquivo de imagem PNG
    img.save(name)
    #Específico da biblioteca Pillow (PIL), imagem é exibida
    img.show()

#Criação de interface gráfica com Tkinker:
#Criando uma instância da classe Tk e um objeto Frame
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
#Criação de Botões na Interface Gráfica
#Quando pressionado, chama a função screenshot
button = tk.Button(frame, text='Screenshot', command=screenshot)
button.pack(side=tk.LEFT)
#Quando pressionado fecha a interface gráfica 
close = tk.Button(frame,text='Sair', command=root.quit)
close.pack(side=tk.LEFT)
#Inicia o loop principal do Tkinter, permitindo que a interface gráfica seja executada e interaja com o usuário.
root.mainloop()
