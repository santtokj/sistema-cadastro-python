import msvcrt
import os
from funcoes_crud import GerenciadorUsuarios

sistema = GerenciadorUsuarios()
while True:
    os.system("cls" if os.name == "nt" else "clear") 
    print("=" * 11, "MENU", "=" * 11)
    print("\n [1] Cadastrar \n [2] gerenciamento de lista \n [3] Sair")
    print("\n", "=" * 26)
    try:
        opcao = input("\nEscolha uma opção: ").strip()
    except Exception as e:
        print("Ocorreu um erro inesperado!")

    match opcao:
        case "1":
            sistema.cadastrar_usuario()
        case "2":
            sistema.lista_usuario()
            msvcrt.getch()
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

# TODO
# Arrumar visual
