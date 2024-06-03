#Grupo: Otávio Rodrigues Amorim de Almeida(202322984),Lealdo Coelho Válido de Jesus(202323215)
import json

def login():
    while True:
        tentativa_usuario = input("Insira o nome de usuário: ")
        tentativa_senha = input("Insira o nome de a senha: ")
        if tentativa_usuario in dict.keys(usuarios):
            if tentativa_senha == usuarios[tentativa_usuario]:
                print("login com sucesso")
                break
            else:
                print("senha errada")
        else:
            print("usuário não existe")
    return [tentativa_usuario,tipo_usuario[tentativa_usuario]]
        
def colaboradores():#gerenciar colaboradoes(adicionar(digite o nome, e digite senha),remover,listar)
    while True:
        print("1.adicionar colaboradores\n2.remover colaboradores\n3.listar colaboradores\n4.sair")
        menu = input("insira oque deseja fazer: ")

        if menu == "1":#adicionar colaboradores
            nome_novo = input("insira o nome do usuario: ")
            senha_novo = input("insira a senha do usuario: ")
            tipo_novo = input("insira o tipo do usuario: ")
            print("insira o tipo de usuario: \n1.administrador\n2.cliente")
            if tipo_novo == "1":
                tipo_novo = "administrador"
            if tipo_novo == "2":
                tipo_novo = "cliente"
            if nome_novo in dict.keys(usuarios):
                print("usuario já existe")
            else:
                usuarios[nome_novo] = senha_novo
                tipo_usuario[nome_novo] = tipo_novo
                print("usuario cadastrado\n")
                break
            

        if menu == "2":#remover colaboradores
            remover = input("insira o nome do usuario que deseja remover: ")
            if remover in dict.keys(usuarios):
                usuarios.pop(remover)
                print("usuario removido")
                break
            else:
                print("usuário não existe")
                break

        if menu == "3":#listar colaboradores
            lista = []
            for i in usuarios.keys():
                lista.append(i)
            print(lista)
            break
        if menu == "4":
            break

        exit()

def pesquisa():
    print("Barra de pesquisa")
    user_resposta = input("")
    if user_resposta in livros.keys():
        print("Livro encontrado")
    else:
        print("Desculpe, Mas não encontramos nada relacionado a isso")
 

def cadastrar_livros():
    print("1.adicionar livro\n2.listar livros")
    menu = input("insira oque deseja fazer:")
    if menu == "1":
        nome_novo = input("insira o nome do livro novo: ")
        autor_novo = input("insira o nome do autor do livro novo: ")
        ano_novo = int(input("insira a data de lançamento do livro: "))
        livros[nome_novo] = [autor_novo,ano_novo]
    if menu == "2":
        for livro in livros:
            print(livro,livros[livro])


def main():
    global usuarios,livros,tipo_usuario
    usuarios = {"admin":"admin","Lealdo":"senha123"}
    #tipo_usuario = {"admin":"admnistrador","Lealdo":"cliente"}

    
    with open("./tipo_usuario.json","r") as f:
        temp = f.read()

    tipo_usuario = json.loads(temp) 
    print(tipo_usuario,"print tipo_usuario")











    livros = {"O instituto":["Stephen King",2019],"Maus":["Art Spiegelman",1986]}

    usuario = login()

    while True:
        print("1.gerenciar colaboradores\n2.gerenciar livros.\n3.Pesquisar Livros\n4.sair")
        menu = input("insira oque deseja fazer: ")
        if menu == "1":
            if usuario[1] != "admnistrador":
                print("não tem permissão para realizar esta ação")
            else:
                colaboradores()
        if menu == "2":
            if usuario[1] != "admnistrador":
                print("não tem permissão para realizar esta ação")
            else:
                cadastrar_livros()
        if menu == "3":
                pesquisa()
        if menu == "4":
            exit()



if __name__ == "__main__":
    """with open("./tipo_usuario.json","w") as f:
        json.dump(usuarios, f)"""#escrever para o json,não necessario
    main()


    
