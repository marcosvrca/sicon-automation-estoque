
import smtplib
from datetime import datetime
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class EmailSender:
    def __init__(self, pasta_destino):
        self.from_address = "SEU_EMAIL"
        self.password = "SUA_SENHA"
        self.to_addresses = ["destinatario1@email.com"]
        self.admin_email = ["admin@email.com"]
        self.subject = "Relatório de Estoque - Envio Automático"
        self.body = "Olá, segue em anexo o relatório de estoque do dia."
        self.pasta_destino = Path(pasta_destino)
        self.log_dir = Path("logs")
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_dir / f"log_{datetime.now():%Y%m%d}.log"

    def log(self, message):
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} - {message}\n")

    def enviar_email(self, destinatarios, assunto, corpo, anexo=None):
        msg = MIMEMultipart()
        msg['From'] = self.from_address
        msg['To'] = ", ".join(destinatarios)
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo, 'plain'))

        if anexo:
            with open(anexo, "rb") as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={Path(anexo).name}')
                msg.attach(part)

        try:
            server = smtplib.SMTP('smtp.office365.com', 587)
            server.starttls()
            server.login(self.from_address, self.password)
            server.sendmail(self.from_address, destinatarios, msg.as_string())
            server.quit()
            self.log(f"E-mail enviado para: {', '.join(destinatarios)}")
            return True
        except Exception as e:
            self.log(f"Erro ao enviar e-mail: {e}")
            return False

    def enviar_relatorio(self):
        csv_files = list(self.pasta_destino.glob("PosicaoGeralEstoque*.csv"))
        if not csv_files:
            raise FileNotFoundError("Nenhum CSV encontrado para envio.")
        arquivo = max(csv_files, key=os.path.getctime)
        return self.enviar_email(self.to_addresses, self.subject, self.body, anexo=arquivo)

    def enviar_erro_final(self, erro_detalhes):
        self.enviar_email(
            self.admin_email,
            "ERRO - Envio do Relatório de Estoque",
            f"Ocorreu um erro na execução automática:\n\n{erro_detalhes}"
        )
