# -*- coding: utf-8 -*-

#Utilizado para interagir com  API
import requests

#utilizado para Manipular os Dados JSON
import json

#Realizando a Criação da Tabela no Banco de Dados
import Connection

#Utilizado para o Banco de Dados
import sqlite3

#Biblioteca para realizar marcaçoes no grafico
import matplotlib.pyplot as plt

#Conexão com Banco 
conn = sqlite3.connect('climatempo.db')
cursor = conn.cursor()

id = 0
cidade = ""
estado = ""
pais = ""
dia = range(15)
Temp_Max = range(15)
Temp_Min = range(15)

def menu():
    escolha = int(input('''------------------------------------------
|                  Menu                  |
|----------------------------------------|
|1 - Cadastrar Cidades                   |
|2 - Consultar Cidades                   |
|3 - Consultar Graficos                  |
|4 - Sair	                         |
|                                        |
|Escolha                                :|'''))
    
    print "|----------------------------------------|\n"
    if escolha == 1:
        print '''******************************************
|Informe a Cidade e o Estado (1 POR VEZ) |
******************************************'''
        pegar_Dados_Cidade()
    elif escolha == 2:
        ver_Cidades()
    elif escolha == 3:
        buscar_Cidade()
    elif escolha == 4:
        exit()
    else:
        print('Escolha invalida, tente novamente')
        menu()
    
def pegar_Dados_Cidade():
    
    cidade_Usuario = ""
    cidade_Usuario = raw_input('''------------------------------------------
|Entre Com o Nome da Cidade             :|''')
    cidade_Usuario.lower().capitalize()

    estado_Usuario = ""
    estado_Usuario = raw_input('''|----------------------------------------|
|Entre Com a Sigla do Estado            :|''')
    estado_Usuario.upper()

    print "|----------------------------------------|\n"
    
    #Pesquisar o Id da Cidade
    response1 = requests.get('''http://apiadvisor.climatempo.com.br/api/v1/locale/city?name='''+cidade_Usuario+'''&state=''' + estado_Usuario+ '''&token=e9b8d9b0218493cf369ff9a26b807d08''')
    data1 = json.loads(response1.content)

    if not data1:
        print '''******************************************
|          Cidade Nao Encontrada         |
******************************************'''
        pegar_Dados_Cidade()
    else:
        for id_Cidade in data1:
            id_Cidade = id_Cidade["id"]

        response2 = requests.get('''http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/'''+str(id_Cidade)+'''/days/15?token=e9b8d9b0218493cf369ff9a26b807d08''')

        data2 = json.loads(response2.content)
        
        id = data2.get("id")

        cidade = data2.get("name")

        estado = data2.get("state")

        pais =  data2.get("country")

    #pegando a estrutura de 1 dia de 0 ate 14
    #pegando: date_br, temperature(max e min)

        i = 0
    
        for i in range(0,15):
        
            dia[i] = json.dumps(data2.get("data")[i]["date_br"])
            diaN[i] = dia[i][1:-6]
            Temp_Max[i] = json.dumps(data2.get("data")[i]["temperature"]["max"])
            Temp_Min[i] = json.dumps(data2.get("data")[i]["temperature"]["min"])
            i += 1

    #Cadastrando no banco a cidade escolhida com suas 15 previsões
        for i in range(0,15):        
            cursor.execute('''
            Insert into climatempo (id, cidade, estado, pais, data, tempMax, tempMin)
            values(?,?,?,?,?,?,?)
            ''',(id ,cidade, estado, pais, diaN[i], Temp_Max[i], Temp_Min[i]))
        conn.commit();
        i += 1

        print '''******************************************
|      Cidade Cadastrada Com Sucesso     |
******************************************'''
        return menu()
    
def ver_Cidades():
    cidades = []
    for linha in cursor.execute("Select cidade from climaTempo"):            
        if linha not in cidades:
            cidades.append(linha)
        cidades.sort()

    if len(cidades) == 0:
        print '''******************************************
|        Nenhuma Cidade Cadastrada       |
******************************************'''
        menu()    
    else:
        print '''******************************************
|       As Cidades Cadastradas Sao:      |
******************************************'''
        for i in range(len(cidades)):
            print cidades[i]
        print "******************************************"
        menu()

def buscar_Cidade():

     print '''******************************************
|Informe as Cidades para Serem Comparadas|
******************************************'''
    cidade1 = ""
    cidade1 = raw_input('''------------------------------------------
|Entre Com a Primeira Cidade:            |''')
    cidade1.lower().capitalize()

    cidade2 = ""
    cidade2 = raw_input('''------------------------------------------
|Entre Com a Segunda Cidade :            |''')
    cidade2.lower().capitalize()

    print "|----------------------------------------|\n"
    
    data1 = []
    temp_Max1 = []
    temp_Min1 = []

    data2 = []
    temp_Max2 = []
    temp_Min2 = []
    
    for linha in cursor.execute("Select * from climaTempo where cidade = '%s'" %cidade1):
    
        data1.append(linha[4])
        temp_Max1.append(linha[5])
        temp_Min1.append(linha[6])
    print temp_Min1
    for linha in cursor.execute("Select * from climaTempo where cidade = '%s'" %cidade2):
        
        data2.append(linha[4])
        temp_Max2.append(linha[5])
        temp_Min2.append(linha[6])
        
    #Mudando Cor BackGroud
    fig = plt.figure()
    rect = fig.patch
    rect.set_facecolor('w')

    #Criando Grafico da Primeira Cidade 
    ax1 = fig.add_subplot(2,1,1, facecolor = 'grey')
    ax1.plot(data1, temp_Max1, 'ro', linewidth = 1.5, linestyle = '-.', label = 'Temperatura Maxima')
    ax1.plot(data1, temp_Min1, 'bo', linewidth = 1.5, linestyle = '--', label = 'Temperatura Minima')
    ax1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    ax1.set_xlabel("Data")
    ax1.set_ylabel("Temperatura\n" + cidade1)

    #Criando Grafico da Primeira Cidade 
    ax2 = fig.add_subplot(2,1,2, facecolor = 'grey')
    ax2.plot(data2, temp_Max2, 'ro', linewidth = 1.5, linestyle = '-.', label = 'Temperatura Maxima')
    ax2.plot(data2, temp_Min2, 'bo', linewidth = 1.5, linestyle = '--', label = 'Temperatura Minima')
    ax2.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    ax2.set_xlabel("Data")
    ax2.set_ylabel("Temperatura\n"+ cidade2)
    
    plt.show()
    return menu()
  
menu()
