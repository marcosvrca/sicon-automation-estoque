
from pathlib import Path

class LimparPasta:
    @staticmethod
    def limpar_pasta(pasta):
        pasta = Path(pasta)
        for arquivo in pasta.glob("*"):
            try:
                arquivo.unlink()
            except Exception as e:
                print(f"Erro ao excluir {arquivo}: {e}")
