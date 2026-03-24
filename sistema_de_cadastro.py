import os
import msvcrt
usuarios = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o terminal
    print("=" * 11, "MENU", "=" * 11)
    print("\n 1. Cadastrar \n 2. Listar \n 3. remoção \n 4. Sair")
    print("\n","=" * 26)
    # Impede a adição de caracteres além dos números apresentados
    try:
        opcao = input("\nEscolha uma opção: ")
    except Exception as e:
        print("Ocorreu um erro inesperado!")

    # Bloco cadastro
    match opcao:
        case "1":
            novo_cadastro = input ("Digite o nome para cadastrar: ").strip().title()
            if novo_cadastro:
                # Impede que o nome tenha menos que três letras e impede a adição de números ao cadastro
                if len(novo_cadastro) >= 3 and novo_cadastro.replace(" ", "").isalpha():
                    # Adiciona usuários na lista
                    usuarios.append(novo_cadastro)
                    print(f"{novo_cadastro} foi adicionado com sucesso, agora temos {len(usuarios)} usuarios cadastrados!")
                else:
                    print("Erro: o nome deve conter ao menos três caracteres e possuir apenas letras!")
            else:
                print("Erro: o nome não pode estar vazio!")
            print("Aperte [enter] para voltar ao menu")
            # Permite retornar ao menu quando apertado qualquer tecla (definido visualmente por enter na print)
            msvcrt.getch()
        # Bloco lista
        case "2":
            print("\nLista")
            if not usuarios:
                print("A lista está vazia!")
            else:
                print(f"\n--- {len(usuarios)} USUÁRIOS ENCONTRADOS ---")
                # Mostra o ID e o nome de cadastro do usuário
                for i, cadastro in enumerate(usuarios):
                    print(f"ID: {i} | nome: {cadastro}")
            print("Aperte [enter] para voltar ao menu")
            msvcrt.getch()
        # Bloco remoção
        case "3":
            if not usuarios:
                print("A lista está vazia!")
            else:
                try:    
                    indice = int(input("Digite o número (ID) para remover: "))
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
            msvcrt.getch()
        # Bloco sair
        case "4":
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