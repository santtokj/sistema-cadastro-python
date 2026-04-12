import os
import msvcrt
import mysql.connector
from database import conectar, criar_cursor

class GerenciadorUsuarios:
    def __init__(self):
        pass

    def nome_cadastrado(self, nome_cadastro):
        return len(nome_cadastro) >= 3 and nome_cadastro.replace(" ", "").isalpha()
    
    def email_cadastrado(self, email_valida):
        return "@" in email_valida and "." in email_valida

    def cadastrar_usuario(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n --- MODO DE CADASTRO (MySQL) ---")
        while True:
            novo_cadastro = input("Digite o nome (ou [Enter] para sair): ").strip().title()
            if not novo_cadastro: break
            
            if self.nome_cadastrado(novo_cadastro):
                novo_email = input(f"E-mail para {novo_cadastro}: ").strip().lower()
                if not self.email_cadastrado(novo_email):
                    print("❌ Erro: E-mail inválido!")
                    continue
                
                try:
                    conn = conectar()
                    cursor = criar_cursor(conn)
                    sql = "INSERT INTO usuarios (nome_usuarios, email_usuarios) VALUES (%s, %s)"
                    cursor.execute(sql, (novo_cadastro, novo_email))
                    conn.commit()
                    print(f"✅ {novo_cadastro} salvo com sucesso!")
                except mysql.connector.Error as err:
                    print(f"❌ Erro no Banco: {err}")
                finally:
                    cursor.close()
                    conn.close()
            else:
                print("❌ Erro: Nome inválido!")

    def lista_usuario(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n-- Lista de Usuários (Puxada do MySQL) --")
            
            try:
                conn = conectar()
                cursor = criar_cursor(conn)
                cursor.execute("SELECT * FROM usuarios")
                usuarios = cursor.fetchall() 
                
                if not usuarios:
                    print("A lista está vazia!")
                    msvcrt.getch()
                    break
                else:
                    print(f"\n--- {len(usuarios)} USUÁRIOS ENCONTRADOS ---")
                    for user in usuarios:
                        print(f"ID: {user[0]} | Nome: {user[1]} | E-mail: {user[2]} | Data: {user[3]}")
                    
                    print("\n [1] Editar | [2] Remover | [ENTER] Voltar ao menu")
                    acao = input("Selecione: ").strip()
                    if acao == "1":
                        self.editar_usuario()
                    elif acao == "2":
                        self.menu_remoção()
                    else:
                        break
            except mysql.connector.Error as err:
                print(f"Erro: {err}")
                break
            finally:
                cursor.close()
                conn.close()

    def editar_usuario(self):
        att = input("\nID para editar (ou [Sair]): ").strip()
        if att.lower() == "sair": return
        
        novo_nome = input("Novo nome (ou Enter para manter): ").strip().title()
        novo_email = input("Novo e-mail (ou Enter para manter): ").strip().lower()

        try:
            conn = conectar()
            cursor = criar_cursor(conn)
            
            cursor.execute("SELECT nome_usuarios, email_usuarios FROM usuarios WHERE idusuarios = %s", (att,))
            atual = cursor.fetchone()
            
            if atual:
                nome_f = novo_nome if novo_nome else atual[0]
                email_f = novo_email if novo_email else atual[1]
                
                sql = "UPDATE usuarios SET nome_usuarios = %s, email_usuarios = %s WHERE idusuarios = %s"
                cursor.execute(sql, (nome_f, email_f, att))
                conn.commit()
                print("✅ Atualizado!")
            else:
                print("❌ ID não encontrado!")
        finally:
            cursor.close()
            conn.close()
            msvcrt.getch()

    def menu_remoção(self):
        print("\n[1] Remover por ID | [2] Reset Total")
        escolha = input("Selecionar: ").strip()
        
        if escolha == "1":
            id_del = input("ID para remover: ").strip()
            try:
                conn = conectar()
                cursor = criar_cursor(conn)
                cursor.execute("DELETE FROM usuarios WHERE idusuarios = %s", (id_del,))
                conn.commit()
                print("✅ Removido!")
            finally:
                cursor.close()
                conn.close()
                msvcrt.getch()
        #Função bugada, evitar uso momentaneamente!!!
        elif escolha == "2":
            confirmar = input("⚠️ ATENÇÃO: Deseja apagar TODOS os usuários? (S/N): ").upper().strip()
            if confirmar == "S":
                try:
                    conn = conectar()
                    cursor = criar_cursor(conn)
                    cursor.execute("TRUNCATE TABLE usuarios")
                    conn.commit()
                    cursor.close()
                    conn.close()
                    print("💥 Banco de dados resetado!")
                except mysql.connector.Error as err:
                    print(f"❌ Erro ao resetar: {err}")
                
                input("Pressione [Enter] para continuar...")
            else:
                print("Operação cancelada.")
                msvcrt.getch()
                
    def sair_sistema(self):
        while True:
            confirmar = input("Deseja realmente sair? (S/N): ").upper().strip()
            if confirmar == "S":
                print("Encerrando o sistema... até logo!")
                msvcrt.getch()
                return True
            elif confirmar == "N":
                print("\nRetornando ao menu...")
                print("Aperte [Enter] para continuar")
                msvcrt.getch()
                return False 
            else:
                print("Erro: Digite apenas 'S' ou 'N'!")