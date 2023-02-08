<p align="center"><img src="https://ae04.alicdn.com/kf/HTB1dM3GXFY7gK0jSZKzq6yikpXaF.jpg" height="500"/></p>
<h1 align="center">ConverterBot for Telegram</h1>
<h3 align="center">made by <a href="https://github.com/NeMoSemi" target="_blank">Nemo_Semi</a></h3>
<a>
<p>Описание проекта:</p>
<p>Данный проект реализовывает телеграм бота, благодаря которому пользователь может узнать актуальный курс валют</p>
<p>Код:</p>
<p>1. В файле main.py находится основная логика бота. После получения ботом команды /start создаются кнопки с валютами, названия валют берутся из словаря. Далее пользователю отправляется приветственное сообщение, а также его id и некоторая информация о нём сохраняется в память бота(users_list.txt). При вызове команды /help пользователю будет отправленно сообщение с некой информацией позволяющей разобраться с интерфейсом бота. В остальных случаях, т.е. при отправке обычных сообщений существует 2 исхода: 1. Бот не распознаёт валюту или сообщение введённое пользователем некорректное, 2. Бот запрашивает курс валюты и отправляет его пользователю.</p>
<p>2. В файле file_for_functions.py как понятно из названия лежат вспомогательные функции. Функция is_spam позволяет отслеживать флуд и блокировать пользователя на заданное время если тот отправил более определённого количества сообщений за какой-то промежуток времени(все эти параметры можно настроить), данная функция вызывается после каждого запроса валюты, а фунция if_id_in_file позволяет проверить наличие пользователя в users_list.txt</p>
</a>
