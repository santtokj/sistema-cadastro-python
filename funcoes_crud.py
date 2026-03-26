import os
import msvcrt
import json
usuarios = []
ARQUIVO_JSON = "usuarios.json"

def salvar_dados():
     with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
          json.dump(usuarios, f, ensure_ascii=False, indent=4)

def carregar_dados():
     if os.path.exists(ARQUIVO_JSON):
          with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
               global usuarios
               usuarios = json.load(f)   



def nome_cadastrado(novo_cadastro):
            return len(novo_cadastro) >= 3 and novo_cadastro.replace(" ", "").isalpha()
def editar_usuario():
            if not usuarios:
                print("A lista está vazia!")
            else:
                while True:
                    try:
                        att = input("Digite o ID para editar (ou digite [Sair] para retornar ao menu): ").strip().lower()
                        
                        if att == "sair":
                            print("\nVoltando ao menu")
                            break
                            
                        indice = int(att)
                        
                        if 0 <= indice < len(usuarios):
                            print(f"Usuário selecionado: {usuarios[indice]}")
                            novo_usuario = input("Digite o novo cadastro do usuário (ou aperte [enter] para cancelar): ").strip().title()
                            
                            if not novo_usuario:
                                print("Edição cancelada! Retornando...")
                                msvcrt.getch()
                                continue
                            
                            if nome_cadastrado(novo_usuario):
                                usuarios[indice] = novo_usuario
                                salvar_dados()
                                print("Sucesso!")
                                break
                            else:
                                print("Nome inválido!")
                        else:
                            print("ID não existe!")
                    except ValueError:
                        print("Erro: Digite apenas números ou 'sair'!")
def menu_remoção():
            if not usuarios:
                print("A lista está vazia")
            else:
                print("\n[1] Remover por ID | [2] Reset Total | [Enter] Voltar ao menu")
                sub_escolha = input("Selecionar: ").strip()
                match sub_escolha:
                    case "1":
                        remover_usuario()
                    case "2":
                        while True:
                            confirmar = input("Digite [resetar] para prosseguir (Ou aperte [enter] para cancelar): ").strip().lower()
                            if not confirmar:
                                print("Operação de reset cancelada.")
                                msvcrt.getch()
                                break 
                            if confirmar == "resetar":
                                usuarios.clear()
                                salvar_dados()
                                print("Sua lista foi resetada com sucesso!")
                                break
                            else:
                                print("Palavra incorreta! ação cancelada.")
                                msvcrt.getch()
                                continue
                    case _:
                            print("Voltando para o menu principal")
def remover_usuario():
            if not usuarios:
                print("A lista está vazia!")
            else:
                while True:
                    try:    
                        entrada = input("ID para remover (ou [enter] para cancelar): ").strip()
                        
                        if not entrada: 
                            print("\nVoltando ao menu")
                            break
                        
                        indice = int(entrada)    
                        
                        if 0 <= indice < len(usuarios):
                            # TRAVA DE SEGURANÇA
                            confirmar = input(f"Tem certeza que deseja remover {usuarios[indice]}? (S/N): ").strip().upper()
                            
                            if confirmar == "S":
                                removido = usuarios.pop(indice)
                                salvar_dados()
                                print(f"Usuário {removido} removido com sucesso!")
                                msvcrt.getch()
                                break
                            else:
                                print("Remoção cancelada!")
                                msvcrt.getch()
                                continue
                        else:
                            print("Erro: Este ID não existe!")
                            msvcrt.getch()
                            
                    except ValueError:
                        print("Erro: Digite apenas números inteiros!")
                        msvcrt.getch()
def cadastrar_usuario():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n --- MODO DE CADASTRO ---")
            while True:
                novo_cadastro = input("Digite o nome de usuario para cadastrar: ").strip().title()
                if not novo_cadastro:
                    print("Finalizando cadastro!")
                    break
                if nome_cadastrado(novo_cadastro):
                    usuarios.append(novo_cadastro)
                    salvar_dados()
                    print(f"✅ {novo_cadastro} adicionado! (Total: {len(usuarios)})")
                    print("Aperte [enter] para retornar ao menu")
                else:
                    print("❌ Erro: O nome deve ter 3+ letras e apenas letras!")
            print("\nVoltando ao menu principal")
def lista_usuario():
            print("\n-- Lista --")
            if not usuarios:
                print("A lista está vazia!")
            else:
                print(f"\n--- {len(usuarios)} USUÁRIOS ENCONTRADOS ---")
                # Mostra o ID e o nome de cadastro do usuário
                for i, cadastro in enumerate(usuarios):
                    print(f"ID: {i} | nome: {cadastro}")
                print("\n [1] Editar | [2] Remover | [ENTER] Voltar ao menu")
                acao = input("Selecione: ").upper().strip()
                if acao == "1":
                    editar_usuario()
                if acao == "2":
                    menu_remoção()