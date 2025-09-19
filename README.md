## SICON Automation - Relatórios de Estoque

## Este projeto é uma automação em Python desenvolvida para otimizar a rotina de geração e envio de relatórios de estoque no sistema SICON.
## O objetivo é eliminar tarefas manuais repetitivas, reduzindo erros e aumentando a produtividade.

⚙️ Fluxo da Automação

🗑️ Limpeza de pasta – remove arquivos antigos para evitar duplicações.

🌐 Login e navegação automática no SICON – acesso via navegador com pyautogui.

📥 Download do relatório de estoque em formato .slk.

🔄 Conversão automática de .slk para .csv.

📧 Envio por e-mail do relatório final para os responsáveis.

🛠️ Tecnologias Utilizadas

Python 3.x

PyAutoGUI → automação de interações na tela

Webbrowser → abertura do sistema SICON

Regex / CSV → parser e conversão de relatórios

Smtplib → envio automático de e-mails

Pathlib / OS → manipulação de arquivos

🚀 Como executar

## Clone este repositório:

git clone https://github.com/seu-usuario/sicon-automation-estoque.git


## Instale as dependências:

pip install -r requirements.txt


Configure seu e-mail e senha no arquivo emailer.py.

Defina a pasta de destino no config.py.

Rode o fluxo principal:

python main.py

📌 Observações

Necessário ter o SICON acessível no navegador.

O script interage com a tela, então recomenda-se não usar o computador durante a execução.

Pode ser agendado no Agendador de Tarefas do Windows para rodar automaticamente.