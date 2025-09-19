
import time
import traceback
from config import PASTA_DESTINO
from sicon_automation.sicon import SiconAutomator
from sicon_automation.converter import SLKConverter
from sicon_automation.emailer import EmailSender
from sicon_automation.cleaner import LimparPasta
from sicon_automation.utils import fechar_chrome, fechar_excel, reiniciar_explorer, localizar_arquivo

def rodar_fluxo(emailer):
    try:
        LimparPasta.limpar_pasta(PASTA_DESTINO)
        automator = SiconAutomator(PASTA_DESTINO)
        automator.executar()

        arquivo_slk = localizar_arquivo(PASTA_DESTINO, "PosicaoGeralEstoque*.slk")
        if not arquivo_slk:
            raise FileNotFoundError("Arquivo SLK não foi gerado.")

        conversor = SLKConverter(PASTA_DESTINO)
        conversor.converter(arquivo_slk)
        return emailer.enviar_relatorio()

    except Exception as e:
        emailer.log(f"Erro no fluxo: {e}")
        fechar_chrome()
        return False

if __name__ == "__main__":
    emailer = EmailSender(PASTA_DESTINO)
    try:
        tentativas = 0
        while tentativas < 4:
            tentativas += 1
            if rodar_fluxo(emailer):
                print("✅ Processo concluído com sucesso.")
                break
            else:
                emailer.log(f"❌ Tentativa {tentativas} falhou. Reiniciando...")
                fechar_chrome()
                fechar_excel()
                reiniciar_explorer()
                time.sleep(3)
        else:
            raise Exception("Falha após 4 tentativas.")

    except Exception:
        erro_detalhes = traceback.format_exc()
        emailer.log(f"Erro fatal:\n{erro_detalhes}")
        fechar_chrome()
        emailer.enviar_erro_final(erro_detalhes)
