import os


def excluir_arquivo(nome_arquivo: str, diretorio: str = ".") -> None:
    """Exclui um arquivo do diretório especificado."""

    caminho_completo = os.path.join(diretorio, nome_arquivo)

    if not os.path.exists(caminho_completo):
        raise FileNotFoundError(
            f"O arquivo '{nome_arquivo}' não existe."
        )

    if not os.path.isfile(caminho_completo):
        raise ValueError(
            f"'{nome_arquivo}' não é um arquivo válido."
        )

    os.remove(caminho_completo)


def ler_arquivo(nome_arquivo: str, diretorio: str = ".") -> str:
    """Lê e retorna o conteúdo de um arquivo."""

    caminho_completo = os.path.join(diretorio, nome_arquivo)

    if not os.path.exists(caminho_completo):
        raise FileNotFoundError(
            f"O arquivo '{nome_arquivo}' não existe."
        )

    if not os.path.isfile(caminho_completo):
        raise ValueError(
            f"'{nome_arquivo}' não é um arquivo válido."
        )

    with open(caminho_completo, "r", encoding="utf-8") as arquivo:
        return arquivo.read()



def renomear_arquivo(caminho_arquivo: str, novo_nome: str) -> str:
    """
    Renomeia um arquivo ou diretório.
    """
    caminho_arquivo = os.path.abspath(caminho_arquivo)

    
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(
            f"Arquivo ou diretório não encontrado: {caminho_arquivo}"
        )

    diretorio = os.path.dirname(caminho_arquivo)


    apenas_o_novo_nome = os.path.basename(novo_nome) 


    novo_caminho = os.path.join(
        diretorio,
        apenas_o_novo_nome
    )

    if os.path.exists(novo_caminho):
        raise FileExistsError(
            f"Já existe um item chamado '{apenas_o_novo_nome}' neste local."
        )

   
    os.rename(
        caminho_arquivo,
        novo_caminho
    )

    return novo_caminho