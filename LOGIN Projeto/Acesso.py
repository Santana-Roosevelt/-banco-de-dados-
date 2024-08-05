import getpass

usuarios = {}

def adicionar_usuario():
    print("Adicionar Novo Usuário")
    nome_usuario = input("Nome de Usuário: ")
    
    if nome_usuario in usuarios:
        print("Usuário já existe.")
        return
    
    senha = getpass.getpass("Senha: ")
    usuarios[nome_usuario] = senha
    print("Usuário adicionado com sucesso!")

def autenticar_usuario():
    print("Autenticar Usuário")
    nome_usuario = input("Nome de Usuário: ")
    
    if nome_usuario not in usuarios:
        print("Usuário não encontrado.")
        return
    
    senha = getpass.getpass("Senha: ")
    
    if usuarios[nome_usuario] == senha:
        print("Acesso concedido.")
    else:
        print("Senha incorreta.")

def menu():
    while True:
        print("Sistema de Controle de Acesso")
        print("1. Adicionar Novo Usuário")
        print("2. Autenticar Usuário")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_usuario()
        elif opcao == '2':
            autenticar_usuario()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
