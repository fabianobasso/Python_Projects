# Funções de validação de dados 
from time import sleep
import os
from .drawMenu import *

# Validation lists 
numbers = ['0','1','2','3','4','5','6','7','8','9']
specialCharacters = ['!','@','#','$','%','&','*','(',')','-','_','+','=',';','.','<','>',':','/','?','~','^',']','[','{','}','´','`','"','|','\\','\'','\"']
aroba = ['@','.']

# text formatting
spceOp = 20

def validateName(data):
    opName = True
    global numbers, specialCharacters, spceOp
    while opName:
        os.system('clear')
        drawMenuRegister(data)
        print('\033[1;32m'+spceOp * " ",end=" ")
        name = input("Digite Nome Completo: ")
        print('\033[0;0m')
        num = 0
        
        
        for i in range(len(name)):
            letter = name[i]
            if letter in numbers:
                num+=1
            if letter in specialCharacters:
                num+=1
            
        if num == 0 and name != "" and name != " ":    
            opName = False
        else:
            drawNameInvalid()
            sleep(3)
            
    return name

def validateEmail(data):
    opEmail = True
    global aroba, spceOp
    while opEmail:
        os.system('clear')
        drawMenuRegister(data)
        print('\033[1;32m'+spceOp * " ",end=" ")
        email = input("Digite Email: ")
        print('\033[0;0m')
        num = 0
    
        for i in range(len(email)):
            letter = email[i]
            if letter in aroba:
                num+=1
        
        if num >= 2 and email != "" and email != " ":    
            opEmail = False
        else:
            drawEmailInvalid()
            sleep(3)
            
    return email            