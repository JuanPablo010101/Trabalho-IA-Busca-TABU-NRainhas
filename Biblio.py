
import queue
from random import randint
from collections import deque
import random
import time
import matplotlib.pyplot as pyplot

def plot_interactions_vs_fitness(interactions, fitness_values):
    """
    Plota uma lista de interações em relação a uma lista de valores de fitness.

    :param interactions: Lista de números inteiros representando as interações.
    :param fitness_values: Lista de valores de fitness correspondentes às interações.
    """
    pyplot.figure(figsize=(10, 6))
    pyplot.plot(interactions, fitness_values, marker='', linestyle='-')
    pyplot.title('Interação vs. Fitness')
    pyplot.xlabel('Interação')
    pyplot.ylabel('Fitness')
    pyplot.grid(True)
    pyplot.show()

# def grafico(num):
#     Listainicial=[]
#     Histo=[]
#     Listainicial=geraposicao(Listainicial.copy(),num)
#     print("--------------------------------------")
#     print(f'Tabuleiro: {len(Listainicial)}')
#     print(f'Lista Inicial: {Listainicial} fitness:{achaFitness(Listainicial )}')
#     tempo=time.time()
#     [Listainicial,Histo]=Busca(Listainicial.copy(),num,2)
#     print(f"Melhor posição: {Listainicial} fitness:{achaFitness(Listainicial)}")
#     tempo=(time.time() -tempo)
#     print(f'Time: {tempo}')
#     print("--------------------------------------")
#     Listainicial.clear()
#     return tempo



#TROCA OS ELEMENTOS DE POSIÇÃO
def Trocaelemet(Lista,pos,pos1):
    aux=Lista[pos]
    Lista[pos]=Lista[pos1]
    Lista[pos1]=aux
    return Lista

#GERA UM VALOR ALEATORIO DENTRO DE UM INTERVALO DEFINIDO EX[1:8]
def geravalor(MaxNumero:int , MinNumero =1):
    return randint(MinNumero, MaxNumero)

#GERA UMA LISTA DE VALORES ALEATORIOS SEM REPETIR
def geraposicao(lista,numero): # gera posição inicial aleatoria para as rainhas
        """Gera novas posições para os numeros de rainhas"""
        MaxNumero = numero
        #lista.__len__() 
        #lista.append(1)
        while(len(lista)< MaxNumero):
            numGerado = geravalor(MaxNumero)
            if numGerado not in lista:
                lista.append(numGerado)
        return lista

#ACHA OS VALORES DA DIAGONAL POSITIVA PARA DESCOBRIR SE AS RAINHAS ESTÃO COLIDINDO
def diagoPositiva(i,Si):
    k= i -Si
    return k

#ACHA OS VALORES DA DIAGONAL NEGATIVA PARA DESCOBRIR SE AS RAINHAS ESTÃO COLIDINDO
def diagoNegativa(i,Si):
    k=i+Si
    return k

# CALCULA O FITNESS PARA DAS RAINHAS QUE ESTÃO COLIDINDO, PARA ENCONTRAR A MELHOR SOLUÇÃO
def achaFitness(Lista):
    DiagonalPositiva=[] # lISTA DOS VALORES DA DIAGONAL POSITIVA
    DiagonalNegativa=[]# lISTA DOS VALORES DA DIAGONAL NEGATIVA
    fitness:int  # DECLARO A VARIAVEL INTEIRA QUE SERA RETORNADA DENTRO DA FUNÇÃO

    for index in range(0,len(Lista)): #-1
        #PASSO A COLUNA QUE SE ENCONTRA A RAINHA
        SiP=Lista[index] 
        SiN=Lista[index]        
        DiagonalPositiva.append(diagoPositiva(index,SiP)) #INSIRO NA LISTA DIAGONAL POSITIVA OS VALORES CALCULADOS
        DiagonalNegativa.append(diagoNegativa(index,SiN)) #INSIRO NA LISTA DIAGONAL NEGATIVA OS VALORES CALCULADOS

#PEGO O TAMANHO MAXIMO DA LISTA DE DIAGONAL E SUBTRAIO COM O TAMANHO DA MESMA LISTA SEM VALORES REPETIDOS 
    fitness=(len(DiagonalPositiva)- len(set(DiagonalPositiva))) 
    fitness=fitness + len(DiagonalNegativa)- len(set(DiagonalNegativa))
    return fitness  

#GERO UMA LISTA DE COMBINAÇÕES POSSIVEIS SEM REPETIR, PARA REALIZAR A TROCA DE POSIÇÕES DA RAINHA
def combinacao(Lista:list):
    lista=[] #Lista Vazia de combinações possiveis
    tamanho=len(Lista)
    for index in range(0,tamanho):
        for j in range(0,tamanho):
            if((index!=j) and (index<j)):
                lista.append((index,j))
    return lista
    

#ENCONTRO A MELHOR SOLUÇÃO DE TROCA, DADA AS POSIÇÕES DA RAINHA
def MelhorSequenciaV2(Lista, Tabu, combina):
    mostrar = False
    aux = True
    # Quero realizar a troca dos elementos da lista com as combinações disponíveis na lista
    vizinhos = []
    MesmaFitness = []
    Tupla = []

    for i in range(0, len(combina)):
        vizinho = Trocaelemet(Lista.copy(), combina[i][0], combina[i][1])
        vizinhos.append(vizinho)

    if mostrar:
        print(f"Vizinhos: {vizinhos}")
        print(f"Combinação: {combina}")
    
    for index, vizinho in enumerate(vizinhos):
        vizinho_fitness = achaFitness(vizinho)
        if vizinho_fitness < achaFitness(Lista):
            # Retirar das combinações possíveis
            # E Pôr em Tabu
            Tabu.append(combina[index])
            combina.pop(index)
            aux = False

            if mostrar:
                print("Menor")
                print(f"Tabu: {Tabu}")
                print(f"Combinação Removida: {combina}")
                print(f"Lista FINAL: {vizinho}")

            Lista = vizinho  # Atualiza a lista com o novo vizinho encontrado
            return Lista

        if vizinho_fitness == achaFitness(Lista):
            MesmaFitness.append(vizinho)
            Tupla.append(combina[index])

    # CASO NENHUM DOS VALORES SEJA MENOR, IREMOS SORTEAR UM DE MESMO FITNESS
    # PARA QUE NÃO ENTRE EM UM LOOP DE MESMA SOLUÇÃO
    if aux and len(MesmaFitness) > 0:
        chosen_vizinho = random.choice(MesmaFitness)
        chosen_index = vizinhos.index(chosen_vizinho)
        Tabu.append(combina[chosen_index])
        combina.pop(chosen_index)
        
        if mostrar:
            print("Igual")
            print(f"Tabu: {Tabu}")
            print(f"Combinação Removida: {combina}")
            print(f"Lista Final: {chosen_vizinho}")

        Lista = chosen_vizinho  # Atualiza a lista com o vizinho escolhido
    return Lista

#REALIZO A BUSCA DE ENCONTRAR A MELHOR  SOLUÇÃO DAS RAINHAS
def Busca(Lista,cont,contTabu):
    historico=[]
    i=[]
    TABU=deque()
    comb=[]
    comb=combinacao(Lista.copy())
    contador=0 # VARIAVEL RESPONSAVEL POR CONTAR OS LAÇOS 
    #CRIA UM LOOP
    while((contador<cont) and (achaFitness(Lista)!=0)):
    
        #ACHO NOVOS VALORES
        if(achaFitness(Lista)!=0):
            Lista=MelhorSequenciaV2(Lista.copy(),TABU,comb)
            i.append(contador+contTabu)
       
        
        #tiro a penalidade
        if(len(TABU)>0):
            if(len(i)>0 and contador in i):
                
                comb.append(TABU.popleft())
                i.remove(contador)
               # print(f"TABU Removido: {TABU}")
      
        
        contador+=1
        historico.append(achaFitness(Lista))
        
    print("Interaçao: ",contador)
    return [Lista,historico]

exibir= False
if(exibir==True):
    Lista=[5, 7, 2, 3, 4, 1, 6]
    Tamanho=len(Lista)
    print(f"Lista Inicial: {Lista}")
    print(f"Fitness Inicial: {achaFitness(Lista)}")

    #Tabu=deque()
    Lista=Busca(Lista.copy(),200,4)
    print(f"Lista Final: {Lista}")
    print(f"Fitness Final: {achaFitness(Lista)}")

    for i in range(Tamanho):
        for j in range(Tamanho):
            if(i==0 and j==0 or j==0):
                print('|',end='')
            if(j<Tamanho and Lista[i]!=j+1):
                print('O|',end='')
            if(j<Tamanho and Lista[i]==j+1):
                print('X|',end='')
            if(j==Tamanho and Lista[i]==j+1):
                print('x|',end='')
            if(j==Tamanho and Lista[i]!=j+1):
                print('O|',end='')
            
        print('')

def Menu(Tamanho,ContTabu,interacao):
    # LISTA VAZIA INICIAL
    Lista=[]
    Historico=[]
    # GERA UMA LISTA ALEATORIA DO TAMANHO DEFINIDO INICIAL
    Lista=geraposicao(Lista.copy(),Tamanho)
    print(f"Posição Inicial:{Lista} Fitness Inicial: {achaFitness(Lista)}")

    NovaLista=[] # LISTA VAZIA FINAL
    tempo=time.time()
    [NovaLista,Historico]=Busca(Lista,interacao,ContTabu) # RETORNA A MELHOR SOLUÇÃO PARA LISTA FINAL
    print(f"Melhor posição: {NovaLista} fitness:{achaFitness(NovaLista)}")
    tempo=(time.time() -tempo)
    print(f"Tempo: {tempo}")

    # IMPRIME UM TABULEIRO 
    if(Tamanho<=50):
        for i in range(Tamanho):
            for j in range(Tamanho):
                if(i==0 and j==0 or j==0):
                    print('|',end='')
                if(j<Tamanho and NovaLista[i]!=j+1):
                    print('O|',end='')
                if(j<Tamanho and NovaLista[i]==j+1):
                    print('X|',end='')
                if(j==Tamanho and NovaLista[i]==j+1):
                    print('x|',end='')
                if(j==Tamanho and NovaLista[i]!=j+1):
                    print('O|',end='')
            
            print('')
    valores=[]
    for i in range(0,len(Historico)):
        valores.append(i)

    # FUNÇÃO PARA PLOTAR O GRAFICO

    plot_interactions_vs_fitness( valores,Historico)
    
#lista=[]
#lista=geraposicao(lista,7)
#print(f"lista: {lista}")