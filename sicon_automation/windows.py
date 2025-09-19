
import time
import pygetwindow as gw

class WindowController:
    @staticmethod
    def focar_e_maximizar_janela_contem(titulo_parcial, tentativas=10, espera=1):
        time.sleep(2)
        for _ in range(tentativas):
            for titulo in gw.getAllTitles():
                if titulo_parcial.lower() in titulo.lower():
                    janela = gw.getWindowsWithTitle(titulo)[0]
                    if not janela.isActive:
                        janela.activate()
                    if not janela.isMaximized:
                        janela.maximize()
                    return True
            time.sleep(espera)
        return False
