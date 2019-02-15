import telebot
import const
import time



bot=telebot.TeleBot(const.token)

upd = bot.get_updates();
print(upd)
last_upd = upd[-1]
message_from_user=last_upd.message
#print(message_from_user)
@bot.message_handler(commands=['start'])
def hendle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard='True');
    user_markup.row('ДА')
    user_markup.row('ОЧЕНЬ')
    user_markup.row('Пойду  еще на один Курс')
    bot.send_message(message.from_user.id,'Добро пожаловать ' + message.from_user.first_name , reply_markup=user_markup)
    bot.send_message(message.chat.id,'Вам нравяться Курсы А-level?')
    


@bot.message_handler(regexp="ДА")
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True,one_time_keyboard='True')
    button_phone = telebot.types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = telebot.types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!", reply_markup=keyboard)
    print(last_upd.message)
@bot.message_handler(regexp="ОЧЕНЬ")
def geophone(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard='True');
    user_markup.row('1','2','3')
    user_markup.row('4','5','6')
    user_markup.row('7','8','9')
    bot.send_message(message.from_user.id,'А какая оценка преподователю?', reply_markup=user_markup)
    bot.send_message(348814433,message)
    
    
#@bot.message_handler(content_types=['text'])
#def hendle_text(message):
#    user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard='True');
#    user_markup.keyboard.keybordbuttn.request_contact = 'True'
#    user_markup.row('телефон')
#    telefone = message.text;
#    user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard='True');
#    user_markup.row('1','2','3')
#    user_markup.row('4','5','6')
#    user_markup.row('7','8','9')
#    bot.send_message(message.from_user.id,message.from_user.first_name , reply_markup=user_markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)