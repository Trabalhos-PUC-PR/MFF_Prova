import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

print("Todas as questões estão em ordem no questões.png")
escolha = int(input("Escolha a Questão (1-6):"))
if(escolha>6 or escolha<1):
    exit("Questão não existente")

'''-------------------------------------------------------------QUESTÃO 1'''
if(escolha==1):
    x = sp.Symbol('x')
    def limite1():
        return (x**3)/((x+1)**2)

    limite = sp.limit(limite1(), x, -1, dir="-")
    print(limite)

'''-------------------------------------------------------------QUESTÃO 2'''
if(escolha==2):
    pH = 1.7
    ions = (10 ** -pH) #https://brainly.com.br/tarefa/283793 eu pesquisei no brainly desculpa
    print("A concentração de íons de hidrogênio no Suquinh de Limão é ",ions)

'''-------------------------------------------------------------QUESTÃO 3'''
if(escolha==3):
    def funcao1():
        return x+2/(x+3)

    x = np.arange(-3, -1, 0.1)
    plt.plot(x, funcao1())
    plt.show();

'''-------------------------------------------------------------QUESTÃO 4'''
if(escolha==4):
    print(sp.limit(((1+(1/x))**(3*x)), x, sp.oo))

'''-------------------------------------------------------------QUESTÃO 5'''
if(escolha==5):
    exit("Questão Anulada :/ ");
#ANULADA, mas ela tende a 1

'''-------------------------------------------------------------QUESTÃO 6'''
if(escolha==6):
    #desenvolvendo a equação
    #P = 100*2**(tempo/15)
    #300/100 = sqrt(2**t)
    #(300/100)**15= 2**t
    #log2((300/100)**15) = t

    tempo = np.log2((300/100)**15)
    print(tempo)