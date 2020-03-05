from time import sleep
import os
import sys
from datetime import datetime


# Colors setting 
menuColor = '\033[44;1;37m'
clearColors = '\033[0;0m'
textColor = '\033[37m' 
logoColor = '\033[1;37m'
logoColorClear ='\033[0;0m'
errorColor = '\033[40;1;31m'
topColor = '\033[44;1;37m'
selectColor = '\033[46;1;37m'
statusColor = '\033[40;1;37m'
statusConColor = '\033[40;1;32m'
boxColor = '\033[1;37m'
colorVerde = '\033[1;32m'
colorVerdeBlack ='\033[40;1;32m'
colorVermelho ='\033[1;31m'
colorVermelhoBlack = '\033[40;1;31m'

# Spacing setting 
mainSpace = 17
divSpace = 8

# Infos App
bancoConnect = "ONLINE"
regAmount = "00000"
version = "Vr 1.0"

# Func mostra data
def clock():
    dataAtual = datetime.now()
    mostraData = dataAtual.strftime('%d/%m/%Y')
    return mostraData

# Desenha o Menu principal
def drawHome():
     #Global color setting variables 
    global menuColor, clearColors, mainSpace, textColor, divSpace, topColor, statusColor, statusConColor
     
    # Global status variables
    global bancoConnect, regAmount, version
    
    print(textColor+71 * " _"+clearColors)
    print(topColor+"|"+ mainSpace * " "+"  |"+ 120 * " "+" |"+clearColors)
    print(topColor+"|"+"       Menu   ", 4* " "+"|"+ 50 * " "+logoColor+"Agenda de Contatos"+clearColors+topColor+ 41 * " ", clock() , "|"+clearColors)
    print(topColor+"|_"+divSpace * " _"+" _|_"+ 59 * " _"+" _|"+clearColors )
    print(menuColor+"|"+ mainSpace * " "+"  |"+clearColors)
    print(menuColor+"|"+" Cadastrar [ 1 ]  "+" |"+clearColors)
    print(menuColor+"|_"+divSpace * " _"+" _|"+clearColors)
    print(menuColor+"|"+ mainSpace * " "+"  |"+clearColors)
    print(menuColor+"|"+" Consultar [ 2 ]  "+" |"+clearColors)
    print(menuColor+"|_"+divSpace * " _"+" _|"+clearColors)
    print(menuColor+"|"+ mainSpace * " "+"  |"+clearColors)
    print(menuColor+"|"+" Atualizar [ 3 ]  "+" |"+clearColors)
    print(menuColor+"|_"+divSpace * " _"+" _|"+clearColors)
    print(menuColor+"|"+ mainSpace * " "+"  |"+clearColors)
    print(menuColor+"|"+" Excluir   [ 4 ]  "+" |"+clearColors)
    print(menuColor+"|_"+divSpace * " _"+" _|"+clearColors)
    print(menuColor+"|"+ mainSpace * " "+"  |"+clearColors)
    print(menuColor+"|"+" Fechar    [ 5 ]  "+" |"+clearColors)
    print(menuColor+"|_"+divSpace * " _"+" _|"+clearColors)
    print(statusColor+"|"+ mainSpace * " "+"  |"+clearColors)
    print(f"{statusColor}| BANCO: {clearColors}{statusConColor}{bancoConnect}{clearColors}{statusColor}     |{clearColors}")
    print(f"{statusColor}| Registros: {clearColors}{statusConColor}{regAmount}{clearColors}{statusColor}  |{clearColors}")
    print(f"{statusColor}| Versão: {clearColors}{statusConColor}{version}{clearColors}{statusColor}    |{clearColors}")
    print(statusColor+"|_"+divSpace * " _"+" _|"+clearColors)
     
# Desenha o Menu de novo cadastro
def drawMenuRegister(data):
    
    # Global color setting variables
    global menuColor, clearColors, mainSpace, textColor, divSpace, topColor, selectColor, colorVerde
     
    # Global status variables
    global bancoConnect, regAmount, version
     
    print(textColor+71 * " _"+clearColors)
    print(topColor+"|"+ mainSpace * " "+"  |"+ 120 * " "+" |"+clearColors)
    print(topColor+"|"+"       Menu   ", 4* " "+"|"+ 45 * " "+logoColor+"Adcionar um novo Contato"+clearColors+topColor+ 40 * " ", clock() , "|"+clearColors)
    print(topColor+"|_"+divSpace * " _"+" _|_"+ 59 * " _"+" _|"+clearColors )
    print(f"{selectColor}| {mainSpace * ' '} |{clearColors}")
    print(f"{selectColor}| Cadastrar [ 1 ]   |{clearColors} {colorVerde}Nome Completo: {clearColors}{data[0]} {(50 - len(data[0])) * ' '} {colorVerde}Email: {clearColors}{data[1]}")
    print(selectColor+"|_"+divSpace * " _"+" _|"+clearColors)
    print(f"{menuColor}| {mainSpace * ' ' } |{clearColors} {colorVerde}Endereço: {clearColors}{data[2]} {(50 - len(data[2])) * ' '} {colorVerde}Cidade: {clearColors}{data[3]} {(30 - len(data[3])) * ' '} {colorVerde}Estado: {clearColors}{data[4]}")
    print(menuColor+"|"+" Consultar [ 2 ]  "+" |"+clearColors)
    print(f"{menuColor}|_{divSpace * ' _'} _|{clearColors} {colorVerde}Bairro: {clearColors}{data[5]} {(30 - len(data[5])) * ' '} {colorVerde}CEP: {clearColors}{data[6]} {(30 - len(data[6])) * ' '} {colorVerde}Numero: {clearColors}{data[7]}")
    print(menuColor+"|"+ mainSpace * " "+"  |"+clearColors)
    print(f"{menuColor}| Atualizar [ 3 ]   |{clearColors} {colorVerde}Telefone Residencial: {clearColors}{data[8]} {(20 - len(data[8])) * ' '} {colorVerde}Celular: {clearColors}{data[9]}" )
    print(menuColor+"|_"+divSpace * " _"+" _|"+clearColors)
    print(f"{menuColor}| {mainSpace * ' '} |{clearColors} {colorVerde}Data de Nascimento: {clearColors}{data[10]}")
    print(menuColor+"|"+" Excluir   [ 4 ]  "+" |"+clearColors)
    print(f"{menuColor}|_{divSpace * ' _' } _|{clearColors} ")
    print(menuColor+"|"+ mainSpace * " "+"  |"+clearColors)
    print(menuColor+"|"+" Fechar    [ 5 ]  "+" |"+clearColors)
    print(menuColor+"|_"+divSpace * " _"+" _|"+clearColors)
    print(statusColor+"|"+ mainSpace * " "+"  |"+clearColors)
    print(f"{statusColor}| BANCO: {clearColors}{statusConColor}{bancoConnect}{clearColors}{statusColor}     |{clearColors}")
    print(f"{statusColor}| Registros: {clearColors}{statusConColor}{regAmount}{clearColors}{statusColor}  |{clearColors}")
    print(f"{statusColor}| Versão: {clearColors}{statusConColor}{version}{clearColors}{statusColor}    |{clearColors}")
    print(statusColor+"|_"+divSpace * " _"+" _|"+clearColors)

# Desenha a caixa para salvamento de dados
def drawBoxSave(data):
    global boxColor, clearColors, colorVerde, colorVermelho, colorVerdeBlack, colorVermelhoBlack
    center = 50
    os.system('clear')
    print(textColor+71 * " _"+clearColors)
    print(topColor+"|"+ mainSpace * " "+"  |"+ 120 * " "+" |"+clearColors)
    print(topColor+"|"+"       Menu   ", 4* " "+"|"+ 45 * " "+logoColor+"Adcionar um novo Contato"+clearColors+topColor+ 40 * " ", clock() , "|"+clearColors)
    print(topColor+"|_"+divSpace * " _"+" _|_"+ 59 * " _"+" _|"+clearColors )
    print(f"{selectColor}| {mainSpace * ' '} |{clearColors}")
    print(f"{selectColor}| Cadastrar [ 1 ]   |{clearColors} {colorVerde}Nome Completo: {clearColors}{data[0]} {(50 - len(data[0])) * ' '} {colorVerde}Email: {clearColors}{data[1]}")
    print(selectColor+"|_"+divSpace * " _"+" _|"+clearColors)
    print(f"{menuColor}| {mainSpace * ' ' } |{clearColors} {colorVerde}Endereço: {clearColors}{data[2]} {(50 - len(data[2])) * ' '} {colorVerde}Cidade: {clearColors}{data[3]} {(30 - len(data[3])) * ' '} {colorVerde}Estado: {clearColors}{data[4]}")
    print(menuColor+"|"+" Consultar [ 2 ]  "+" |"+clearColors)
    print(f"{menuColor}|_{divSpace * ' _'} _|{clearColors} {colorVerde}Bairro: {clearColors}{data[5]} {(30 - len(data[5])) * ' '} {colorVerde}CEP: {clearColors}{data[6]}")
    print(menuColor+"|"+ mainSpace * " "+"  |"+clearColors)
    print(f"{menuColor}| Atualizar [ 3 ]   |{clearColors} {colorVerde}Telefone Residencial: {clearColors}{data[7]} {(20 - len(data[7])) * ' '} {colorVerde}Celular: {clearColors}{data[8]}" )
    print(menuColor+"|_"+divSpace * " _"+" _|"+clearColors)
    print(f"{menuColor}| {mainSpace * ' '} |{clearColors} {colorVerde}Data de Nascimento: {clearColors}{data[9]}")
    print(menuColor+"|"+" Excluir   [ 4 ]  "+" |"+clearColors)
    print(f"{menuColor}|_{divSpace * ' _' } _|{clearColors} ")
    print(menuColor+"|"+ mainSpace * " "+"  |"+clearColors)
    print(menuColor+"|"+" Fechar    [ 5 ]  "+" |"+clearColors)
    print(menuColor+"|_"+divSpace * " _"+" _|"+clearColors)
    print(statusColor+"|"+ mainSpace * " "+"  |"+clearColors+28 * "_ "+clearColors)
    print(f"{statusColor}| BANCO: {clearColors}{statusConColor}{bancoConnect}{clearColors}{statusColor}     |{55 * ' '}|{clearColors}")
    print(f"{statusColor}| Registros: {clearColors}{statusConColor}{regAmount}{clearColors}{statusColor}  |               Os dados estão corretos?{16 * ' '}|{clearColors}")
    print(f"{statusColor}| Versão: {clearColors}{statusConColor}{version}{clearColors}{statusColor}    | Para gravar {clearColors}{colorVerdeBlack}S{clearColors}{statusColor}(Sim) ou para digitar novamente{clearColors}{colorVermelhoBlack} N{clearColors}{statusColor}(Não)   |{clearColors}")
    print(statusColor+"|_"+divSpace * " _"+" _|"+27 * "_ "+"_|"+clearColors)
    
    # print("\n")
    # print(boxColor+51 * " "+28 * "_ ")
    # print(center * " "+"|"+55 * " "+"|")
    # print(center * " "+"|               Os dados estão corretos?"+16 *" "+"|") 
    # print(center * " "+"| Para gravar "+clearColors+colorVerde+"S"+clearColors+boxColor+"(Sim) ou para digitar novamente "+clearColors+colorVermelho+"N"+clearColors+boxColor+"(Não)   |")
    # print(center * " "+"|"+27 * "_ "+"_|"+clearColors)
    print(colorVerde,end=" ")
    op = input("                    Digite a opção: ")
    print(clearColors)
    return op   

# Desenha a caixa de Registrando
def drawBoxRec(data):
    global colorVerde, clearColors
    os.system('clear') 
    drawMenuRegister(data)
    i = 0
    for i in range (1, 11):
        
        sys.stdout.write(colorVerde+"\r                     Registrando {}0%".format(i))
        sys.stdout.flush()
        sleep(0.1)
    print(clearColors)

# Desenha a caixa de opção invalida
def drawOpInvalidate():
    global colorVermelho, clearColors
    print(30 * " "+colorVermelho+"Opcão invalida Digite S ou N"+clearColors)
    
# Desenha a caixa de opção invalida no menu Home
def drawOpIvalidateHome():
    global errorColor, clearColors
    spaceFortyTwo = 42
    spaceTwenty = 20
    spacetForty = 40
    print(spaceFortyTwo * " "+errorColor+spaceTwenty*" "+spacetForty* "-"+spaceTwenty*" "+clearColors)
    print(spaceFortyTwo * " "+errorColor+spaceTwenty*" "+"|"+" Opção Invalidade, tente novamente :D |"+spaceTwenty*" "+clearColors)
    print(spaceFortyTwo * " "+errorColor+spaceTwenty*" "+spacetForty* "-"+spaceTwenty*" "+clearColors)
    sleep(1)
    os.system('clear')
    
# Desenha a caixa não é um numero    
def drawOpIsNotNumber():
    global errorColor, clearColors
    spaceFortyTwo = 42
    spaceTwenty = 20
    spacetFortyOne = 41
    print(spaceFortyTwo * " "+errorColor+spaceTwenty*" "+spacetFortyOne* "-"+spaceTwenty*" "+clearColors)
    print(spaceFortyTwo * " "+errorColor+spaceTwenty*" "+"|"+" Isso não é número, tente novamente :D |"+spaceTwenty*" "+clearColors)
    print(spaceFortyTwo * " "+errorColor+spaceTwenty*" "+spacetFortyOne* "-"+spaceTwenty*" "+clearColors)
    sleep(1)
    os.system('clear')
    

def drawNameInvalid():
    global colorVermelhoBlack, clearColors
    print(60 * " "+colorVermelhoBlack+"!!! Erro !!!\n"+clearColors+"\n"+
          30 * " "+colorVermelhoBlack+"Nome deve conter somente letras e não pode ser vazio (acentos são permitidos)"+clearColors)
    
def drawEmailInvalid():
    global colorVermelhoBlack, clearColors
    print(60 * " "+colorVermelhoBlack+"!!! Erro !!!\n"+clearColors+"\n"+
          40 * " "+colorVermelhoBlack+"Email informado é invalido Exemplo: fulano@detal.com"+clearColors)