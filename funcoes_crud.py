import os
import msvcrt
import json

class GerenciadorUsuarios:
    def __init__(self, arquivo_json="usuarios.json"):
        self.arquivo_json = arquivo_json
        self.usuarios = {}
        self.carregar_dados()

    def salvar_dados(self):
        with open(self.arquivo_json, "w", encoding="utf-8") as f:
            json.dump(self.usuarios, f, ensure_ascii=False, indent=4)

    def carregar_dados(self):
        if os.path.exists(self.arquivo_json):
            try:
                with open(self.arquivo_json, "r", encoding="utf-8") as f:
                    dados_brutos = json.load(f)   
                    self.usuarios = {int(k): v for k, v in dados_brutos.items()}
            except (json.JSONDecodeError, ValueError):
                self.usuarios = {}
        else:
            self.usuarios = {}

    def nome_cadastrado(self, nome_cadastro):
        return len(nome_cadastro) >= 3 and nome_cadastro.replace(" ", "").isalpha()

    def cadastrar_usuario(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n --- MODO DE CADASTRO ---")
        while True:
            novo_cadastro = input("Digite o nome de usuário (ou [Enter] para sair): ").strip().title()
            if not novo_cadastro:
                print("Finalizando cadastro!")
                break
            
            if self.nome_cadastrado(novo_cadastro):
                novo_id = max(self.usuarios.keys()) + 1 if self.usuarios else 0
                self.usuarios[novo_id] = novo_cadastro
                self.salvar_dados()
                print(f"✅ {novo_cadastro} adicionado com ID: {novo_id}!")
            else:
                print("❌ Erro: O nome deve ter 3+ letras e apenas letras!")

    def lista_usuario(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n-- Lista de Usuários --")
            if not self.usuarios:
                print("A lista está vazia!")
                msvcrt.getch()
                break
            else:
                print(f"\n--- {len(self.usuarios)} USUÁRIOS ENCONTRADOS ---")
                for id_real, nome in self.usuarios.items():
                    print(f"ID: {id_real} | Nome: {nome}")
                
                print("\n [1] Editar | [2] Remover | [ENTER] Voltar ao menu")
                acao = input("Selecione: ").strip()
                if acao == "1":
                    self.editar_usuario()
                elif acao == "2":
                    self.menu_remoção()

    def editar_usuario(self):
        while True:
            try:
                att = input("\nID para editar (ou digite [Sair] para cancelar): ").strip().lower()
                if att == "sair": break
                
                indice = int(att)
                if indice in self.usuarios:
                    print(f"Usuário selecionado: {self.usuarios[indice]}")
                    novo_nome = input("Digite o novo nome (ou [Enter] para cancelar): ").strip().title()
                    
                    if not novo_nome:
                        print("Edição cancelada!")
                        break
                    
                    if self.nome_cadastrado(novo_nome):
                        self.usuarios[indice] = novo_nome
                        self.salvar_dados()
                        print("✅ Sucesso!")
                        break
                    else:
                        print("❌ Nome inválido!")
                else:
                    print("❌ ID não existe!")
            except ValueError:
                print("Erro: Digite apenas números!")

    def menu_remoção(self):
        print("\n[1] Remover por ID | [2] Reset Total | [Enter] Voltar")
        sub_escolha = input("Selecionar: ").strip()
        
        if sub_escolha == "1":
            self.remover_usuario()
        elif sub_escolha == "2":
            confirmar = input("Digite [resetar] para apagar TUDO: ").strip().lower()
            if confirmar == "resetar":
                self.usuarios.clear()
                self.salvar_dados()
                print("💥 Lista resetada!")
            else:
                print("Ação cancelada.")

    def remover_usuario(self):
        try:    
            entrada = input("ID para remover (ou [Enter] para cancelar): ").strip()
            if not entrada: return
            
            indice = int(entrada)
            if indice in self.usuarios:
                confirmar = input(f"Remover {self.usuarios[indice]}? (S/N): ").strip().upper()
                if confirmar == "S":
                    removido = self.usuarios.pop(indice)
                    self.salvar_dados()
                    print(f"✅ {removido} removido!")
            else:
                print("❌ ID não encontrado.")
        except ValueError:
            print("❌ Digite um número válido.")