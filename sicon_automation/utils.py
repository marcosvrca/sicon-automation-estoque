
import os
import time
import subprocess
from pathlib import Path

def fechar_chrome():
    os.system("taskkill /im chrome.exe /f")

def fechar_excel():
    os.system("taskkill /im excel.exe /f")

def reiniciar_explorer():
    os.system("taskkill /f /im explorer.exe >nul 2>&1")
    time.sleep(2)
    subprocess.Popen("explorer")
    time.sleep(3)

def localizar_arquivo(pasta, padrao):
    arquivos = list(Path(pasta).glob(padrao))
    return max(arquivos, key=os.path.getctime) if arquivos else None
