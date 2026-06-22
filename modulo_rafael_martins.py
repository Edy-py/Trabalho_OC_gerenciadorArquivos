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


import os

import os


def renomear_arquivo(
    caminho_arquivo: str,
    novo_nome: str
) -> str:
    """
    Renomeia um arquivo.

    Args:
        caminho_arquivo: Caminho relativo ou absoluto do arquivo.
        novo_nome: Novo nome do arquivo.

    Returns:
        Caminho completo do arquivo renomeado.
    """

    caminho_arquivo = os.path.abspath(caminho_arquivo)

    if not os.path.isfile(caminho_arquivo):
        raise FileNotFoundError(
            f"Arquivo não encontrado: {caminho_arquivo}"
        )

    diretorio = os.path.dirname(caminho_arquivo)

    novo_caminho = os.path.join(
        diretorio,
        novo_nome
    )

    if os.path.exists(novo_caminho):
        raise FileExistsError(
            f"Já existe um arquivo chamado '{novo_nome}'"
        )

    os.rename(
        caminho_arquivo,
        novo_caminho
    )

    return novo_caminho