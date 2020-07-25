# Weathify
Простой Telegram бот написанный на Python 3.x который умеет показывать погоду указанную пользователем
### Что умеет бот
* Умеет показывать погоду
* Умеет показывать температуру
* Умеет показывать силу ветра
* Умеет показывать влажность
* Умеет давать рекомендации, в зависимости от температуры 
### Использованные библиотеки и репозитории
* [PyOWM](https://github.com/csparpa/pyowm) - для работы с API OpenWeather.org
* [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - для работы с API Telegram (BotFather)
### Быстрый старт
* В ниже представленную строчку вставляем свой ключ API, который Вы должны получить на [этом](https://openweathermap.org/) сайте
```python
    ## Ключ API OpenWeather.org для работы PyOWM
    owm = pyowm.OWM('ваш API ключ с сайта openweathermap.org', config_dict)
```
* Далее Вам надо получить API ключ у [BotFather](https:/t.me/BotFather) в Telegram и вставить его в код приведённый ниже
```python
    ## Ключ API Telegram для работы бота
    bot = telebot.TeleBot('ваш API ключ полученный от BotFather'a')
```
* Запускаем код через консоль или нажимаем на зелёный треугольник (значок play) в Visual Studio Code
