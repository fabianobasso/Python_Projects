"""
    Programa para fazer cadastro de pessoas usando MySQL em python 
    modulo usado para conectar no banco mysql.connector 
"""
# Modulos importados
import mysql.connector
from mysql.connector import errorcode
import sys

###########################
# Variáveis Globais       #
###########################
cleanColor = '\033[0;0m'
statusColorError = '\033[1;31m'
statusColorSuccess = '\033[1;32m'

###########################
# Funções do programa
###########################

# conDataBase -> Função que faz a conexão com o banco (OBS: o dicionário config contém as informações de um Laboratório de Dev pessoal)
def conDataBase():
    global cleanColor, statusColorError
    config = {
                'user': 'pyDev',
                'password': 'pydev2019',
                'host': '10.10.10.7',
                'database': 'pydev'
            }
    try:
        con = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(f"{statusColorError}Algo está errado com seu nome de usuário ou senha{cleanColor}")
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"{statusColorError}O banco de dados não exite{cleanColor}")
    return con

def personRegistration(con):
    global statusColorError, cleanColor, statusColorSuccess
    print(f"\n{statusColorSuccess}    Novo Cadastro {cleanColor}")
    print(f"{statusColorSuccess}\n    Digite as informações para cadastrar usuário: {cleanColor}")
    name = input("    Nome: ")
    email = input("    Email: ")
    phone = input("    Telefone: ")
    cursor = con.cursor()
    sql = "insert into cadastroUser(nome, email, phone) values('"+name+"','"+email+"','"+phone+"')"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"{statusColorSuccess}\n    usuário cadastrado com sucesso.{cleanColor}")
    except mysql.connector.Error as err:
        print(f"{statusColorError}     Algo deu errado: {err} {cleanColor}")
    con.close()
    Main()

def viewAllRegistration(con):
    global statusColorError, cleanColor, statusColorSuccess
    cursor = con.cursor()
    sql = "select * from cadastroUser"
    try:
        cursor.execute(sql)
        dataViews = cursor.fetchall()
        print(108 * "-")
        print(f"{45 * ' '} Listar Todos")
        print(108 * "-")
        for data in dataViews:
            name = data[0]
            email = data[1]
            phone = data[2]    
            idUser = data[3] 
            print(f"{statusColorSuccess}ID:{cleanColor} {idUser}    {statusColorSuccess}Nome:{cleanColor}{name}{(30 - len(name)) * ' '}{statusColorSuccess}Email:{cleanColor}{email}{(30 - len(email)) * ' '}{statusColorSuccess}Telefone:{cleanColor} {phone} ")
    except mysql.connector.Error as err:
        print(f"{statusColorError}     Algo deu errado: {err} {cleanColor}")
    con.close()
    Main() 

def searchRegistration(con):
    global statusColorError, cleanColor, statusColorSuccess
    cursor = con.cursor()
    print(f"\n {statusColorSuccess}    Pesquisar Cadastro  \n ")
    print(statusColorSuccess,end=' ')
    search = input("   Digite o Nome a ser pesquisado: ")
    print(cleanColor)
    sql = "select * from cadastroUser where nome like '%"+search+"%'"
    try:
        cursor.execute(sql)
        dataViews = cursor.fetchall()
        print(108 * "-")
        print(f"{45 * ' '} Pesquisado por {search}")
        print(108 * "-")
        for data in dataViews:
            name = data[0]
            email = data[1]
            phone = data[2]    
            idUser = data[3] 
            print(f"{statusColorSuccess}ID:{cleanColor} {idUser}    {statusColorSuccess}Nome:{cleanColor}{name}{(30 - len(name)) * ' '}{statusColorSuccess}Email:{cleanColor}{email}{(30 - len(email)) * ' '}{statusColorSuccess}Telefone:{cleanColor} {phone} ")
    except mysql.connector.Error as err:
        print(f"{statusColorError} Algo deu errado: {err} {cleanColor}")
    con.close()
    Main()
        
def deleteRegistration(con):
    global statusColorError, cleanColor, statusColorSuccess
    cursor = con.cursor()
    print(f"\n{statusColorSuccess}    Excluir Cadastro \n {cleanColor}")
    code = input("    Informe o ID para excluir usuário: ")
    sql = "delete from cadastroUser where idUser ="+code
    try:
        cursor.execute(sql)
        con.commit()
        print(f"{statusColorSuccess} \n    Usuário deletado com sucesso {cleanColor}")
    except mysql.connector.Error as err:
        print(f"{statusColorError}    Algo deu errado: {err} {cleanColor}")
        Main()
    con.close()
    Main()   

def changeRegistration(con):
    global statusColorError, cleanColor, statusColorSuccess
    cursor = con.cursor()
    update = True
    print(f"\n{statusColorSuccess}    Alterar Cadastro \n{cleanColor}")
    code = input("    Informe o ID do registro que deseja alterar: ")
    
    while update:
        print("""\n
    [1] - Nome
    [2] - Telefone
    [3] - E-Mail""")
        try:            
            choseChange = int(input("    Escolha o que vai ser alterado nesse cadastro: "))
            if choseChange == 1:
                newname = input("    Informe o nome para alterar: ")
                sql = "update cadastroUser set nome='"+newname+"' where idUser = "+code
                try:
                    cursor.execute(sql)
                    con.commit()
                    print(f"{statusColorSuccess} \n     Nome Alterado com sucesso {cleanColor}")
                    update = False
                except mysql.connector.Error as err:
                    print(f"{statusColorError}    Algo deu errado: {err} {cleanColor}")
                    update = False
            elif choseChange == 2:
                newPhone = input("    Informe o telefone para alterar: ")
                sql = "update cadastroUser set phone='"+newPhone+"' where idUser = "+code
                try:
                    cursor.execute(sql)
                    con.commit()
                    print(f"{statusColorSuccess} \n    Telefone Alterado com sucesso {cleanColor}")
                    update = False
                except mysql.connector.Error as err:
                    print(f"{statusColorError}    Algo deu errado: {err} {cleanColor}")
                    update = False
            elif choseChange == 3:
                newEmail = input("    Informe o e-mail para alterar: ")
                sql = "update cadastroUser set email='"+newEmail+"' where idUser = "+code
                try:
                    cursor.execute(sql)
                    con.commit()
                    print(f"{statusColorSuccess} \n    E-Mail Alterado com sucesso {cleanColor}")
                    update = False
                except mysql.connector.Error as err:
                    print(f"{statusColorError}    Algo deu errado: {err} {cleanColor}")
                    update = False
            else:
                print('\033[1;31m'+"    Opção Invalida, escolha entre 1 e 3"+'\033[0;0m')
        except ValueError:
            print('\033[1;31m'+"    Não é numero, escolha entre 1 e 3"+'\033[0;0m')
        
    con.close()
    Main()   
        
        
# Main -> Função do menu principal do programa
def Main():
    print("""\n
    [1] - Cadastrar
    [2] - ALterar
    [3] - Excluir
    [4] - Pesquisar
    [5] - Listar Todos
    [6] - Sair""")
    
    try:
        choseOp = int(input("\n    Escolha uma opção: "))
        if choseOp < 1 or choseOp > 6:
           print('\033[1;31m'+"    Opção Invalida, escolha entre 1 e 6"+'\033[0;0m')
           Main()
    except ValueError:
        print('\033[1;31m'+"    Não é numero, escolha entre 1 e 6"+'\033[0;0m')
        Main()
    con = conDataBase()    
    if choseOp == 1:
        personRegistration(con)
    if choseOp == 2:
        changeRegistration(con)    
    if choseOp == 3:
        deleteRegistration(con)
    if choseOp == 4:
        searchRegistration(con)    
    if choseOp == 5:
        viewAllRegistration(con)
    if choseOp == 5:
        sys.exit()
    
if __name__ == '__main__':
    Main()