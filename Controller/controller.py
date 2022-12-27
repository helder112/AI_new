import time  # contar tempo de execucao
import math
import numpy as np
import csv  # biblioteca necessária para ler ficheiros externos
import random
import matplotlib.pyplot as plt
import seaborn as sns;
from sklearn import metrics

import string

#sns.set()
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as mtp


def createLists():
    X = []  # lista de mensagens
    Y = []  # lista de classificação das mensagens
    X_validacao = []
    Y_validacao = []
    X_teste = []
    Y_teste = []
    mham = 0
    mspam = 0
    total_hamspmClassification = 0
    total_hamspm_Test = 0
    total_hamspmTraining = 0
    mTotal = 0
    return X,Y,X_validacao,Y_validacao,X_teste,Y_teste,mham,mspam,total_hamspmClassification,total_hamspm_Test,total_hamspmTraining,mTotal

def file_import(X,Y,xpto):

    if xpto=="":
        xpto='spam.csv'

    with open(xpto, encoding="latin-1") as csv_file:
        csv_reader = csv.reader(csv_file)  # abrir o ficheiro das mensagens
        for line in csv_reader:
            X.append(line[1])
            Y.append(line[0])

    # 4 eliminar cabeçalhos
    X.pop(0)
    Y.pop(0)
    return documentFiltering(X,Y)
def chartoreject(new_string):
  #  rejeitar = ':<>=#().",!?|\/*?'  # caracteres a não considerar como palavra na mensagem
   # chartoreject =[':','<','>','=','#','(',')','.','"',',','!','?','|','/','*','?']
   # for j in range(len(chartoreject)):
  #      mensagem = new_string.replace(chartoreject[j], "")

    test_str = new_string.translate(str.maketrans('', '', string.punctuation))

   # print(test_str)

    return test_str
    # 5

def documentFiltering(X,Y):
    for emailidx in range(len(X)):
        new_string = X[emailidx].lower()
        X[emailidx] = chartoreject(new_string)





#6 percorrer todas as menssagens e contar se Spam ou Ham e o total de menssagens

    mham= Y.count("ham")
    mspam= Y.count("spam")
    mTotal=len(X)
    total_hamspmClassification = (mham * 0.15)+ mspam * 0.15
    total_hamspm_Test = (mham * 0.15)+ mspam * 0.15
    total_hamspmTraining = (mham * 0.15)+ mspam * 0.15
    return mspam,mham,mTotal,total_hamspmClassification,total_hamspm_Test,total_hamspmTraining

def messageValidation(X,Y,X_validacao,Y_validacao,mham,mspam,total_hamspmClassification,mTotal):
    divisaoham = mham * 0.15
    divisaospam = mspam * 0.15
    divHam = 0
    divSpam = 0
    countdivs = int(divHam) + int(divSpam)
    flag = True

    while flag:
        randomNum = random.randrange(len(X))
        if countdivs > total_hamspmClassification:
            flag = False
        else:
            if divSpam < divisaospam:
                if Y[randomNum] == "spam":
                    X_validacao.append(X[randomNum])
                    X.pop(randomNum)
                    Y_validacao.append(Y[randomNum])
                    Y.pop(randomNum)
                    divSpam = divSpam + 1
            if divHam < divisaoham:
                if Y[randomNum] == "ham":
                    X_validacao.append(X[randomNum])
                    X.pop(randomNum)
                    Y_validacao.append(Y[randomNum])
                    Y.pop(randomNum)
                    divHam = divHam + 1
            countdivs = int(divHam) + int(divSpam)

def messageTest(X,Y,X_teste,Y_teste,mham,mspam,total_hamspm_Test,mTotal):
    testHam = mham * 0.15
    testSpam = mspam * 0.15
    divHam = 0
    divSpam = 0
    countdivs = int(divHam) + int(divSpam)

    flag = True

    while flag:
        randomNum = random.randrange(len(X))
        if countdivs > total_hamspm_Test:
            flag = False
        else:
            if divSpam < testSpam:
                if Y[randomNum] == "spam":
                    X_teste.append(X[randomNum])
                    X.pop(randomNum)
                    Y_teste.append(Y[randomNum])
                    Y.pop(randomNum)
                    divSpam = divSpam + 1
            if divHam < testHam:
                if Y[randomNum] == "ham":
                    X_teste.append(X[randomNum])
                    X.pop(randomNum)
                    Y_teste.append(Y[randomNum])
                    Y.pop(randomNum)
                    divHam = divHam + 1
            countdivs = int(divHam) + int(divSpam)
    mTotal= len(X)


def naiveBaiesTrain(X,Y):
    BoW= []
 #compute D
    for x in range(len(X)):
        email = X[x]
        emailSplit = email.split()
        for wordIdx in range(len(emailSplit)):
            if not emailSplit[wordIdx] in BoW:
                BoW.append(emailSplit[wordIdx])

    # compute m,mham,mspam
    m = len(X)
    mham = Y.count("ham")
    mspam = Y.count("spam")
    #inicializar P € R^2xn com Pij =1, Wspam=n,Wham=n
    p = np.ones((2, len(BoW)))
    wspam = 0  # quantidade de palavras classificadas spam
    wham = 0  # quantidade de palavras classificadas ham

#count the occurrence of each word
    for x in range(len(X)):
        email=X[x]
        emailSplit= email.split()
        if Y[x] == "spam":
            for wordIdx in range(len(emailSplit)):
                bowIdx=BoW.index(emailSplit[wordIdx])
                p[0][bowIdx]=p[0][bowIdx]+1
                wspam += 1
        elif Y[x]== "ham":
            for wordIdx in range(len(emailSplit)):
                bowIdx = BoW.index(emailSplit[wordIdx])
                p[1][bowIdx] = p[1][bowIdx] + 1
                wham+=1
#normalize counts; convert absolute frequencies to relative ones
    for bowIdx in range(len(BoW)):
        p[0][bowIdx] =p[0][bowIdx]/wspam
        p[1][bowIdx] =p[1][bowIdx]/wham

    return len(BoW), BoW, p[0],p[1]


def classificador(a, b, valor, b_lexico, truePositive, trueNegative, falsePositive, falseNegative,X,Y,mTotal):
    classificacao = []
    classificacaoPredicted=[]
    classificacaoActual=[]

    n, vetorpalavras, vetorclassificadoSpam, vetorclassificadoHam = naiveBaiesTrain(X,Y)
    for i in range(len(a)):
        x = np.zeros(n)
        t = -b_lexico
        analise = a[i]  # mensagem que vai analisar
        analise = analise.split()
        for j in analise:
            if j in vetorpalavras:
                k= vetorpalavras.index(j)
                x[k] = x[k] + 1  # ler uma mensagem, conta as palavras que constam no lexus e essa conta é o xj
                t=t + 1 * (math.log10(vetorclassificadoSpam[k]) - math.log10(vetorclassificadoHam[k]))
               # t = t + x[k] * (math.log10(vetorclassificadoSpam[k]) - math.log10(vetorclassificadoHam[k]))

        if t> 0:
            classificacao.append("spam")
            classificacaoPredicted.append(0)

        else:
            classificacao.append("ham")
            classificacaoPredicted.append(1)

    for i in range(len(classificacao)):
        if b[i]=="spam":
            classificacaoActual.append(0)
        else:
            classificacaoActual.append(1)
        etiquetado = classificacao[i]
        etiqueta = b[i]
        if etiquetado == etiqueta:
            if etiquetado == "ham":
                truePositive[valor] = truePositive[valor] + 1
            else:
                trueNegative[valor] = trueNegative[valor] + 1
        else:
            if etiquetado == "ham":
                falsePositive[valor] = falsePositive[valor] + 1
            else:
                falseNegative[valor] = falseNegative[valor] + 1
    return truePositive, trueNegative, falsePositive, falseNegative,classificacaoActual,classificacaoPredicted


def metricas(truePositive, trueNegative, falsePositive, falseNegative):
    acc = (truePositive + trueNegative) / (truePositive + trueNegative + falsePositive + falseNegative)
    err = (falsePositive + falseNegative) / (truePositive + trueNegative + falsePositive + falseNegative)
    sn = truePositive / (truePositive + falseNegative)
    sp = trueNegative / (trueNegative + falsePositive)
    p = truePositive / (truePositive + falsePositive)
    r = truePositive / (truePositive + trueNegative)
    FM = 2 * p * r / (p + r)
    matrizconfusao = np.array([[truePositive, falsePositive], [falseNegative, trueNegative]])
    return acc, err, sn, sp, p, r, FM, matrizconfusao




def main_naive(X,Y,X_validacao,Y_validacao,X_teste,Y_teste,mham,mspam,total_hamspmClassification,total_hamspm_Test,total_hamspmTraining,mTotal):
    tempo_inicio = time.time()
    messageValidation(X,Y,X_validacao,Y_validacao,mham,mspam,total_hamspmClassification,mTotal)
    messageTest(X,Y,X_teste,Y_teste,mham,mspam,total_hamspm_Test,mTotal)
    c = [0.1,1,25,35,45,50,55,60,65,75,100]  # c = hiperparametro para classificar se é spam, pre determinar o valor

    truePositive = np.zeros(len(c))
    trueNegative = np.zeros(len(c))
    falsePositive = np.zeros(len(c))
    falseNegative = np.zeros(len(c))

    for valor in range(len(c)):
        b_lexico = math.log10(c[valor]) + math.log10(mham) - math.log10(mspam) # to offset the rejection treshold
        truePositive, trueNegative, falsePositive, falseNegative,classificacaoActual,classificacaoPredicted = classificador(X_validacao, Y_validacao, valor, b_lexico, truePositive, trueNegative, falsePositive, falseNegative,X,Y,mTotal)
    acertos = []
    for i in range(len(c)):
        acertos.append(truePositive[i] + trueNegative[i])
    i = acertos.index(max(acertos))

    valorC= f"{c[i]}"

    acc1, err1, sn1, sp1, p1, r1, FM1, matrizconfusao1 = metricas(truePositive[i], trueNegative[i], falsePositive[i], falseNegative[i])

    print(f" Para o conjunto de hiperparametro {c}, o  melhor desempenho está em C=", c[i],
          ", sendo as métricas desse código para o conjunto de validação:")
    print("Matriz de confusão: \n", matrizconfusao1)
    print(f"Accurancy: {acc1 * 100:.2f}%")
    print(f"Ratior Error: {err1 * 100 :.2f}%")
    print(f"Sensitivity: {sn1 * 100 :.2f}%")
    print(f"Specificity: {sp1 * 100 :.2f}%")
    print(f"Precision: {p1 * 100 :.2f}%")
    print(f"Recall: {r1 * 100 :.2f}%")
    print(f"F-Measure: {FM1 * 100 :.2f}%")
    print("Conhecendo o melhor hiperparametro, faz-se a classificacao das mensagens de teste, sendo suas métricas:")

    c = c[i]
    b_lexico = math.log10(c) + math.log10(mham) - math.log10(mspam) # to offset the rejection treshold
    valor = 0
    truePositive = np.zeros(1)
    trueNegative = np.zeros(1)
    falsePositive = np.zeros(1)
    falseNegative = np.zeros(1)
    truePositive, trueNegative, falsePositive, falseNegative,classificacaoActual,classificacaoPredicted= classificador(X_teste, Y_teste, valor, b_lexico, truePositive, trueNegative, falsePositive, falseNegative,X,Y,mTotal)

    acc2, err2, sn2, sp2, p2, r2, FM2, matrizconfusao2 = metricas(truePositive[0], trueNegative[0], falsePositive[0], falseNegative[0])

    print("Matriz de confusão : \n", matrizconfusao2)
    print(f"Accurancy: {acc2 * 100:.2f}%")
    print(f"Ratior Error: {err2 * 100 :.2f}%")
    print(f"Sensitivity: {sn2 * 100 :.2f}%")
    print(f"Specificity: {sp2 * 100 :.2f}%")
    print(f"Precision: {p2 * 100 :.2f}%")
    print(f"Recall: {r2 * 100 :.2f}%")
    print(f"F-Measure: {FM2 * 100 :.2f}%")

    tempo_fim = time.time()
    ExecutionTime = tempo_fim - tempo_inicio
    print(f"Tempo total de execução da classificação das mensagens por algoritmo de Naive Bayes: {ExecutionTime:.1f}s")
  #  plotConfusionMatrix(classificacaoActual,classificacaoPredicted)



    return f"{acc1 * 100:.2f}%", f"{err1 * 100 :.2f}%", f"{sn1 * 100 :.2f}%", f"{sp1 * 100 :.2f}%", f"{p1 * 100 :.2f}%", f"{r1 * 100 :.2f}%", f"{FM1 * 100 :.2f}%",f"{acc2 * 100:.2f}%", f"{err2 * 100 :.2f}%", f"{sn2 * 100 :.2f}%", f"{sp2 * 100 :.2f}%", f"{p2 * 100 :.2f}%", f"{r2 * 100 :.2f}%", f"{FM2 * 100 :.2f}%",f"{ExecutionTime:.2f}s",classificacaoActual,classificacaoPredicted, valorC



