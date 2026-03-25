import os
import msvcrt
usuarios = []
def editar_usuario():
            if not usuarios:
                print("A lista está vazia!")
            else:
                while True:
                    try:
                        att = input("Digite o ID para editar (ou tente [enter] para retornar ao menu): ").strip()
                        if not att:
                            print("\nVoltando ao menu")
                            break
                        indice = int(att)
                        if 0 <= indice < len(usuarios):
                            print(f"Usuário selecionado: {usuarios[indice]}")
                            novo_usuario = input("Digite o novo cadastro do usuário: ").strip().title()
                            if len(novo_usuario) >= 3 and novo_usuario.replace(" ","").isalpha():
                                usuarios[indice] = novo_usuario
                                print("Sucesso!")
                                break
                            else:
                                print("Nome inválido!")
                        else:
                            print("ID não existe!")
                    except ValueError:
                        print("Erro: Digite apenas números!")
def menu_remoção():
    if not usuarios:
        print("A lista está vazia")
    else:
        print("\n[1] Remover por ID | [2] Reset Total | [Enter] Voltar")
        sub_escolha = input("Selecionar: ").strip()
        match sub_escolha:
            case "1":
                remover_usuario()
            case "2":
                confirmar = input("Digite confirmar para prosseguir: ").upper().strip()
                if confirmar == "confirmar":
                    usuarios.clear()
                    print("Sua lista foi resetada com sucesso!")
            case _:
                print("Voltando para o menu principal")
def remover_usuario():
            if not usuarios:
                print("A lista está vazia!")
            else:
                while True:
                    try:    
                        entrada = input("Digite o número (ID) para remover(ou aperte [enter] para retornar ao menu): ")
                        if not entrada: 
                            print("\nVoltando ao menu")
                            break
                        indice = int(entrada)    
                        if indice >= 0:
                            removido = usuarios.pop(indice)
                            print(f"usuario {removido} removido!")
                        else:
                            print("Erro: O ID não pode ser negativo")
                    except ValueError:
                        print("Erro: Digite apenas números inteiros!")
                    except IndexError:
                        print("Erro: Este ID não existe!")
                    print("Aperte [enter] para voltar ao menu")     
while True:
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o terminal
    print("=" * 11, "MENU", "=" * 11)
    print("\n [1] Cadastrar \n [2] gerenciamento de lista \n [3] Sair")
    print("\n","=" * 26)
    # Impede a adição de caracteres além dos números apresentados
    try:
        opcao = input("\nEscolha uma opção: ")
    except Exception as e:
        print("Ocorreu um erro inesperado!")

    # Bloco cadastro
    match opcao:
        case "1":
            print("\n --- MODO DE CADASTRO (aperte [enter] para parar) ---")
            while True:
                novo_cadastro = input("Digite o nome de usuario para cadastrar: ").strip().title()
                if not novo_cadastro:
                    print("Finalizando cadastro!")
                    break
                if len(novo_cadastro) >= 3 and novo_cadastro.replace(" ", "").isalpha():
                    usuarios.append(novo_cadastro)
                    print(f"✅ {novo_cadastro} adicionado! (Total: {len(usuarios)})")
                else:
                    print("❌ Erro: O nome deve ter 3+ letras e apenas letras!")
            print("\nVoltando ao menu principal")
            msvcrt.getch()
        # Bloco lista
        case "2":
            print("\n-- Lista --")
            if not usuarios:
                print("A lista está vazia!")
            else:
                print(f"\n--- {len(usuarios)} USUÁRIOS ENCONTRADOS ---")
                # Mostra o ID e o nome de cadastro do usuário
                for i, cadastro in enumerate(usuarios):
                    print(f"ID: {i} | nome: {cadastro}")
                print("\n [1] Editar | [2] Remover | [ENTER] Voltar ao menu")
                acao = input("Deseja fazer algo com algum ID? ").upper().strip()
                if acao == "1":
                    editar_usuario()
                if acao == "2":
                    menu_remoção()
            msvcrt.getch()
        # Bloco remoção
        case "1":
            remover_usuario()
            msvcrt.getch()
        # Edição de nomes
        case "2":
            editar_usuario()
            msvcrt.getch()
        # Bloco sair
        case "3":
            sair_de_vez = False
            while True:
                confirmar = input("Deseja realmente sair? (S/N): ").upper().strip()

                if confirmar == "S":
                    print("Encerrando o sistema... até logo!")
                    msvcrt.getch()
                    sair_de_vez = True
                    break
                elif confirmar == "N":
                    print("\nRetornando ao menu...")
                    print("Aperte [enter] para continuar")
                    msvcrt.getch()
                    break
                else:
                    print("Erro: Digite apenas 'S' ou 'N'!")
            if sair_de_vez:
                break          
        case _:
            print("Opção inválida!")
            print("Aperte [enter] para voltar ao menu")
            msvcrt.getch()

#Remover função de voltar ao menub quando apertado enter
#Adicionar função de cancelar ação de remover/alterar
#Concertar função de reset total de lista
#Salvar dados em .txt
#Ler dados em .txt
#Arrumar visual
#Revisar codigo em busca de erros