import os
from pathlib import Path

# 1. IMPORTAÇÕES DE LÓGICA
import modulo_edilson

# IMPORTAR OS MÓDULOS DE VOCÊS AQUI ABAIXO
# import modulo_rafael
# import modulo_rafael


def exibir_cabecalho(titulo: str):
    """Renderiza o cabeçalho padrão estilo terminal Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;36m=" * 50)
    print(f" {titulo.upper()} ".center(50, "#"))
    print("=" * 50 + "\033[0m")


# ==========================================
# PARTE: EDILSON
# ==========================================

def tela_criar_diretorio():
    exibir_cabecalho("Criar Diretório")
    print("\033[33mDigite [V] a qualquer momento para voltar.\033[0m\n")
    
    nome = input("Nome do novo diretório: ").strip()
    if nome.lower() == 'v' or not nome: return

    dir_pai = input("Diretório pai: ").strip()
    if dir_pai.lower() == 'v': return
    if not dir_pai: dir_pai = "."

    try:
        caminho = modulo_edilson.criar_diretorio(nome, dir_pai)
        print(f"\n\033[1;32m[SUCESSO] Diretório criado em: {caminho.resolve()}\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m[ERRO] Não foi possível criar o diretório: {e}\033[0m")
        
    input("\nPressione [Enter] para voltar...")


def tela_criar_arquivo():
    exibir_cabecalho("Criar Arquivo")
    print("\033[33mDigite [V] a qualquer momento para voltar.\033[0m\n")
    
    nome = input("Nome do arquivo (ex: notas.txt): ").strip()
    if nome.lower() == 'v' or not nome: return

    dir_pai = input("Diretório de destino: ").strip()
    if dir_pai.lower() == 'v': return
    if not dir_pai: dir_pai = "."

    conteudo = input("Conteúdo do arquivo: ")
    if conteudo.strip().lower() == 'v': return

    try:
        caminho = modulo_edilson.criar_arquivo(nome, conteudo, dir_pai)
        print(f"\n\033[1;32m[SUCESSO] Arquivo criado com sucesso em: {caminho.resolve()}\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m[ERRO] Falha ao criar arquivo: {e}\033[0m")

    input("\nPressione [Enter] para voltar...")


def tela_listar_arquivos():
    exibir_cabecalho("Listar Arquivos")
    print("\033[33mDigite [V] para voltar.\033[0m\n")
    
    alvo = input("Diretório para listar: ").strip()
    if alvo.lower() == 'v': return
    if not alvo: alvo = "."

    try:
        arquivos = modulo_edilson.listar_arquivos(alvo)
        print(f"\n\033[1;34m=== Arquivos em '{Path(alvo).resolve()}' ===\033[0m")
        if not arquivos:
            print("  (Nenhum arquivo encontrado neste diretório)")
        else:
            for arq in arquivos:
                print(f"  📄 {arq.name}")
        print("\033[1;34m" + "-"*50 + "\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m[ERRO] {e}\033[0m")

    input("\nPressione [Enter] para voltar...")


# ==========================================
# PARTE: RAFAEL OC
# ==========================================

def tela_excluir_arquivo():
    exibir_cabecalho("Excluir Arquivo - Rafael OC")
    print("\033[33mDigite [V] para voltar.\033[0m\n")
    
    nome_arquivo = input("Nome do arquivo a ser excluído: ").strip()
    if nome_arquivo.lower() == 'v' or not nome_arquivo: return
    
    diretorio = input("Diretório onde o arquivo está: ").strip()
    if diretorio.lower() == 'v': return
    if not diretorio: diretorio = "."

    try:
        # descomentar e ajustar a linha abaixo com sua função 
        # resultado = modulo_rafael.excluir_arquivo(nome_arquivo, diretorio)
        # print(f"\n\033[1;32m[SUCESSO] {resultado}\033[0m")
        print("\n\033[1;33m[AVISO] Tela pronta! Conecte sua função aqui, Rafael OC.\033[0m") # excluir linha depois de descomentado
    except Exception as e:
        print(f"\n\033[1;31m[ERRO] {e}\033[0m")
        
    input("\nPressione [Enter] para voltar...")


def tela_ler_arquivo():
    exibir_cabecalho("Ler Arquivo")
    print("\033[33mDigite [V] para voltar.\033[0m\n")
    
    nome_arquivo = input("Nome do arquivo para leitura: ").strip()
    if nome_arquivo.lower() == 'v' or not nome_arquivo: return
    
    diretorio = input("Diretório do arquivo: ").strip()
    if diretorio.lower() == 'v': return
    if not diretorio: diretorio = "."

    try:
        # descomentar e ajustar a linha abaixo com sua função 
        # conteudo = modulo_rafael.ler_arquivo(nome_arquivo, diretorio)
        # print(f"\n\033[1;34m=== Conteúdo do Arquivo ===\033[0m\n{conteudo}\n\033[1;34m===========================\033[0m")
        print("\n\033[1;33m[AVISO] Tela pronta! Conecte sua função aqui, Rafael OC.\033[0m") # excluir depois que descomentar
    except Exception as e:
        print(f"\n\033[1;31m[ERRO] {e}\033[0m")
        
    input("\nPressione [Enter] para voltar...")


def tela_renomear():
    exibir_cabecalho("Renomear Arquivo/Diretório - Rafael OC")
    print("\033[33mDigite [V] para voltar.\033[0m\n")
    
    # Parâmetros livres para a função opcional de renomear
    caminho_atual = input("Nome ou caminho atual do item: ").strip()
    if caminho_atual.lower() == 'v' or not caminho_atual: return
    
    novo_nome = input("Novo nome ou novo caminho: ").strip()
    if novo_nome.lower() == 'v' or not novo_nome: return

    try:
        # Caso vc faça a função opcional, adiciona aqui, caso não, exclua
        print("\n\033[1;33m[AVISO] Tela pronta! Caso tenha feito a função de renomear, coloque-a aqui.\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m[ERRO] {e}\033[0m")
        
    input("\nPressione [Enter] para voltar...")


# ==========================================
# PARTE: RAFAEL NAVES
# ==========================================

def tela_excluir_diretorio():
    exibir_cabecalho("Excluir Diretório")
    print("\033[33mDigite [V] para voltar.\033[0m\n")
    
    diretorio = input("Nome da pasta/diretório para excluir: ").strip()
    if diretorio.lower() == 'v' or not diretorio: return
    
    local = input("Diretório pai onde ela está: ").strip()
    if local.lower() == 'v': return
    if not local: local = "."

    try:
        # descomentar e ajustar a linha abaixo com sua função 
        # resultado = modulo_rafael.excluir_diretorio(diretorio, local)
        # print(f"\n\033[1;32m[SUCESSO] {resultado}\033[0m")
        print("\n\033[1;33m[AVISO] Tela pronta! Conecte sua função aqui, Rafael Naves.\033[0m") # exclua depois
    except Exception as e:
        print(f"\n\033[1;31m[ERRO] {e}\033[0m")
        
    input("\nPressione [Enter] para voltar...")


def tela_copiar_arquivo():
    exibir_cabecalho("Copiar Arquivo")
    print("\033[33mDigite [V] para voltar.\033[0m\n")
    
    nome_arquivo = input("Nome do arquivo de origem (ex: dado.txt): ").strip()
    if nome_arquivo.lower() == 'v' or not nome_arquivo: return
    
    arquivo = input("Diretório atual dele: ").strip()
    if arquivo.lower() == 'v': return
    if not arquivo: arquivo = "."
    
    diretorio = input("Diretório de destino (onde a cópia vai salvar): ").strip()
    if diretorio.lower() == 'v' or not diretorio: return

    try:
        # descomentar e ajustar a linha abaixo com sua função 
        # resultado = modulo_rafael.copiar_arquivo(nome_arquivo, arquivo, diretorio)
        # print(f"\n\033[1;32m[SUCESSO] {resultado}\033[0m")
        print("\n\033[1;33m[AVISO] Tela pronta! Conecte sua função aqui, Rafael Naves.\033[0m") # exclua depois
    except Exception as e:
        print(f"\n\033[1;31m[ERRO] {e}\033[0m")
        
    input("\nPressione [Enter] para voltar...")


def tela_copiar_diretorio():
    exibir_cabecalho("Copiar Diretório")
    print("\033[33mDigite [V] para voltar.\033[0m\n")
    
    origem = input("Diretório/Pasta que deseja copiar: ").strip()
    if origem.lower() == 'v' or not origem: return
    
    destino = input("Diretório/Pasta de destino: ").strip()
    if destino.lower() == 'v' or not destino: return

    try:
        # Caso vc faça a função opcional, adiciona aqui, caso não, exclua
        print("\n\033[1;33m[AVISO] Tela pronta! Caso tenha feito a função de copiar pastas, coloque-a aqui.\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m[ERRO] {e}\033[0m")
        
    input("\nPressione [Enter] para voltar...")