
import pyautogui
import webbrowser
import time
from .windows import WindowController
from .utils import fechar_chrome

class SiconAutomator:
    def __init__(self, pasta_destino):
        self.pasta_destino = pasta_destino
        self.window = WindowController()

    def clicar(self, x, y, delay=0.5):
        pyautogui.click(x, y)
        time.sleep(delay)

    def executar(self):
        webbrowser.open("https://siconnet.scania.com.br/sicomnet3/mcm/sicomweb.gen.gen.pag.Login.cls")
        time.sleep(8)
        self.window.focar_e_maximizar_janela_contem("SICONnet - Login")

        self.clicar(1891, 110)
        self.clicar(1857, 112)
        time.sleep(6)

        self.window.focar_e_maximizar_janela_contem("SICONnet")

        self.clicar(34, 136)
        self.clicar(27, 194)
        self.clicar(171, 293)
        self.clicar(291, 514)

        self.clicar(1279, 216)
        self.clicar(950, 248)
        self.clicar(1275, 344)
        self.clicar(246, 395)

        self.clicar(252, 386)
        pyautogui.write("1")
        pyautogui.press("tab")

        self.clicar(252, 426)
        pyautogui.write("E")
        pyautogui.press("tab")

        self.clicar(247, 508)
        pyautogui.write("1")

        self.clicar(882, 596)
        self.clicar(648, 669)
        self.clicar(762, 653)

        if not self.window.focar_e_maximizar_janela_contem("Salvar como", tentativas=60, espera=1):
            raise TimeoutError("Janela 'Salvar como' não apareceu.")

        self.clicar(495, 56)
        pyautogui.write(self.pasta_destino)
        pyautogui.press("enter")
        time.sleep(1)
        self.clicar(1754, 990)

        time.sleep(5)
        fechar_chrome()
