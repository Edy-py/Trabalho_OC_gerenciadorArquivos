import modulo_telas


def menu_principal():
    while True:
        modulo_telas.exibir_cabecalho("Sistema de Arquivos - Grupo v1.0")

        # --- PARTE EDILSON ---

        print("\n\033[1;36m[ Operações em Arquivos ]\033[0m")

        print("  \033[1;32m[1]\033[0m Ler Arquivo")
        print("  \033[1;32m[2]\033[0m Listar Arquivos")
        print("  \033[1;32m[3]\033[0m Renomear Arquivo/Diretório") # necessário ajustes
        print("  \033[1;32m[4]\033[0m Copiar Arquivo")
        print("  \033[1;32m[5]\033[0m Copiar Diretório")

        print("\n" + "\033[1;36m[ Criar ]\033[0m")
        print("  \033[1;32m[6]\033[0m Criar Novo Diretório")
        print("  \033[1;32m[7]\033[0m Criar Novo Arquivo")
        
        print("\n\033[1;36m[ Operações de Exclusão ]\033[0m")
        print("  \033[1;32m[8]\033[0m Excluir Diretório")
        print("  \033[1;32m[9]\033[0m Excluir Arquivo")

        print("\n" + "\033[1;36m=" * 50 + "\033[0m")
        print("  \033[1;31m[0]\033[0m Sair do Programa")
        print("\033[1;36m=" * 50 + "\033[0m")

        opcao = input("\033[1;33muser@terminal:~$\033[0m ").strip()

        # Roteamento das opções para as telas correspondentes
        if opcao == "1":
            modulo_telas.tela_ler_arquivo()
        elif opcao == "2":
            modulo_telas.tela_listar_arquivos()
        elif opcao == "3":
            modulo_telas.tela_renomear()
        elif opcao == "4":
            modulo_telas.tela_copiar_arquivo()
        elif opcao == "5":
            modulo_telas.tela_copiar_diretorio()
        elif opcao == "6":
            modulo_telas.tela_criar_diretorio()
        elif opcao == "7":
            modulo_telas.tela_excluir_diretorio()
        elif opcao == "8":
            modulo_telas.tela_criar_arquivo()
        elif opcao == "9":
            modulo_telas.tela_excluir_arquivo()
        elif opcao == "0":
            print("\n\033[1;31m[!] Sessão encerrada.\033[0m")
            break
        else:
            input(
                "\n\033[1;31mOpção inválida! Pressione [Enter] para tentar novamente.\033[0m"
            )


if __name__ == "__main__":
    menu_principal()
