🐾 FURIA Bot – Telegram Bot com Telebot
Este é um bot interativo feito em Python com a biblioteca PyTelegramBotAPI (Telebot), voltado para fãs da equipe de eSports FURIA. O bot permite acompanhar o próximo jogo, responder a um quiz temático e conhecer curiosidades da organização.

🚀 Funcionalidades
Comando /start com menu interativo usando botões

Comando /help com orientações de uso

Quiz com perguntas sobre a FURIA, com sistema de pontuação

Informações sobre o próximo jogo

Curiosidades da organização

Respostas automáticas para qualquer mensagem não reconhecida

📦 Requisitos
Python 3.7+

Biblioteca pyTelegramBotAPI

No arquivo main.py, substitua a variável TOKEN com o seu token de acesso do Bot:

python
Copiar
Editar
TOKEN = 'SEU_TOKEN_AQUI'
Execute o bot:
python main.py
🎯 Exemplo de uso
Envie /start para ver as opções.

Clique em “🎮 Quiz da FURIA” para testar seus conhecimentos.

Envie qualquer mensagem para ver a resposta padrão.

📁 Estrutura do Projeto
bash

furia-bot/
├── main.py # Código principal do bot
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo
📌 Observações
O bot usa InlineKeyboardMarkup para interação com botões.

As respostas do quiz são tratadas via callback queries com sistema de pontuação por usuário.

O conteúdo é voltado ao universo FURIA (CS:GO).
