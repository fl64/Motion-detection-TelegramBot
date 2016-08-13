# Motion-detection-TelegramBot

![](https://raw.githubusercontent.com/fl64/Motion-detection-TelegramBot/c7db15d6ff2614820ebb2078b383b3e9edc3914a/pri2.JPG)

## Intro
- Телеграм-бот для получения фото с веб-камеры в случае фиксации ей какого-либо движения.
- Тестировался и отлаживался на Rasberry Pi2 с Ubuntu Server 16.04. Описание установки Ubuntu Server доступно по ссылке: https://wiki.ubuntu.com/ARM/RaspberryPi

## Install
1. Производим установку ОС :)
2. Подключаем камеру
3. Установка motion:
	- Устанавливаем пакет motion: ```sudo apt install motion```
	- Производим корректировку настроек в ```/etc/motion/motion.conf``` (Пример настроек есть в репозитории). 
	- По-умолчанию бот мониторинг фото в каталоге ```/tmp```
	- Для запуска motion в виде сервиса, в файле ```/etc/default/motion``` устаналиваем следующее занчение параметра: ```start_motion_daemon=yes```
	- Производим настройки сервиса motion:
		- ``` systemctl enable motion ```
    	- ``` systemctl start motion  ```
4. Регистрация бота
	- Добавляем в телеграме бота @BotFather
	- Вводим ```/newbot```
	- Далее задаем имя бота и его username.
	- После завершения предыдущих шагов @BotFather выдаст токен для бота. Его необходимо будет задать в переменной token в bot.py.
	- Вводим ```/setcommands```, и добавляем команды (не обязательно)
		- start - start
		- stop - stop
5. Установка бота
	- Устанавливаем pip3 и необходимые библиотеки:
		- ```sudo apt-get install python3-pip```
		- ```sudo pip3 install --upgrade pip```
		- ```sudo pip3 install telepot```
		- ```sudo pip3 install watchdog```
	- Создаем каталог ```mkdir /opt/bot``` и копируем в него ```bot.py```
	- Отредактируем ```bot.py```
		- **password** - пароль для подключения к боту
		- **monitor_path** - каталог, где мониторятся файлы "*.jpg"
		- **teletoken** - токен для бота, полученный на шаге 4.
	- В каталог ```/etc/systemd/system/``` копируем файл ```bot.service```
	- Регистрируем сервис бота
		- ```systemctl enable bot```
		- ```systemctl start bot```
6. Проверка
	- В телеграм производим поиска бота по ранее заданному имени
	- Запускаем бота коммандой ```/start password```
	- Для остановки работы бота ввести: ```/stop```

Созданно под впечатлением: https://github.com/Surzhikov/Telegram-Webcam-Home-Guard :)
