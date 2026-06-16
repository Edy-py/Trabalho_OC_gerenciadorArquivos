from pathlib import Path
from typing import List

def listar_arquivos(diretorio: str | Path) -> List[Path]:
    """Lista todos os arquivos de um diretório."""
    
    caminho = Path(diretorio)
    if not caminho.exists():
        raise FileNotFoundError(f"O diretório '{diretorio}' não existe.")
    if not caminho.is_dir():
        raise NotADirectoryError(f"O caminho '{diretorio}' não é um diretório válido.")
    return [item for item in caminho.iterdir() if item.is_file()]


def criar_diretorio(nome_diretorio: str, diretorio_pai: str | Path = ".") -> Path:
    """Cria um diretório de forma segura."""

    caminho_completo = Path(diretorio_pai) / nome_diretorio
    caminho_completo.mkdir(parents=True, exist_ok=True)
    return caminho_completo


def criar_arquivo(nome_arquivo: str, conteudo: str = "", diretorio_pai: str | Path = ".") -> Path:
    """Cria um arquivo no diretório especificado."""

    caminho_completo = Path(diretorio_pai) / nome_arquivo
    caminho_completo.parent.mkdir(parents=True, exist_ok=True)
    caminho_completo.write_text(conteudo, encoding="utf-8")
    return caminho_completo