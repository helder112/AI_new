import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import PIL
import numpy as np
from PIL import ImageSequence, ImageTk
from matplotlib import pyplot as plt
from sklearn import metrics
from Controller import controller,sudokuController
#from . import Controller as controller
from threading import Thread
import pathlib

class App:

    def __init__(self, root,xpto=""):
        self.xpto = xpto
        self.root= root
        self.T1 = Thread()
        self.T2=Thread()
        self.imgPlot=Label(self.root)

        # setting title
        root.title("Naive Bayes and Perceptron")
        # setting window size
        width = 1100
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.config(bg='#1E90FF')

        canvas = tk.Canvas(root, width=1100, height=500,bg='#1E90FF')

        canvas.pack()
        canvas.tk.call('raise', canvas._w)
        GButton_499 = tk.Button(root)
        GButton_499["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#1005F9"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Calcular Naive Bayes"
        GButton_499.place(x=320, y=450, width=120, height=35)
        GButton_499["command"] = self.GButton_499_command

        sudokuButton = tk.Button(root)
        sudokuButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        sudokuButton["font"] = ft
        sudokuButton["fg"] = "#1005F9"
        sudokuButton["justify"] = "center"
        sudokuButton["text"] = "Calcular Sudoku"
        sudokuButton.place(x=580, y=450, width=120, height=35)
        sudokuButton["command"] = self.sudokuCommand




        GButton_480 = tk.Button(root)
        GButton_480["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_480["font"] = ft
        GButton_480["fg"] = "#1005F9"
        GButton_480["justify"] = "center"
        GButton_480["text"] = "Calcular Perceptrão"
        GButton_480.place(x=450, y=450, width=120, height=35)
        GButton_480["command"] = self.GButton_480_command


        GButton_599 = tk.Button(root)
        GButton_599["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_599["font"] = ft
        GButton_599["fg"] = "#1005F9"
        GButton_599["justify"] = "center"
        GButton_599["text"] = "Escolher Ficheiro"
        GButton_599.place(x=190, y=450, width=120, height=35)
        GButton_599["command"] = self.GButton_599_command

        GLabel_200 = tk.Label(root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_200["font"] = ft
        GLabel_200["fg"] = "#333333"
        GLabel_200["justify"] = "left"
        GLabel_200["text"] = "Accurancy:"
        GLabel_200.place(x=40, y=50, width=70, height=25)

        GLabel_186 = tk.Label(root,bg='#1E90FF')
        GLabel_186["cursor"] = "arrow"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_186["font"] = ft
        GLabel_186["fg"] = "#333333"
        GLabel_186["justify"] = "left"
        GLabel_186["text"] = "Ratio Error:"
        GLabel_186.place(x=40, y=80, width=70, height=25)

        GLabel_33 = tk.Label(root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_33["font"] = ft
        GLabel_33["fg"] = "#333333"
        GLabel_33["justify"] = "left"
        GLabel_33["text"] = "Sensitivity:"
        GLabel_33.place(x=40, y=110, width=70, height=25)

        GLabel_84 = tk.Label(root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_84["font"] = ft
        GLabel_84["fg"] = "#333333"
        GLabel_84["justify"] = "left"
        GLabel_84["text"] = "Specificity:"
        GLabel_84.place(x=40, y=140, width=70, height=25)

        GLabel_737 = tk.Label(root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_737["font"] = ft
        GLabel_737["fg"] = "#333333"
        GLabel_737["justify"] = "left"
        GLabel_737["text"] = "Precision:"
        GLabel_737.place(x=40, y=170, width=70, height=25)

        GLabel_898 = tk.Label(root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_898["font"] = ft
        GLabel_898["fg"] = "#333333"
        GLabel_898["justify"] = "left"
        GLabel_898["text"] = "Recall:"
        GLabel_898.place(x=40, y=200, width=70, height=25)

        GLabel_592 = tk.Label(root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_592["font"] = ft
        GLabel_592["fg"] = "#333333"
        GLabel_592["justify"] = "left"
        GLabel_592["text"] = "F-Measure:"
        GLabel_592.place(x=40, y=230, width=70, height=25)

        GLabel_685 = tk.Label(root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=11)
        GLabel_685["font"] = ft
        GLabel_685["fg"] = "#333333"
        GLabel_685["justify"] = "center"
        GLabel_685["text"] = "Categoria"
        GLabel_685.place(x=40, y=20, width=70, height=15)

        GLabel_98 = tk.Label(root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=11)
        GLabel_98["font"] = ft
        GLabel_98["fg"] = "#333333"
        GLabel_98["justify"] = "center"
        GLabel_98["text"] = "Validação"
        GLabel_98.place(x=130, y=20, width=60, height=15)

        GLabel_961 = tk.Label(root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=11)
        GLabel_961["font"] = ft
        GLabel_961["fg"] = "#333333"
        GLabel_961["justify"] = "center"
        GLabel_961["text"] = "Teste"
        GLabel_961.place(x=205, y=20, width=70, height=15)

        canvas.create_line(0, 40, 650, 40, fill="White", width=3)
        canvas.create_line(0, 270, 650, 270, fill="White", width=3)
        canvas.create_line(120, 0, 120, 270, fill="White", width=3)

        canvas.create_line(200, 0, 200, 270, fill="White", width=3)
        canvas.create_line(3, 0, 3, 448, fill="White", width=3)
        canvas.create_line(650, 0, 650, 450, fill="White", width=3)

        canvas.create_line(0, 400, 650, 400, fill="White", width=3)
        canvas.create_line(0, 448, 650, 448, fill="White", width=3)
        canvas.create_line(0,3 , 650, 3, fill="White", width=3)
        root.mainloop()

    def select_file(root):
        filetypes = (
            ('text files', '*.csv'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=filename
        )
        return filename


        open_button = tk.Button(root,text='Open a File',command=self.select_file)

        open_button.pack(expand=True)

    def GButton_599_command(self):
        self.xpto = self.select_file()
        GLabel_selectFileLabel = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_selectFileLabel["font"] = ft
        GLabel_selectFileLabel["fg"] = "#333333"
        GLabel_selectFileLabel["justify"] = "left"
        GLabel_selectFileLabel["text"] = "Ficheiro:"
        GLabel_selectFileLabel.place(x=10, y=415, width=100, height=15)

        GLabel_selectFile = tk.Label(self.root,borderwidth=3,relief="groove")
        ft = tkFont.Font(family='Times', size=10)
        GLabel_selectFile["font"] = ft
        GLabel_selectFile["fg"] = "#333333"
        GLabel_selectFile["justify"] = "left"
        GLabel_selectFile["text"] = self.xpto
        GLabel_selectFile.place(x=100, y=410, width=400, height=25)

    def startPerceptrao(self):

        photo = tk.PhotoImage(file="processing.gif")
        GlabelLoading = tk.Label(image=photo)
        GlabelLoading.place(x=200, y=310, width=400, height=25)
        GlabelLoading.pack()
        #criar Listas vazias
        X, Y, X_validacao, Y_validacao, X_teste, Y_teste, mham, mspam, total_hamspmClassification, total_hamspm_Test, total_hamspmTraining, mTotal = controller.createLists()
        #importar ficheiro
        mspam, mham, mTotal, total_hamspmClassification, total_hamspm_Test, total_hamspmTraining,yclass = controller.file_import(X, Y, self.xpto)
        #execucao do algoritmo
        acc1, err1, sn1, sp1, p1, r1, fm1, acc2, err2, sn2, sp2, p2, r2, fm2, ExecutionTime,T,Y_teste,classifica = controller.main_perceptrao(X, yclass, X_validacao, Y_validacao, X_teste, Y_teste, mham, mspam, total_hamspmClassification,total_hamspm_Test, total_hamspmTraining, mTotal)
        #criacao de labels e interface para atualizar com o código depos de executado

        GLabel_270 = tk.Label(self.root,borderwidth=3,relief="groove",bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_270["font"] = ft
        GLabel_270["fg"] = "#333333"
        GLabel_270["justify"] = "center"
        GLabel_270["text"] = f"Execution Time: {ExecutionTime}"
        GLabel_270.place(x=10, y=300, width=200, height=25)

        GlabelC= tk.Label(self.root,borderwidth=3,relief="groove",bg='#1E90FF')
        GlabelC["font"] = ft
        GlabelC["fg"] = "#333333"
        GlabelC["justify"] = "center"
        GlabelC["text"] = f"Melhor desempenho em T= {T}"
        GlabelC.place(x=10, y=330, width=200, height=25)

        GLabel_359 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_359["font"] = ft
        GLabel_359["fg"] = "#333333"
        GLabel_359["justify"] = "center"
        GLabel_359["text"] = acc1
        GLabel_359.place(x=130, y=50, width=60, height=25)

        GLabel_383 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_383["font"] = ft
        GLabel_383["fg"] = "#333333"
        GLabel_383["justify"] = "center"
        GLabel_383["text"] = err1
        GLabel_383.place(x=130, y=80, width=60, height=25)

        GLabel_139 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_139["font"] = ft
        GLabel_139["fg"] = "#333333"
        GLabel_139["justify"] = "center"
        GLabel_139["text"] = sn1
        GLabel_139.place(x=130, y=110, width=60, height=25)

        GLabel_453 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_453["font"] = ft
        GLabel_453["fg"] = "#333333"
        GLabel_453["justify"] = "center"
        GLabel_453["text"] = sp1
        GLabel_453.place(x=130, y=140, width=60, height=25)

        GLabel_997 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_997["font"] = ft
        GLabel_997["fg"] = "#333333"
        GLabel_997["justify"] = "center"
        GLabel_997["text"] = p1
        GLabel_997.place(x=130, y=170, width=60, height=25)

        GLabel_437 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_437["font"] = ft
        GLabel_437["fg"] = "#333333"
        GLabel_437["justify"] = "center"
        GLabel_437["text"] = r1
        GLabel_437.place(x=130, y=200, width=60, height=25)

        GLabel_913 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_913["font"] = ft
        GLabel_913["fg"] = "#333333"
        GLabel_913["justify"] = "center"
        GLabel_913["text"] = fm1
        GLabel_913.place(x=130, y=230, width=60, height=25)

        GLabel_995 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_995["font"] = ft
        GLabel_995["fg"] = "#333333"
        GLabel_995["justify"] = "center"
        GLabel_995["text"] = acc2
        GLabel_995.place(x=210, y=50, width=60, height=25)

        GLabel_496 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_496["font"] = ft
        GLabel_496["fg"] = "#333333"
        GLabel_496["justify"] = "center"
        GLabel_496["text"] =  err2
        GLabel_496.place(x=210, y=80, width=60, height=25)

        GLabel_162 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_162["font"] = ft
        GLabel_162["fg"] = "#333333"
        GLabel_162["justify"] = "center"
        GLabel_162["text"] = sn2
        GLabel_162.place(x=210, y=110, width=60, height=25)

        GLabel_500 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_500["font"] = ft
        GLabel_500["fg"] = "#333333"
        GLabel_500["justify"] = "center"
        GLabel_500["text"] = sp2
        GLabel_500.place(x=210, y=140, width=60, height=25)

        GLabel_63 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_63["font"] = ft
        GLabel_63["fg"] = "#333333"
        GLabel_63["justify"] = "center"
        GLabel_63["text"] = p2
        GLabel_63.place(x=210, y=170, width=60, height=25)

        GLabel_617 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_617["font"] = ft
        GLabel_617["fg"] = "#333333"
        GLabel_617["justify"] = "center"
        GLabel_617["text"] = r2
        GLabel_617.place(x=210, y=200, width=60, height=25)

        GLabel_61 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_61["font"] = ft
        GLabel_61["fg"] = "#333333"
        GLabel_61["justify"] = "center"
        GLabel_61["text"] = fm2
        GLabel_61.place(x=210, y=230, width=60, height=25)
        GlabelLoading["text"] = ""

        #mudar do Y_teste de -1 para 0 em spam para validar o plot
        for i in range(len(Y_teste)):
            if Y_teste[i]== -1:
                Y_teste[i] =0

        return self.calcularPlot(Y_teste,classifica)


    def startNaive(self):
        photo = tk.PhotoImage(file="processing.gif")
        GlabelLoading = tk.Label(image=photo)
        GlabelLoading.place(x=200, y=310, width=400, height=25)
        GlabelLoading.pack()

        X, Y, X_validacao, Y_validacao, X_teste, Y_teste, mham, mspam, total_hamspmClassification, total_hamspm_Test, total_hamspmTraining, mTotal = controller.createLists()
        mspam, mham, mTotal, total_hamspmClassification, total_hamspm_Test, total_hamspmTraining,yclass = controller.file_import(X, Y, self.xpto)
        acc1, err1, sn1, sp1, p1, r1, fm1, acc2, err2, sn2, sp2, p2, r2, fm2, ExecutionTime,classificacaoActual,classificacaoPredicted,C = controller.main_naive(X, Y, X_validacao, Y_validacao, X_teste, Y_teste, mham, mspam, total_hamspmClassification,total_hamspm_Test, total_hamspmTraining, mTotal)

        GLabel_270 = tk.Label(self.root,borderwidth=3,relief="groove",bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_270["font"] = ft
        GLabel_270["fg"] = "#333333"
        GLabel_270["justify"] = "center"
        GLabel_270["text"] = f"Execution Time: {ExecutionTime}"
        GLabel_270.place(x=10, y=300, width=200, height=25)




        GlabelC= tk.Label(self.root,borderwidth=3,relief="groove",bg='#1E90FF')
        GlabelC["font"] = ft
        GlabelC["fg"] = "#333333"
        GlabelC["justify"] = "center"
        GlabelC["text"] = f"Melhor desempenho em C= {C}"
        GlabelC.place(x=10, y=330, width=200, height=25)

        GLabel_359 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_359["font"] = ft
        GLabel_359["fg"] = "#333333"
        GLabel_359["justify"] = "center"
        GLabel_359["text"] = acc1
        GLabel_359.place(x=130, y=50, width=60, height=25)

        GLabel_383 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_383["font"] = ft
        GLabel_383["fg"] = "#333333"
        GLabel_383["justify"] = "center"
        GLabel_383["text"] = err1
        GLabel_383.place(x=130, y=80, width=60, height=25)

        GLabel_139 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_139["font"] = ft
        GLabel_139["fg"] = "#333333"
        GLabel_139["justify"] = "center"
        GLabel_139["text"] = sn1
        GLabel_139.place(x=130, y=110, width=60, height=25)

        GLabel_453 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_453["font"] = ft
        GLabel_453["fg"] = "#333333"
        GLabel_453["justify"] = "center"
        GLabel_453["text"] = sp1
        GLabel_453.place(x=130, y=140, width=60, height=25)

        GLabel_997 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_997["font"] = ft
        GLabel_997["fg"] = "#333333"
        GLabel_997["justify"] = "center"
        GLabel_997["text"] = p1
        GLabel_997.place(x=130, y=170, width=60, height=25)

        GLabel_437 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_437["font"] = ft
        GLabel_437["fg"] = "#333333"
        GLabel_437["justify"] = "center"
        GLabel_437["text"] = r1
        GLabel_437.place(x=130, y=200, width=60, height=25)

        GLabel_913 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_913["font"] = ft
        GLabel_913["fg"] = "#333333"
        GLabel_913["justify"] = "center"
        GLabel_913["text"] = fm1
        GLabel_913.place(x=130, y=230, width=60, height=25)

        GLabel_995 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_995["font"] = ft
        GLabel_995["fg"] = "#333333"
        GLabel_995["justify"] = "center"
        GLabel_995["text"] = acc2
        GLabel_995.place(x=210, y=50, width=60, height=25)

        GLabel_496 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_496["font"] = ft
        GLabel_496["fg"] = "#333333"
        GLabel_496["justify"] = "center"
        GLabel_496["text"] =  err2
        GLabel_496.place(x=210, y=80, width=60, height=25)

        GLabel_162 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_162["font"] = ft
        GLabel_162["fg"] = "#333333"
        GLabel_162["justify"] = "center"
        GLabel_162["text"] = sn2
        GLabel_162.place(x=210, y=110, width=60, height=25)

        GLabel_500 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_500["font"] = ft
        GLabel_500["fg"] = "#333333"
        GLabel_500["justify"] = "center"
        GLabel_500["text"] = sp2
        GLabel_500.place(x=210, y=140, width=60, height=25)

        GLabel_63 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_63["font"] = ft
        GLabel_63["fg"] = "#333333"
        GLabel_63["justify"] = "center"
        GLabel_63["text"] = p2
        GLabel_63.place(x=210, y=170, width=60, height=25)

        GLabel_617 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_617["font"] = ft
        GLabel_617["fg"] = "#333333"
        GLabel_617["justify"] = "center"
        GLabel_617["text"] = r2
        GLabel_617.place(x=210, y=200, width=60, height=25)

        GLabel_61 = tk.Label(self.root,bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_61["font"] = ft
        GLabel_61["fg"] = "#333333"
        GLabel_61["justify"] = "center"
        GLabel_61["text"] = fm2
        GLabel_61.place(x=210, y=230, width=60, height=25)
        GlabelLoading["text"] = ""


        return self.calcularPlot(classificacaoActual, classificacaoPredicted)

    def calcularPlot(self,actual,predicted):

        cm_display = metrics.ConfusionMatrixDisplay.from_predictions(actual, predicted, cmap="cividis")
        plt.savefig("Output.png")
        load = PIL.Image.open("Output.png")
        load = load.resize((400, 400))
        render = ImageTk.PhotoImage(load)
        self.imgPlot=Label(self.root, image=render)
        #img = Label(self.root, image=render)
        self.imgPlot.image=render
       # img.image = render
        self.imgPlot.place(x=670, y=30)


        #self.processing("Stop",False)

    def processing(self,T1):
        lbl = Label(self.root,bg='#1E90FF')
        lbl.place(x=300, y=150)
        if T1.is_alive():
            img = PIL.Image.open("processing4.gif")
            for img in ImageSequence.Iterator(img):
                img = img.resize((100, 100))
                img = ImageTk.PhotoImage(img, )
                lbl.config(image=img)
                self.root.update()
            self.root.after(0, self.processing(T1))
        else:
            img=""
            lbl.destroy()
            self.root.update()

    def GButton_499_command(self):
        self.resetInterface()
        if self.T1.is_alive():
            showinfo(
                title='Por favor aguarde',
                message=" O programa está em Execução por favor espere a sua finalização antes de executar novamente!"
            )
        else:
            self.T1 = Thread(target=self.startNaive)

            self.T1.start()

            T2=Thread(target=self.processing(self.T1))

            T2.start()


    def GButton_480_command(self):
        self.resetInterface()

        if self.T1.is_alive():
            showinfo(
                title='Por favor aguarde',
                message=" O programa está em Execução por favor espere a sua finalização antes de executar novamente!"
            )
        else:
            self.T1 = Thread(target=self.startPerceptrao)

            self.T1.start()

            T2=Thread(target=self.processing(self.T1))

            T2.start()


    def sudokuCommand(self):

        if self.T1.is_alive():
            showinfo(
                title='Por favor aguarde',
                message=" O programa está em Execução por favor espere a sua finalização antes de executar o Sudoku!"
            )
        else:
            sudoku = np.zeros((9, 9))
            sudoku[0, 2] = 3
            sudoku[0, 4] = 2
            sudoku[0, 6] = 6
            sudoku[1, 0] = 9
            sudoku[1, 3] = 3
            sudoku[1, 5] = 5
            sudoku[1, 8] = 1
            sudoku[2, 2] = 1
            sudoku[2, 3] = 8
            sudoku[2, 5] = 6
            sudoku[2, 6] = 4
            sudoku[3, 2] = 8
            sudoku[3, 3] = 1
            sudoku[3, 5] = 2
            sudoku[3, 6] = 9
            sudoku[4, 0] = 7
            sudoku[4, 8] = 8
            sudoku[5, 2] = 6
            sudoku[5, 3] = 7
            sudoku[5, 5] = 8
            sudoku[5, 6] = 2
            sudoku[6, 2] = 2
            sudoku[6, 3] = 6
            sudoku[6, 5] = 9
            sudoku[6, 6] = 5
            sudoku[7, 0] = 8
            sudoku[7, 3] = 2
            sudoku[7, 5] = 3
            sudoku[7, 8] = 9
            sudoku[8, 2] = 5
            sudoku[8, 4] = 1
            sudoku[8, 6] = 3
            dominio = {}
            restricoes = []
            sudokuController.iniciar(sudoku, dominio,restricoes)



    def resetInterface(self):

        GLabel_270 = tk.Label(self.root, borderwidth=3, relief="groove", bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_270["font"] = ft
        GLabel_270["fg"] = "#333333"
        GLabel_270["justify"] = "center"
        GLabel_270["text"] = ""
        GLabel_270.place(x=10, y=300, width=200, height=25)

        GlabelC = tk.Label(self.root, borderwidth=3, relief="groove", bg='#1E90FF')
        GlabelC["font"] = ft
        GlabelC["fg"] = "#333333"
        GlabelC["justify"] = "center"
        GlabelC["text"] = ""
        GlabelC.place(x=10, y=330, width=200, height=25)

        GLabel_359 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_359["font"] = ft
        GLabel_359["fg"] = "#333333"
        GLabel_359["justify"] = "center"
        GLabel_359["text"] = ""
        GLabel_359.place(x=130, y=50, width=60, height=25)

        GLabel_383 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_383["font"] = ft
        GLabel_383["fg"] = "#333333"
        GLabel_383["justify"] = "center"
        GLabel_383["text"] = ""
        GLabel_383.place(x=130, y=80, width=60, height=25)

        GLabel_139 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_139["font"] = ft
        GLabel_139["fg"] = "#333333"
        GLabel_139["justify"] = "center"
        GLabel_139["text"] = ""
        GLabel_139.place(x=130, y=110, width=60, height=25)

        GLabel_453 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_453["font"] = ft
        GLabel_453["fg"] = "#333333"
        GLabel_453["justify"] = "center"
        GLabel_453["text"] = ""
        GLabel_453.place(x=130, y=140, width=60, height=25)

        GLabel_997 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_997["font"] = ft
        GLabel_997["fg"] = "#333333"
        GLabel_997["justify"] = "center"
        GLabel_997["text"] = ""
        GLabel_997.place(x=130, y=170, width=60, height=25)

        GLabel_437 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_437["font"] = ft
        GLabel_437["fg"] = "#333333"
        GLabel_437["justify"] = "center"
        GLabel_437["text"] = ""
        GLabel_437.place(x=130, y=200, width=60, height=25)

        GLabel_913 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_913["font"] = ft
        GLabel_913["fg"] = "#333333"
        GLabel_913["justify"] = "center"
        GLabel_913["text"] = ""
        GLabel_913.place(x=130, y=230, width=60, height=25)

        GLabel_995 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_995["font"] = ft
        GLabel_995["fg"] = "#333333"
        GLabel_995["justify"] = "center"
        GLabel_995["text"] = ""
        GLabel_995.place(x=210, y=50, width=60, height=25)

        GLabel_496 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_496["font"] = ft
        GLabel_496["fg"] = "#333333"
        GLabel_496["justify"] = "center"
        GLabel_496["text"] = ""
        GLabel_496.place(x=210, y=80, width=60, height=25)

        GLabel_162 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_162["font"] = ft
        GLabel_162["fg"] = "#333333"
        GLabel_162["justify"] = "center"
        GLabel_162["text"] = ""
        GLabel_162.place(x=210, y=110, width=60, height=25)

        GLabel_500 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_500["font"] = ft
        GLabel_500["fg"] = "#333333"
        GLabel_500["justify"] = "center"
        GLabel_500["text"] = ""
        GLabel_500.place(x=210, y=140, width=60, height=25)

        GLabel_63 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_63["font"] = ft
        GLabel_63["fg"] = "#333333"
        GLabel_63["justify"] = "center"
        GLabel_63["text"] = ""
        GLabel_63.place(x=210, y=170, width=60, height=25)

        GLabel_617 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_617["font"] = ft
        GLabel_617["fg"] = "#333333"
        GLabel_617["justify"] = "center"
        GLabel_617["text"] = ""
        GLabel_617.place(x=210, y=200, width=60, height=25)

        GLabel_61 = tk.Label(self.root, bg='#1E90FF')
        ft = tkFont.Font(family='Times', size=10)
        GLabel_61["font"] = ft
        GLabel_61["fg"] = "#333333"
        GLabel_61["justify"] = "center"
        GLabel_61["text"] = ""
        GLabel_61.place(x=210, y=230, width=60, height=25)

        self.imgPlot.destroy()


