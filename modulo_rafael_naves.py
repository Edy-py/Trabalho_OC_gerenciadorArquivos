import shutil
from pathlib import Path


def excluir_diretorio(diretorio: str, local: str) -> str:
    """
    Exclui um diretório e todo o conteúdo (arquivos e subpastas) dentro dele.
    """
    caminho_completo = Path(local) / diretorio

    if caminho_completo.is_dir():
        # shutil.rmtree remove a árvore inteira de diretórios
        shutil.rmtree(caminho_completo)
        return f"Diretório '{diretorio}' excluído com sucesso."
    else:
        raise FileNotFoundError(
            f"O diretório '{diretorio}' não foi encontrado em '{local}'."
        )


def copiar_arquivo(
    nome_arquivo: str, diretorio_origem: str, diretorio_destino: str
) -> str:
    """
    Copia um arquivo de um diretório de origem para um diretório de destino.
    """
    caminho_origem = Path(diretorio_origem) / nome_arquivo
    caminho_destino = Path(diretorio_destino) / nome_arquivo

    if caminho_origem.is_file():
        # Cria a pasta de destino caso ela não exista ainda
        Path(diretorio_destino).mkdir(parents=True, exist_ok=True)

        # shutil.copy2 copia o arquivo preservando os metadados (data de criação, etc)
        shutil.copy2(caminho_origem, caminho_destino)
        return (
            f"Arquivo '{nome_arquivo}' copiado para '{diretorio_destino}' com sucesso."
        )
    else:
        raise FileNotFoundError(
            f"O arquivo '{nome_arquivo}' não foi encontrado em '{diretorio_origem}'."
        )


def copiar_diretorio(origem: str, destino: str) -> str:
    """
    Copia um diretório inteiro (com todos os arquivos e subpastas) para um novo local.
    """
    caminho_origem = Path(origem)
    # Define que a cópia ficará dentro do destino, com o mesmo nome da pasta original
    caminho_destino = Path(destino) / caminho_origem.name

    if caminho_origem.is_dir():
        # shutil.copytree copia toda a estrutura. dirs_exist_ok=True evita erro se a pasta destino já existir
        shutil.copytree(caminho_origem, caminho_destino, dirs_exist_ok=True)
        return f"Diretório '{origem}' copiado para '{destino}' com sucesso."
    else:
        raise FileNotFoundError(f"O diretório '{origem}' não existe.")
