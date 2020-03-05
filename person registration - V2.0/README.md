# Projeto cadastro de pessoas

Esse projeto foi desenvolvido para mostra meus conhecimentos usando banco de dados em python.  


Foi usado nesse projeto banco de dados __mariaDB(v10.3)__, o modulo __mysql.connector__ para fazer a conexão com o banco de dados.  


__Criado uma unica tabela:__  
```sql
create table cadastroUser
(
    nome varchar(100)not null,
    email varchar(100)not null,
    phone varchar(100)not null,
    idUser int primary key not null AUTO_INCREMENT 
);
```

### Menu principal

<img src="img/menu.png" height="200" width="200"/>


__Cadatrar ->__ Cadastrar uma nova pessoa na base de dados.  
__Alterar ->__ Fazer modificação em usuário já cadastrado.  
__Excluir ->__ Apagar da base de dados um usuário cadastrado.  
__Pesquisar ->__ Faz um pesquisa por um nome especifico e mostra na tela.  
__Listar Todos ->__ Lista todos os usuário cadastrado.  
__Sair ->__ Sai do programa.  


__Cadastro :__  
<img src="img/Cadastro.png" height="300" width="300"/>  



__Alterar :__  
<img src="img/Alterar.png" height="300" width="300"/>  


__Pesquisar :__  
<img src="img/pesquisadopor.png" height="300" width="700"/>  

__Listar Todos :__  
<img src="img/ListarTodos.png" height="300" width="700"/>  


