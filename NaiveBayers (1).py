
# coding: utf-8

# In[1]:


import pandas as pd

import numpy as np

import nltk

import numpy as np

# Stopwords
from nltk.corpus import stopwords


# In[4]:


text = pd.read_csv('chennai_reviews.csv', sep=',') #ler aquivo de dados e guarda nessa variavel text. ele tem que tá na mesma pasta do codigo
text.head() #ajusta o texto de acordo com o cabeçalho
print(type(text)) #tipo da base. Vale notar que o text é do tipo list pandas. então as operações de listas valem pra ele
print(text) #mostra a base de dados


padroes = [] #vetor de que vai guardar as mensagens
dicionario = []

print(len(text))

#aqui to retirando da base os comentários e os sentimentos e guardadndo no vetor padroes. tambem to fazendo o dicionario
for i in range(len(text)):
    #para pegar determinado dado de determinado tipo na base voce faz nome da base.tipo de dado[posicao dele]. tipo "text.Review_Text[0]
    if(len(str(text.Sentiment[i])) ==1): #verifica se os dados de sentimentos são só numeros 1, 2 ou 3 e se for...
        x = str(text.Review_Text[i]).split() #pega cada comentário na base de dados o separa em palavras, converte para string e guarda numa lista
        dicionario = dicionario + x #pega essas palavras e joga no vetor dicionario
        padroes.append(str(text.Review_Text[i]).split()) #também joga esse comentario separado em strings no vetor padroes
        padroes[len(padroes)-1].insert(0,str(text.Sentiment[i])) #joga o sentimento desse comentario nele tambem


print (len(dicionario))
unicos = list(set(dicionario)) #aqui pega o dicionario e retira as palavras repetidas.
#print(unicos)


# In[5]:


import random

treino = []
teste = []

lista = list(range(len(padroes)))
random.shuffle(lista)
print(len(padroes))
x=0
for i in lista:
    if (x < int(len(lista)*0.8)):
        treino.append(padroes[i])
    else:
        teste.append(padroes[i])
    
    x+=1
    
print(len(teste))
print(len(treino))

#print(teste)


# In[6]:


#etapa de treinamento
print (treino[0])


vetor_resultados = [] #guarda todos os vetores das ocorrencias das palavras do dicionario

for j in range(len(treino)): #itera na quantidade de frases no vetor de treino
    vetor_ocorrencia = [] #para cada palavra do dicionario, guarda 0 se ela não ta na frase e 1 se ela ta na frase

    for i in unicos: #itera no dicionario
        var = 0
        for x in range(len(treino[j])):
            #print (treino[j][x])
            if (i == treino[j][x]):
                #print(i +"\t"+treino[j][x])
                var = 1;
        if (var == 1):
            vetor_ocorrencia.append(1)
        else:
            vetor_ocorrencia.append(0)
    vetor_resultados.append(vetor_ocorrencia)
   # break

#print(vetor_ocorrencia)


# In[7]:


print(unicos[50])
#vetor_ocorrencia[50]
#print(vetor_resultados[0])


# In[8]:


# calculo da porcentagem de sentimento de cada palavra

soma_total = np.zeros(len(unicos))

soma_positivo = np.zeros(len(unicos))

for i in vetor_resultados:
    soma_total = soma_total + np.array(i)

    
for i,j in zip(treino, vetor_resultados):
    if (i[0] == '3'):
        soma_positivo = soma_positivo + np.array(j)


# In[99]:


print (soma_positivo[0])


# In[100]:


print(soma_total[0])


# In[9]:


#calcula a taxa de comentarios positivos em porcento para cada palavra
a = soma_positivo / (soma_total+0.01)
#print(list(a))


# In[10]:



#etapa de teste. transfroma os comentarios em vetor de 0 e 1
print (teste[0])


vetor_resultados_teste = [] #guarda todos os vetores das ocorrencias das palavras do dicionario

for j in range(len(teste)): #itera na quantidade de frases no vetor de treino
    vetor_ocorrencia_teste = [] #para cada palavra do dicionario, guarda 0 se ela não ta na frase e 1 se ela ta na frase

    for i in unicos: #itera no dicionario
        var = 0
        for x in range(len(teste[j])):
            #print (treino[j][x])
            if (i == teste[j][x]):
                #print(i +"\t"+treino[j][x])
                var = 1;
        if (var == 1):
            vetor_ocorrencia_teste.append(1)
        else:
            vetor_ocorrencia_teste.append(0)
    vetor_resultados_teste.append(vetor_ocorrencia_teste)
   # break

#print(vetor_ocorrencia)


# In[27]:


acertos = 0
quant_pos = 0
quant_neg = 0
erros = 0
for i, y in zip(vetor_resultados_teste, teste): #para cada comentario
    pos = 1
    neg = 1 
    
    for j, x in zip(i, a):
        if (j == 1):
            pos = x * pos
            neg = (1-x) * neg
            
    if (pos > neg):
        quant_pos += 1
        
        if (int(y[0]) == 3):
            acertos += 1
        else:
            erros += 1
    if (neg > pos):
        quant_pos += 1
        
        if(int(y[0]) != 3):
            acertos += 1
        else:
            erros += 1
    
    '''      
    if (pos > neg and int(y[0]) == 3):
        acertos+=1
        print("*******positivo***************\n", y)
    if (neg > pos and int(y[0]) != 3):
        acertos+=1
        print("*************negativo***************\n", y)''' 


# In[28]:


print(acertos)
print(len(teste))
print(erros)


# In[29]:


len(padroes)

