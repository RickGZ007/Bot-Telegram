import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Conexão com o bot
TOKEN = ''
bot = telebot.TeleBot(TOKEN)

# Comando /start com botões
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("🗓️ Próximo jogo", callback_data="next_game"),
        InlineKeyboardButton("🎮 Quiz da FURIA", callback_data="quiz_1"),
        InlineKeyboardButton("🤓 Curiosidades", callback_data="facts")
    )
    bot.send_message(message.chat.id, "Salve fã da FURIA! Escolha uma opção:", reply_markup=markup)

# Comando /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Você pode interagir comigo usando comandos ou clicando nos botões. Em breve terei mais novidades!")

# Quiz perguntas e respostas
quiz_perguntas = {
    "quiz_1": {
        "pergunta": "Qual jogador é conhecido pelo estilo agressivo e pela famosa 'rushadinha'?",
        "opcoes": ["arT", "FalleN", "KSCERATO", "fer"],
        "correta": "arT",
        "proxima": "quiz_2"
    },
    "quiz_2": {
        "pergunta": "Em que ano a FURIA foi considerada top 1 da América do Norte?",
        "opcoes": ["2018", "2019", "2020", "2021"],
        "correta": "2020",
        "proxima": "quiz_3"
    },
    "quiz_3": {
        "pergunta": "Qual é o animal símbolo da organização FURIA?",
        "opcoes": ["Tigre", "Pantera", "Lobo", "Águia"],
        "correta": "Pantera",
        "proxima": None
    }
}

usuarios_pontuacao = {}

# Callback dos botões e quiz
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "next_game":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🔴 Próxima partida: FURIA vs NAVI, 04/05 às 17h - IEM Dallas 🏆")

    elif call.data == "facts":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Você sabia? A FURIA foi top 1 NA em 2020 e tem a torcida mais fiel do CS:GO brasileiro! 🇧🇷")

    elif call.data.startswith("quiz_"):
        pergunta_data = quiz_perguntas.get(call.data)
        if pergunta_data:
            markup = InlineKeyboardMarkup()
            for opcao in pergunta_data["opcoes"]:
                markup.add(InlineKeyboardButton(opcao, callback_data=f"resposta_{call.data}_{opcao}"))
            bot.send_message(call.message.chat.id, pergunta_data["pergunta"], reply_markup=markup)

    elif call.data.startswith("resposta_"):
        partes = call.data.split("_")
        pergunta_id = f"{partes[1]}_{partes[2]}"
        resposta = "_".join(partes[3:])
        pergunta_data = quiz_perguntas.get(pergunta_id)

        correta = pergunta_data["correta"]
        proxima = pergunta_data["proxima"]
        user_id = call.from_user.id

        if user_id not in usuarios_pontuacao:
            usuarios_pontuacao[user_id] = 0

        if resposta == correta:
            usuarios_pontuacao[user_id] += 1
            bot.send_message(call.message.chat.id, f"✅ Correto, {call.from_user.first_name}! Pontuação: {usuarios_pontuacao[user_id]}")
        else:
            bot.send_message(call.message.chat.id, f"❌ Errado! A resposta certa era: {correta}. Pontuação: {usuarios_pontuacao[user_id]}")

        if proxima:
            callback_query(type('call', (object,), {'data': proxima, 'message': call.message, 'from_user': call.from_user, 'id': call.id}))
        else:
            bot.send_message(call.message.chat.id, f"🎉 Fim do quiz! Sua pontuação final: {usuarios_pontuacao[user_id]} / 3")

# Resposta padrão
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Use os botões ou comandos /start e /help para interagir comigo 😉")

# Iniciar o bot
if __name__ == "__main__":
    print("FURIA Bot está online!")
    bot.polling(none_stop=True)