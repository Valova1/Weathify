## Импорты библиотек
import pyowm
from pyowm.utils.config import get_default_config
import telebot
## Конфигурация языковых параметров для библиотеки PyOwm
config_dict = get_default_config()
config_dict['language'] = 'ru'
## Ключ API OpenWeather.org для работы PyOwm
owm = pyowm.OWM('cc53fdcad5ab0252e30bf537f00f1e9d', config_dict)
## Ключ API Telegram для работы бота
bot = telebot.TeleBot('1260087893:AAF6XfjqETTzCQkUBR6N7jy6muWH-xgkKqc')
## Распознования команд и ответ на них
@bot.message_handler(commands=['start', 'weather'])
def send_welcome(message):
	bot.reply_to(message, "Пожалуйста, напишите полное название города, в котором нужно узнать погоду")
## Вывод резултата погоды с серверов OpenWeather.org
@bot.message_handler(content_types = ['text'])
def send_echo(message):
      ## Менеджер
      mgr = owm.weather_manager()
      observation = mgr.weather_at_place(message.text)
      w = observation.weather
      ## Переменная температуры
      temp = w.temperature('celsius')['temp']
      ## Переменная скорости ветра
      wind_speed = w.wind()['speed']
      ## Сам ответ пользователю
      answer = "Сейчас за окном " + w.detailed_status + "\n"
      answer += "Текущая температура:  " + str(temp) + " ℃" + "\n"
      answer += "Скорость ветра:  " + str(wind_speed) + " м/с" + "\n"
      answer += "Влажность:  " + str(w.humidity) + "%" + "\n\n"
      ## Рекомендации (опционально, без них тоже всё будет работать прекрасно)
      ## Если температура меньше 10 ℃, то...
      if temp < 10:
            answer += "На улице холодно. Пожалуйста, одевайтесь теплее"
      ## Если температура меньше 20 ℃, то...
      elif temp < 20:
            answer += "На улице прохладно. Пожалуйста, одевайтесь теплее"
      ## Если температура больше 20 ℃, то...
      elif temp > 20:
            answer += "На улице тепло. Можете одевать лёгкую одежду"
      ## Если температура больше 28 ℃, то...
      elif temp >= 28:
            answer += "На улице жарко. Можете одевать лёгкую одежду, но не забудьте про головной убор"
      ## Инициализация ответа
      bot.reply_to(message, answer)
## Запуск бота
bot.polling( none_stop = True )