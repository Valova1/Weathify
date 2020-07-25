![logo](https://github.com/dmitrylaas/Weathify/blob/master/images/logo.png)
# Weathify
Простой Telegram бот написанный на Python 3.x который умеет показывать погоду указанную пользователем
>Хочу обратить Ваше внимание на то, что это не проект, но может быть им будет. Использовать исходный код можно, иначе было бы глупо запретить его использование, так как есть куча уроков по созданию идентичного бота. Вообще, в планах доработать этот код, поэтому сильно не копипастите. Спасибо за понимание :)
### Что умеет бот
* Умеет показывать погоду
* Умеет показывать температуру
* Умеет показывать силу ветра
* Умеет показывать влажность
* Умеет давать рекомендации, в зависимости от температуры 
### Использованные библиотеки и репозитории
* [PyOWM](https://github.com/csparpa/pyowm) - для работы с API OpenWeather.org
* [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - для работы с API Telegram (BotFather)
* [Smashicons](https://www.flaticon.com/authors/smashicons) - иконка для бота
### Быстрый старт
* В ниже представленную строчку вставляем свой ключ API, который Вы должны получить на [этом](https://openweathermap.org/) сайте
```python
    ## Ключ API OpenWeather.org для работы PyOWM
    owm = pyowm.OWM('ваш API ключ с сайта openweathermap.org', config_dict)
```
* Далее Вам надо получить API ключ у [BotFather](https://t.me/BotFather) в Telegram и вставить его в код приведённый ниже
```python
    ## Ключ API Telegram для работы бота
    bot = telebot.TeleBot('ваш API ключ полученный от BotFather'a')
```
* Запускаем код через консоль или нажимаем на зелёный треугольник (значок play) в Visual Studio Code
### Скриншоты (результат)
| Скриншот 1 | Скриншот 2 |
| :----: | :----: |
|![one](https://github.com/dmitrylaas/Weathify/blob/master/images/screenshot_1.png) |![two](https://github.com/dmitrylaas/Weathify/blob/master/images/screenshot_2.png) |
