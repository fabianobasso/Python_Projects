print ("--------------------------------- Sistema para cadastro de pessoas ---------------------------------")
import MySQLdb
import sys

def connectDataBase():
    db = "pytest"
    user = "py"
    password = "blood"
    host = "localhost"

    try:
        con = MySQLdb.connect(db=db, user=user, passwd=password, host=host)
        print ("Banco de dados Online")
    except MySQLdb as erro:
        print ("Não conseguiu conectar com o banco de dados",erro)
        menu()
    return con

def Cadastro(con):
    print("Digite os dados da pessoa.: \n")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cursor = con.cursor()
    sql = "insert into usuario (name,email,senha) values ('"+nome+"','"+email+"','"+senha+"')"
    # print (sql)
    try:
        cursor.execute(sql)
        con.commit()
        print("Usuario cadastrado com sucesso!!!")
    except MySQLdb as erro:
        print("Não foi possivel cadastrar o usuario: ",erro)

    con.close()    
    menu()

def ListarTodos(con):
    cursor = con.cursor()
    sql = "select * from usuario"
    try:
        cursor.execute(sql)
        dadosUsuario = cursor.fetchall()
        print (70 * "-")
        print ("\t\t\t Listar Todos")
        print (70 * "-")
        for dados in dadosUsuario:
            codigo = dados[0]
            nome = dados[1]
            email = dados[2]
            senha = dados[3]
            data = dados[4]
            print (f"Id: {codigo} Nome: {nome} E-mail: {email} Senha: {senha} Criado em: {data}")
        print (f"\n Listou {(len(dadosUsuario))} usuários")    
    except MySQLdb as erro:
        print ("Não conseguiu listar.: ",erro)
    
    con.close()
    menu()

def Pesquisar(con):
    nome = input("Digite o nome de usuario a pesquisa: ")
    cursor = con.cursor()
    sql = "select * from usuario where name like '%"+nome+"%'"
    try:
        cursor.execute(sql)
        dadosUsuario = cursor.fetchall()
        print (70 * "-")
        print ("\t\t\t Lista de Usuario")
        print (70 * "-")
        for dados in dadosUsuario:
            codigo = dados[0]
            nome = dados[1]
            email = dados[2]
            senha = dados[3]
            data = dados[4]
            print (f"Id: {codigo} Nome: {nome} E-mail: {email} Senha: {senha} Criado em: {data}")
    except MySQLdb as erro:
        print (f"Não foi possivel localizar: {nome} ",erro) 
    con.close()
    menu() 

def Alterar(con):
    codigo = input("Digite o codigo da pessoa que deseja alterar o nome: ")
    nome = input("Digite o novo nome: ")
    cursor = con.cursor()
    sql = "update usuario set name='"+nome+"' where iduser = "+codigo          
    try:
        cursor.execute(sql)
        con.commit()
        print(f"Usuario {codigo} alterado com sucesso")
    except MySQLdb as erro:
        print ("não foi possivel alterar usuario",erro)
    con.close()
    menu()

def Excluir(con):
    codigo = input("Digite o Codigo do usuario para excluir:" )
    cursor = con.cursor()
    sql = "delete from usuario where iduser = "+codigo
    try:
        cursor.execute(sql)
        con.commit()
        print (f"Você exclui o usuario de codigo: {codigo} com sucesso")
    except MySQLdb as erro:
        print (f"Não foi possivel excluir o usuario de {codigo}")        
    con.close()
    menu()


def menu():
    opcaoEscolhida = int(input("Escolha uma opção:\n\n1- Cadastrar\n2- Alterar\n3- Excluir\n4- Pesquisar\n5- Listar todos\n6- Sair\n\nOpção.: "))
    try:        
        if opcaoEscolhida < 1 or opcaoEscolhida > 6:
            print("Opção Inválida, escolha entre 1 e 6")
            menu()
    except:
        print("Opção Inválida, escolha entre 1 e 6")
        menu()
    con = connectDataBase()     
    if opcaoEscolhida == 1:
        Cadastro(con) 
    elif opcaoEscolhida == 2:
        Alterar(con)
    elif opcaoEscolhida == 3:
        Excluir(con)
    elif opcaoEscolhida == 4:
        Pesquisar(con)     
    elif opcaoEscolhida == 5:
        ListarTodos(con)
    elif opcaoEscolhida == 6:
        sys.exit()          
    

menu()
