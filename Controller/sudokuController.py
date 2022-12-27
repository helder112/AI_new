import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
import numpy as np


def iniciar(sudoku, dominio,restricoes):
    root = tk.Tk()
    root.title("Sudoku Solver")
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    width = 500
    height = 400
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=True, height=True)
    root.config(bg='#1E90FF')
    framelogo=Frame(root)
    framelogo.pack(side=TOP, anchor=NW, pady=50, padx=50)
    frame = Frame(root)
    frame.pack(side=TOP)
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)
    for x in range(len(sudoku)):
        for y in range(len(sudoku)):
            valortxt= tk.Entry(frame,width=5,justify="center")
            posicao = int(sudoku[x,y])

            if y==2 and x==2 or y==5 and x==5or y==2 and x==5 or y==5 and x==2:
                valortxt.grid(row=x, column=y, padx=(2,20),pady=(2,20))
            elif  y== 2 or y== 5:
                valortxt.grid(row=x, column=y, padx=(2,20))
            elif x== 2 or x==5:
                valortxt.grid(row=x, column=y, pady=(2,20))

            else:
                valortxt.grid(row=x, column=y, padx=2,pady=2)
            if posicao>0:
                valortxt.insert(0,posicao)

    for x in range(len(sudoku)):
        for y in range(len(sudoku)):
            posicao = sudoku[x, y]
            if posicao != 0:
                dominiolocal = [posicao]
                dominio.get((x, y))
                dominio[(x, y)] = dominiolocal
            elif posicao == 0:
                dominiolocal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                dominio.get((x, y))
                dominio[(x, y)] = dominiolocal

    for x in range(len(sudoku)):
        for y in range(len(sudoku)):
            for i in range(9):
                if i != y:
                    restricoes.append(
                        ((x, y), (x, i)))
            for j in range(9):
                if j != x:
                    restricoes.append(((x, y), (j, y)))

            lin = (x // 3) * 3
            col = (y // 3) * 3
            for w in range(lin, (lin + 3)):
                for z in range(col, (col + 3)):
                    if w != x and z != y:
                        restricoes.append(
                            ((x, y), (w, z)))
    solve_button = tk.Button(bottomframe, text="Solve", command=lambda: printvalores(sudoku,dominio,restricoes,frame))
    solve_button.grid(row=11, column=11)
    root.mainloop()
def revisar(Di, Dj):
    revisado= False
    for i in Di:
        removal= True
        for j in Dj:
            if i != j:
                removal= False
                break
        if removal:
            Di.remove(i)
            revisado=True
    return revisado

def Ac3(restricoes, dominio):
    queue= restricoes.copy()
    lixo=[]
    solucao= True
    while queue != []:
        (xi, xj)= queue.pop(0)
        lixo.append((xi, xj))
        Di= dominio[xi]
        Dj= dominio[xj]
        revisado= revisar(Di, Dj)
        if revisado == True:
            if Di!= []:
                for i in range(len(lixo)):
                    (a, b)= lixo[i]
                    if a != xj:
                        if b== xi:
                            queue.append((a,b))
            if Di == []:
                solucao= False
                break
    return solucao

def printvalores(sudoku,dominio,restricoes,frame):
    solucao= Ac3(restricoes, dominio)
    if solucao == True:
        for x in range(len(sudoku)):
            for y in range(len(sudoku)):
                if sudoku[x, y]== 0:   # se a posicao estava em zero, preenche como encontrado pelo programa
                    D=dominio[(x,y)]
                    sudoku[x,y]= D[0]
                valortxt = tk.Entry(frame,width=5,justify="center")
                posicao = int(sudoku[x, y])
                if y == 2 and x == 2 or y == 5 and x == 5 or y == 2 and x == 5 or y == 5 and x == 2:
                    valortxt.grid(row=x, column=y, padx=(2, 20), pady=(2, 20))
                elif y == 2 or y == 5:
                    valortxt.grid(row=x, column=y, padx=(2, 20))
                elif x == 2 or x == 5:
                    valortxt.grid(row=x, column=y, pady=(2, 20))

                else:
                    valortxt.grid(row=x, column=y, padx=2, pady=2)
                valortxt.insert(0, posicao)
    else:
        showinfo(
            title='Por favor aguarde',
            message="Sudoku nao possui solucao  pelo algoritmo Ac3!"
        )



