# Menu
from time import sleep
import os
import sys
from datetime import datetime
from .drawMenu import *
from .validateData import *

# Variables
data = ["","","","","","","","","","","",""]
        

def main():
    # colorVerdeE = '\033[1;32m' 
    # clearColorsE = '\033[0;0m'
    while True:
        os.system('clear')
        drawHome() 
        try:
            print('\033[1;32m',end=" ")
            op = int(input("                    Escolha uma opção: "))
            print('\033[0;0m')
            if op == 1:
                os.system('clear')
                mainRegister()
                main()
            elif op == 2:
                os.system('clear')
            elif op == 3:
                os.system('clear')
            elif op == 4:
                os.system('clear')
            elif op == 5:
                os.system('clear')
                sys.exit()
            else:
                drawOpIvalidateHome()
        except  ValueError:
            drawOpIsNotNumber()
   
        
def mainRegister():
    # Variavel global 
    global data
    
    # Inserir os dados 
    reg = True
    while reg:
        for i in range(len(data)):
            os.system('clear')
            drawMenuRegister(data) # Desenha o menu de cadastro
            if data[i] == data[0]:
                data[i] = validateName(data)
                os.system('clear')
            if data[i] == data[1]:
                data[i] = validateEmail(data)
                os.system('clear')
            if data[i] == data[2]:
                data[i] = input("Endereço (Rua ou Av): ")
                os.system('clear')
            if data[i] == data[3]:
                data[i] = input("Cidade: ")
                os.system('clear')
            if data[i] == data[4]:
                data[i] = input("Estado: ")
                os.system('clear')
            if data[i] == data[5]:
                data[i] = input("Bairro: ")
                os.system('clear')
            if data[i] == data[6]:
                data[i] = input("CEP: ")
                os.system('clear')
            if data[i] == data[7]:
                data[i] = input("Numero: ")
                os.system('clear')
            if data[i] == data[8]:
                data[i] = input("Telefone Residencial: ")
                os.system('clear')
            if data[i] == data[9]:
                data[i] = input("Celular: ")
                os.system('clear')
            if data[i] == data[10]:
                data[i] = input("Data de Nascimento: ")
                os.system('clear')
                
        #  escolha gravar no banco de dados se os dados estiverem corretos, ou digitar novamente se estiver errado        
        rec = True
        while rec: 
                os.system('clear') 
                drawMenuRegister(data) # Desenha o menu de cadastro
                toSave = drawBoxSave(data)
                if toSave == "S" or toSave == "s":
                    data.pop(11)    
                    dataRec = data  # Essa Variavel para passar para o inserir no banco 
                    drawBoxRec(data)           
                    data = ["","","","","","","","","","","",""]
                    reg = False
                    rec = False
                    return main()
                elif toSave == "N" or toSave == "n":
                        data = ["","","","","","","","","","","",""]
                        rec = False
                        mainRegister()
                else:
                        drawOpInvalidate()
                        sleep(1)
                        
            
    
            
 
    

    