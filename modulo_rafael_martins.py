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


def renomear_arquivo(
    nome_antigo: str,
    nome_novo: str,
    diretorio: str = "."
) -> str:
    """Renomeia um arquivo."""

    caminho_antigo = os.path.join(diretorio, nome_antigo)

    if not os.path.exists(caminho_antigo):
        raise FileNotFoundError(
            f"O arquivo '{nome_antigo}' não existe."
        )

    caminho_novo = os.path.join(diretorio, nome_novo)

    os.rename(caminho_antigo, caminho_novo)

    return caminho_novo